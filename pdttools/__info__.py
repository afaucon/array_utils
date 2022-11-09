from importlib.metadata import metadata


__package_name__ = "pdttools"

md = metadata(__package_name__)

__description__ = md["Summary"]
__version__ = md["Summary"]
__author__ = md["Author"]
__author_email__ = md["Author-email"]
__license__ = md["License"]

del md
