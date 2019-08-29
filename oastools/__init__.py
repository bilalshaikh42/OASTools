from .validate import *
from .parse import *
from .utils import *
import pkg_resources

# read version
with open(pkg_resources.resource_filename('oastools', 'VERSION'), 'r') as file:
    __version__ = file.read().strip()

#import subpackages
