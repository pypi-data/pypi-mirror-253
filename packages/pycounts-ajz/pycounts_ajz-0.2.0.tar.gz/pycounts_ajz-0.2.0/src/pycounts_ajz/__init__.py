# # read version from installed package
# from importlib.metadata import version
# __version__ = version("pycounts")


# read version from installed package
from importlib.metadata import version
__version__ = version(__name__)

# populate package namespace
from pycounts_ajz.pycounts import count_words
from pycounts_ajz.plotting import plot_words