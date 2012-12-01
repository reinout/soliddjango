# Import a whole package or module.
import os
import os.path
# Import something specific from a module.
from os.path import exists


# Available because of import 'os' or 'os.path':
os.path.exists('.')
# Available because of directly importing it:
exists('.')
