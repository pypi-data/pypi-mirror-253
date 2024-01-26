import os
import sys
import shutil
import time
import importlib
import functools
import operator
import numpy as np
import torch

from . import system
from .io import LoadableModule
from .config import load_config
from .device import configure_device


class BaseModelTrainer:

    def __init__(self, basedir):
        """
        Universal model training base class.

        When subclassing the base model trainer, the following two steps must be done:

            1. In the __init__() method of the subclass, the following parameters need to
               be manually defined:

               self.model: The initialized torch model to be trained.
               self.optimizer: The initialized torch optimizer to train the model.

            2. The sample() method must be overridden to return training data samples

        Additional options can be specified or overridden in the config yaml file or in
        the initialization.
        """
        self.basedir = basedir

        # load the training config file
        self.config = load_config(self.basedir)
        
        # by default, all model training is done on the gpu. don't see why not
        self.device = configure_device(verbose=True)

        # init the model and optimizers. these should be set in the
        # configure method of any subclasses (see below)
        self.model = None
        self.optimizer = None
        self.min_lr = None

        # some initializations
        self.initial_epoch = 1
        self.current_epoch = 1
        self.last_loss_spike_epoch = 1
        self.loss_weights = {}
 
        # the number of standard deviations that a step loss can increase before
        # being considered a loss spike
        self.loss_spike_factor = 4 

        # the number of epochs to wait after a loss spike before another can be detected
        self.loss_spike_cooldown = 2

        # if this is enabled, then sampled batches are actually not batched at all, i.e.
        # the output of batch() is just the output of sample(). this only works when batch
        # size is 1 and will fail otherwise
        self.unbatched = False

        # mixed precision - to enable, specify the self.mixed_type floating point datatype
        # and configure the self.grad_scaler gradient scalar, if necessary. if you use this
        # you'll probably want to review the torch mixed precision documentation
        self.mixed_type = None
        self.grad_scaler = None

        # provide support for W&B (Weights and Biases) which is an ML ops platform
        # to track model training online - highly recommended
        self.wandb = None
        if self.config.opt('wandb/enable', False):
            try:
                import wandb
            except ModuleNotFoundError:
                system.fatal('Weights and Biases has been enabled in the training config, '
                             'but the module is not installed. Either install the `wandb` '
                             'python package or disable its usage in the config.')
            self.wandb = wandb
            self.wandb_configure_run()

    @property
    def initial_epoch(self):
        return self._initial_epoch

    @initial_epoch.setter
    def initial_epoch(self, epoch):
        differs = epoch != getattr(self, '_initial_epoch', None)
        self._initial_epoch = epoch
        if differs:
            self.on_initial_epoch_set(epoch)

    def wandb_configure_run(self):
        """
        Initialize the W&B run (if enabled). All W&B suboptions in the training
        config yaml file will be passed to the wandb init fuction.
        """
        if self.wandb is None:
            return
        options = self.config.opt('wandb').copy()
        options.pop('enable')
        options['dir'] = self.basedir
        if options.get('name') is None:
            options['name'] = os.path.basename(self.basedir)
        self.wandb.init(**options)

    def wandb_log(self, data, **kwargs):
        """
        Log step information to the W&B run (if enabled).

        Parameters
        ----------
        data : dict or wandb.Table
            Data to be logged to W&B.
        **kwargs : dict, optional
            Additional arguments to be passed to `wandb.log()`.
        """
        if self.wandb is None:
            return
        self.wandb.log(data, **kwargs)

    def wandb_finish(self):
        """
        Finish the W&B run (if enabled).
        """
        if self.wandb is None:
            return
        self.wandb.finish()

    def load_checkpoint(self, epoch, load_optimizer=True):
        """
        Load checkpoint weights from a given epoch number. This function loads
        the checkpoint file from the 'checkpoints' subdirectory in the base model
        output folder.

        Parameters
        ----------
        epoch : int
            The epoch number to load checkpoint weights from.
        load_optimizer : bool, optional
            Whether to load optimizer parameters from the checkpoint file as well.
        """
        filename = os.path.join(self.basedir, 'checkpoints', f'{epoch:05d}.pt')
        self.load_weights(filename, load_optimizer=load_optimizer)
        self.initial_epoch = epoch
        self.current_epoch = epoch
        self.on_checkpoint_loaded(epoch)

    def load_weights(self, filename, load_optimizer=True):
        """
        Load weights from a given file into the initialized model. This function
        also (optionally) loads optimizer parameters from the checkpoint file
        if they exist.

        Parameters
        ----------
        filename : str
            The path to the file containing the weights.
        load_optimizer : bool, optional
            Whether to load optimizer parameters from the file.
        """
        print(f'Loading weights from {filename}.')
        checkpoint = torch.load(filename)
        self.model.load_state_dict(checkpoint['model_state_dict'], strict=False)
        optimizer_state = checkpoint.get('optimizer_state_dict')
        if optimizer_state is not None and load_optimizer:
            try:
                self.optimizer.load_state_dict(optimizer_state)
            except:
                warning('Could not load optimizer state from weights file, '
                        'perhaps the model architecture has changed')

    def sample(self):
        """
        This is the primary data generation function that must be implemented for any
        subclass of the BaseModelTrainer. This function must return a dictionary of
        objects corresponding to a single training data point. These returned objects
        will be eventually stacked by the batch() method, where any returned tensors
        will also be stacked into a single batched tensor and placed on the training
        device, if they aren't already.

        Returns
        -------
        sample : dict
            Dictionary containing tensors and other necessary information corresponding
            to a single training data point.
        """
        raise NotImplementedError(f'sample() method must be implemented in {self.__class__.__name__}')

    def batch(self, batch_size):
        """
        This function creates a training batch by stacking the individual outputs of
        the sample() method. For every set of tensor items returned by sample(), this
        function will create a tensor stack along the first axis and transfer the batched
        tensor to the training device. Every set of non-tensor item will be simply converted
        to a list and kept on the CPU.

        Parameters
        ----------
        batch_size : int, optional
            Size of the returned data batch.

        Returns
        -------
        batched : dict
            Dictionary containing stacked tensors and other necessary information corresponding
            to a batch of training data.
        """
        batch_sample = {}
        for i in range(batch_size):

            # get a single sample
            sample = self.sample()

            # make sure the sample is a dictionary
            if not isinstance(sample, dict):
                raise ValueError('The output of the sample() method must be a dictionary of objects '
                                f'and tensors, but got type {sample.__class__.__name__}.')

            # stack dictionary items across batches
            for key, item in sample.items():
                if i == 0:
                    batch_sample[key] = [item]
                else:
                    batch_sample[key].append(item)

        # find the batched items that are tensors, stack them into a single tensor,
        # and ensure they are on the correct training device
        for key, item in batch_sample.items():
            if isinstance(item[0], torch.Tensor):
                batch_sample[key] = torch.stack(item).to(self.device)

        return batch_sample

    def inspect(self):
        """
        This is the data inspection method that can be implemented for any subclass
        of the BaseModelTrainer. This optional method is called whenever the '--inspect'
        flag is provided to the 'ds train' command. It is meant to facilitate visualizing
        and debugging data samples. Due to the diversity of outputs that might be
        returned by the sample() funtion, this method must be implemented manually for
        each subclass.
        """
        raise NotImplementedError(f'inspect() method has not been implemented for class {self.__class__.__name__}')

    def train(self):
        """
        """

        # make sure the subclass has included the super constructor
        if not getattr(self, 'basedir'):
            raise NotImplementedError(f'The __init__ method of {self.__class__.__name__} must '
                                       'include a call to super().__init__()')

        # make sure model has been configured
        if self.model is None:
            raise NotImplementedError(f'self.model must be configured in the __init__ method '
                                      f'of the {self.__class__.__name__} subclass')
        print(f'Training model {self.model.__class__.__name__}.')

        # make sure optimizer has been configured
        if self.optimizer is None:
            raise NotImplementedError(f'self.optimizer must be configured in the __init__ method '
                                      f'of the {self.__class__.__name__} subclass')
        print(f'Using optimizer {self.optimizer.__class__.__name__}.')

        # get some configurable optimization options
        batch_size       = self.config.opt('optimization/batch_size', 1)
        accumulations    = self.config.opt('optimization/accumulations', 1)
        steps_per_epoch  = self.config.opt('optimization/steps_per_epoch', 100)
        checkpoint_freq  = self.config.opt('optimization/checkpoint_freq', 20)
        validation_freq  = self.config.opt('optimization/validation_freq', 20)

        print(f'Using a batch size of {batch_size} with {steps_per_epoch} steps per epoch.')

        # make the checkpoint output directory under the basedir
        os.makedirs(os.path.join(self.basedir, 'checkpoints'), exist_ok=True)

        # helper function to save the model checkpoints with particular formatting
        def save_epoch():
            filename = os.path.join(self.basedir, 'checkpoints', f'{self.current_epoch:05d}.pt')
            if isinstance(self.model, LoadableModule):
                self.model.save(filename, optimizer_state_dict=self.optimizer.state_dict())
            else:
                system.warning(f'{self.model.__class__.__name__} does not subclass '
                               'LoadableModule, so it will not be saved with '
                               'configuration info.')
                torch.save({
                    'epoch': epoch,
                    'model_state_dict': self.model.state_dict(),
                    'optimizer_state_dict': self.optimizer.state_dict(),
                    }, filename)

        # print info about training start
        if self.initial_epoch == 1:
            print(f'Starting training:')
        else:
            print(f'Picking up training from epoch {self.initial_epoch}:')

        # these are used for tracking spikes in the loss and will be set
        # after the first epoch is completed
        epoch_loss_mean = None
        epoch_loss_std = None

        # training loops
        self.current_epoch = self.initial_epoch
        while True:

            # get the epoch start time for profiling purposes
            if self.device.type == 'cuda':
                torch.cuda.synchronize()
            epoch_start_time = time.perf_counter()

            # initialize a buffers to track the individual losses and total losses
            # across each step in this epoch
            epoch_individual_loss_means = {}
            epoch_total_losses = []

            for step in range(steps_per_epoch):

                # reset optimizer
                self.optimizer.zero_grad(set_to_none=True)

                # loop over the number of forward steps. this will only be greater than
                # one when gradient accumulation is enabled
                for _ in range(accumulations):

                    # sample a training batch
                    if not self.unbatched:
                        batch_sample = self.batch(batch_size)
                    else:
                        # to prevent misuse, we should ensure the batch size is 1 when batching is disabled
                        if batch_size != 1:
                            raise ValueError('Trainer has `unbatched == True` but the specified '
                                            f'batch size is {batch_size}, not 1')
                        batch_sample = self.sample()
                        for key, item in batch_sample.items():
                            if isinstance(item, torch.Tensor):
                                batch_sample[key] = item.to(self.device)

                    # compute the forward training step
                    use_mixed = self.mixed_type is not None
                    with torch.autocast(self.device.type, dtype=self.mixed_type, enabled=use_mixed):
                        result = self.step(batch_sample)

                        # if the loss result is a dictionary, then we gather some
                        # info about each individual returned loss and apply the weighting
                        if isinstance(result, dict):
                            for name, loss in result.items():
                                # cache the mean values by accumulating over the epoch
                                # as opposed to actually storing each loss value
                                scaled = loss.item() / steps_per_epoch
                                if epoch_individual_loss_means.get(name) is None:
                                    epoch_individual_loss_means[name] = scaled
                                else:
                                    epoch_individual_loss_means[name] += scaled

                            # apply specified weights to each indiviual loss
                            for name, weight in self.loss_weights.items():
                                loss = result.get(name)
                                if loss is None:
                                    continue
                                if weight < 1e-8:
                                    result.pop(name)
                                else:
                                    result[name] = loss * weight

                            # sum the weighted individual losses
                            total_loss = functools.reduce(operator.add, result.values())
                        else:
                            # if the return loss is not a dictionary, assume it's a single
                            # value that does not need to be weighted or anything
                            total_loss = result

                        # cache the total loss for this step
                        epoch_total_losses.append(total_loss.item())

                        # scale by number of accumulations
                        if accumulations > 1:
                            total_loss /= accumulations

                    # scale gradients for mixed precision (if necessary)
                    if self.grad_scaler is not None:
                        total_loss = self.grad_scaler.scale(total_loss)

                    # compute gradients for this accumulation step
                    total_loss.backward()

                # step the optimizer
                if self.grad_scaler is not None:
                    self.grad_scaler.step(self.optimizer)
                    self.grad_scaler.update()
                else:
                    self.optimizer.step()

                # call step hook
                self.on_step_end(step)

            # compute the average step time across the epoch
            if self.device.type == 'cuda':
                torch.cuda.synchronize()
            iter_time = (time.perf_counter() - epoch_start_time) / steps_per_epoch

            # compute some total loss stats for this epoch
            epoch_loss_mean = np.mean(epoch_total_losses)
            epoch_loss_std = np.std(epoch_total_losses)

            # get the current learning rate
            lr = self.optimizer.param_groups[0]['lr']

            # prepare an epoch info dictionary for logging purposes
            epoch_info = {
                'Scale/Epoch': self.current_epoch ,
                'Scale/Iter': self.current_epoch * steps_per_epoch,
                'General/Iter Time': iter_time,
                'General/LR': lr,
                'Loss/Total': epoch_loss_mean,
            }

            # include each individual mean loss value
            for name, loss in epoch_individual_loss_means.items():
                epoch_info[f'Loss/{name}'] = loss

            # include each individual loss weight
            for name, weight in self.loss_weights.items():
                epoch_info[f'Loss Weight/{name}'] = weight

            # run the validation method
            if self.current_epoch % validation_freq == 0 and self.current_epoch != self.initial_epoch:
                # make sure to disable gradient computations
                with torch.no_grad():
                    self.model.train(False)
                    metrics = self.validate()
                    self.model.train(True)
                self.on_validation_end(metrics, self.current_epoch)
                if metrics is not None:
                    epoch_info.update({f'Validation/{k}': m for k, m in metrics.items()})

            # send epoch info to W&B
            self.wandb_log(epoch_info)

            # print out a command-line summary - this of course doesn't include everything,
            # but just some basic stuff like loss values and timing
            summary = [
                f'Epoch: {self.current_epoch}',
                f'{iter_time:.2f} sec/step',
                f'LR: {lr:.2E}',
                f'Total Loss: {epoch_loss_mean:.4E}',
            ]
            for name, loss in epoch_individual_loss_means.items():
                summary.append(f'{name} Loss: {loss:.4E}')
            print('   '.join(summary), flush=True)

            # save epoch checkpoint
            if self.current_epoch % checkpoint_freq == 0 and self.current_epoch != self.initial_epoch:
                save_epoch()

            # epoch hook
            self.on_epoch_end(self.current_epoch)

            # break if min learning-rate reached
            lr = self.optimizer.param_groups[0]['lr']
            if self.min_lr is not None and lr < self.min_lr:
                print('Surpassed minimum learning rate - stopping training.')
                save_epoch()
                break

            # update global current epoch
            self.current_epoch += 1

        # clean up wandb stuff
        self.wandb_finish()

    def validate(self):
        """
        Runs the validation method for the trainer.

        Returns
        -------
        dict
            A dictionary of validation metrics.
        """
        return None

    def on_initial_epoch_set(self, epoch):
        """
        Optional hook that runs whenever the initial epoch is changed.

        Parameters
        ----------
        epoch : int
            The updated initial epoch number.
        """
        pass

    def on_epoch_end(self, epoch):
        """
        Optional hook that runs after every epoch is completed.

        Parameters
        ----------
        epoch : int
            The current epoch number.
        """
        pass

    def on_step_end(self, step):
        """
        Optional hook that runs after every step is completed per epoch.

        Parameters
        ----------
        epoch : int
            The current step number in the current epoch.
        """
        pass

    def on_loss_spike(self, sample, epoch):
        """
        Optional hook that runs whenever the loss spikes by a certain amount.
        This spiking threshold is computed as the 

        Parameters
        ----------
        sample : dict
            The data sample that caused the loss spike.
        epoch : int
            The current epoch number.
        """
        pass

    def on_validation_end(self, metrics, epoch):
        """
        Optional hook that runs after validation. This hook is useful for
        incrementing LR schedulers that depend on a particular validation metric.

        Parameters
        ----------
        metrics : dict
            The validation metrics dictionary returned by the validate function,
            if implemented.
        epoch : int
            The current epoch number.
        """
        pass

    def on_checkpoint_loaded(self, epoch):
        """
        Optional hook that runs after a model checkpoint is loaded.

        Parameters
        ----------
        epoch : int
            The epoch number of the loaded checkpoint.
        """
        pass


def command():
    """
    Command line utility for training a model. All parameters, including which model to train,
    are specified by the training config yaml file.
    """

    description = '''
    Train a deepsurfer module.

    This is a universal utility for training any module in the deepsurfer codebase.
    Specifications about which module to train, model parameters, optimization settings,
    data locations, W&B options, etc are all passed to the trainer via a yaml config
    file. To run model training:

    <DIM>ds train /path/to/output/dir

    It is expected that a config.yaml file lives in the output directory, though it can
    also be directly specified with the --config flag. Note that when this flag is used,
    the config is copied to the output directory and will overwrite any existing file.
    '''
    parser = system.parse.SubcommandParser(description=description)
    parser.add_argument('dir', help='Model output directory.')
    parser.add_argument('--config', metavar='file', help='Optional path to configuration file. Will use the '
                                                         'config.yaml file in output directory if not specified.')
    parser.add_argument('--load-checkpoint', type=int, help='Load checkpoint weights from epoch number. This will '
                                                            'also update the starting epoch number.')
    parser.add_argument('--load-weights', type=int, help='Load weights from file.')
    parser.add_argument('--no-load-optimizer', action='store_true', help='Do not load optimizer state from file.')
    parser.add_argument('--initial-epoch', metavar='file', help='Override the starting epoch number.')
    parser.add_argument('--lr', type=float, help='Overwrite the current learning rate.')
    parser.add_argument('--inspect', action='store_true', help='Visualize training data samples and exit.')
    args = parser.parse_args()
    outdir = args.dir

    # process and check the specified training configuration file
    if args.config:
        os.makedirs(outdir, exist_ok=True)
        system.warning(f'Writing over previously saved config in {outdir}.')
        shutil.copyfile(args.config, os.path.join(outdir, 'config.yaml'))
    else:
        if not os.path.isdir(outdir):
            system.fatal(f'Training directory {outdir} does not exist.')

    # load the specified training configuration file
    config = load_config(outdir)

    # infer the model trainer class from the config and initialize it
    trainer_class = system.import_member(config.opt('trainer'))
    trainer = trainer_class(outdir)

    # if the inspect flag was provided, just call the inspect method of the trainer
    # to visualize the sample, then exit without actually running anything
    if args.inspect:
        print('Inspecting data generation without actually training.')
        trainer.inspect()
        sys.exit()

    # sanity check on mutually exclusive loading options
    if args.load_checkpoint and args.load_weights:
        system.fatal('Can only specify one of --load-checkpoint or --load-weghts')

    # load any checkpoints if specified
    load_optimizer = not args.no_load_optimizer
    if args.load_checkpoint:
        trainer.load_checkpoint(args.load_checkpoint, load_optimizer=load_optimizer)
    elif args.load_weights:
        trainer.load_weights(args.load_weights, load_optimizer=load_optimizer)

    # overwrite learning rate
    if args.lr:
        trainer.optimizer.param_groups[0]['lr'] = args.lr

    # go ahead and train the damn thing
    trainer.train()
