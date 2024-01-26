import torch


def soft_dice_loss(true, pred):
    """
    Computes the soft Dice loss between N true and predicted probabilistic labels.

    Parameters
    ----------
    true : Tensor
        A tensor of shape (B, N, ...) containing ground truth values.
    pred : Tensor
        A tensor of the same shape as `true` containing predicted values.

    Returns
    -------
    Tensor
        The soft Dice loss for each of the N labels.
    """
    ndims = len(list(pred.size())) - 2
    dims = list(range(2, ndims + 2))
    top = 2 * (true * pred).sum(dim=dims) + 1e-5
    bottom = (true + pred).sum(dim=dims) + 1e-5
    loss = 1 - (top / bottom)
    return loss
