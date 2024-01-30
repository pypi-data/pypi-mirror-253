from .utils import Waifu
from .errors import InvalidInput, InvalidResponse
from .api_types import TypesAndCats, ApiTypes, NSFWCats, SFWCats, URL, URLStack

"""
Waifu API Wrapper for Python.
Visit for more: https://waifu.pics/docs
Developer: https://github.com/fswair
"""

__all__ = [
    "Waifu",
    "InvalidInput",
    "InvalidResponse",
    "TypesAndCats",
    "ApiTypes",
    "NSFWCats",
    "SFWCats",
    "URL",
    "URLStack"
]

__version__ = "1.0.0"

__author__ = "fswair"

__license__ = "GPLv3"

__waifu__ = Waifu()

__waifu__.__version__ = __version__