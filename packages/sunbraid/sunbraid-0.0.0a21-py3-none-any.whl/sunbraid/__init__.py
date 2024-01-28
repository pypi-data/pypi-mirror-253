import pkg_resources
from . import inline, data
from .head import render

__version__ = pkg_resources.get_distribution('sunbraid').version