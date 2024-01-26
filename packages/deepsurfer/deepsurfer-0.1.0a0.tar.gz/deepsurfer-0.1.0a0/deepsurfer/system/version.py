from .. import __version__


class Version:

    def __init__(self, major, minor=None, patch=None):
        """
        Simple structure for representing and comparing release versions. This
        is a useful utility class for checking embedded version information in
        saved model files. This really only accounts for numerical versions with
        optional minor and patch information (ie. it will need to be updated to
        support version with string tags).
        """
        self.major = major
        self.minor = minor
        self.patch = patch

    def __repr__(self):
        strings = [str(self.major)]
        if self.minor is not None:
            strings.append(str(self.minor))
        if self.patch is not None:
            strings.append(str(self.patch))
        return '.'.join(strings)

    def make_tuple(self):
        a = int(self.major)
        b = 0 if self.minor is None else int(self.minor)
        c = 0 if self.patch is None else int(self.patch)
        return (a, b, c)

    def __lt__(self, vers):
        return self.make_tuple() < parse_version(vers).make_tuple()

    def __le__(self, vers):
        return self.make_tuple() <= parse_version(vers).make_tuple()

    def __gt__(self, vers):
        return self.make_tuple() > parse_version(vers).make_tuple()

    def __ge__(self, vers):
        return self.make_tuple() >= parse_version(vers).make_tuple()

    def __eq__(self, vers):
        return self.make_tuple() == parse_version(vers).make_tuple()

    def __ne__(self, vers):
        return self.make_tuple() != parse_version(vers).make_tuple()


def parse_version(version):
    """
    Parse a version string into a valid Version object, if possible.

    Parameters
    ----------
    version : str or Version
        Release version string.

    Returns
    -------
    Version
    """
    if isinstance(version, Version):
        return version
    items = [int(v) for v in version.split('.')]
    if len(items) > 3:
        raise ValueError(f'invalid version string \'{version}\'')
    return Version(*items)


def current_version():
    """
    The current deepsurfer version.

    Returns
    -------
    Version
    """
    return parse_version(__version__)
