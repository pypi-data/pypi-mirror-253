import importlib.metadata as metadata
from datetime import date

# load package info
__pkg_name__ = metadata.metadata("taurex_emcee")["Name"]
__version__ = metadata.metadata("taurex_emcee")["version"]
__author__ = metadata.metadata("taurex_emcee")["Author"]
__license__ = metadata.metadata("taurex_emcee")["license"]
__copyright__ = "2021-{:d}, {}".format(date.today().year, __author__)
__summary__ = metadata.metadata("taurex_emcee")["Summary"]

from .emcee_optimizer import EmceeSampler
