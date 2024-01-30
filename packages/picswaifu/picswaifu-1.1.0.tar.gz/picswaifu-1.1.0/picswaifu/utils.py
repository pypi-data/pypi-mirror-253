from aiohttp import ClientSession
from enum import Enum, auto
import asyncio

class InvalidResponse(Exception):
    """Error class for invalid responses."""
    pass

class InvalidInput(Exception):
    """Error class for invalid inputs."""
    pass

class URL(str):
    """Representation class belongs to type of URL"""
    pass

class URLStack(list):
    """Representation class belongs to type of URL Stack"""
    pass

class ApiTypes(Enum):
    """API Types specified on docs"""
    SFW  = auto()
    NSFW = auto()

class SFWCats(Enum):
    """Category Options Enumeration Class for API Type SFW"""
    WAIFU = auto()
    NEKO = auto()
    SHINOBU = auto()
    MEGUMIN = auto()
    BULLY = auto()
    CUDDLE = auto()
    CRY = auto()
    HUG = auto()
    AWO0 = auto()
    KISS = auto()
    LICK = auto()
    PAT = auto()
    SMUG = auto()
    BONK = auto()
    YEET = auto()
    BLUSH = auto()
    SMILE = auto()
    WAVE = auto()
    HIGHFIVE = auto()
    HANDHOLD = auto()
    NOM = auto()
    BITE = auto()
    GLOMP = auto()
    SLAP = auto()
    KILL = auto()
    KICK = auto()
    HAPPY = auto()
    WINK = auto()
    POKE = auto()
    DANCE = auto()
    CRINGE = auto()

class NSFWCats(Enum):
    """Category Options Enumeration Class for API Type SFW"""
    WAIFU = auto()
    NEKO = auto()
    TRAP = auto()
    BLOWJOB = auto()

class TypesAndCats:
    """Category Classes for API Types"""
    SFW = {
        "category_class": SFWCats
    }

    NSFW = {
        "category_class": NSFWCats
    }

class Waifu(object):
    """
    :arg: __type: ApiTypes = defaulted [ApiTypes.SFW]
    :arg: __category: ApiTypes = defaulted [SFWCats.NEKO]
    :arg: __multi: bool = defaulted [True]
    
    :function: get()
        Returns URL or URLStack
    :function: get_nsfw (__category: NSFWCats, __multi: bool = False)
        Returns URL or URLStack
    :function: get_sfw  (__category: SFWCats, __multi: bool = False)
        Returns URL or URLStack
    """
    SINGLE_RESP_URL = "https://api.waifu.pics/%s/%s"
    MULTI_RESP_URL  = "https://api.waifu.pics/many/%s/%s"
    def __new__(cls, __type: ApiTypes = ApiTypes.SFW, __category: SFWCats | NSFWCats = SFWCats.NEKO, __multi: bool = False):
        cls.files = []
        cls.multi = __multi
        cls.type = __type
        cls.category = __category
        cls.category_class = cls.category.__class__
        return super().__new__(cls)
    def __init__(self, *args, **kwargs) -> None:
        pass
        if self.type == ApiTypes.SFW:
            assert (TypesAndCats.SFW.get("category_class") == self.category_class), \
                "Wrong category for API Type SFW"
        elif self.type == ApiTypes.NSFW:
            assert (TypesAndCats.NSFW.get("category_class") == self.category_class), \
                "Wrong category for API Type NSFW"
        else:
            raise ValueError("Unknown API Type!")
        

    async def get_sfw(self, category: SFWCats = None, multi: bool = None) -> URL | URLStack:
        assert (isinstance(category, SFWCats)), "Category must be intantiated from SFWCats"
        url = self.SINGLE_RESP_URL if not multi else self.MULTI_RESP_URL
        url = url % ("sfw", category.name.lower())
        async with ClientSession(headers={"User-Agent": "Mozilla/5.0 (compatible; MSIE 10.0; Windows; U; Windows NT 10.4; Win64; x64; en-US Trident/6.0)"}) as client:
            if multi:
                resp = await client.post(url, json={"exclude": []})
                data = await resp.json()
                if data.get("files"):
                    self.files = data["files"]
                    return self.files
                else:
                    raise InvalidResponse("Response was invalid.")
            else:
                resp = await client.get(url)
                data = await resp.json()
                file = data["url"]
                return file

    async def get_nsfw(self, category: NSFWCats = None, multi: bool = None) -> URL | URLStack:
        assert (isinstance(category, NSFWCats)), "Category must be intantiated from NSFWCats"
        url = self.SINGLE_RESP_URL if not multi else self.MULTI_RESP_URL
        url = url % ("nsfw", category.name.lower())
        async with ClientSession(headers={"User-Agent": "Mozilla/5.0 (compatible; MSIE 10.0; Windows; U; Windows NT 10.4; Win64; x64; en-US Trident/6.0)"}) as client:
            if multi:
                resp = await client.post(url, json={"exclude": []})
                data = await resp.json()
                if data.get("files"):
                    self.files = data["files"]
                    return self.files
                else:
                    raise InvalidResponse("Response was invalid.")
            else:
                resp = await client.get(url)
                data = await resp.json()
                file = data["url"]
                return file
    async def get(self) -> URL | URLStack:
        if self.type == ApiTypes.SFW:
            return await self.get_sfw(self.category, multi=self.multi)
        elif self.type == ApiTypes.NSFW:
            return await self.get_nsfw(self.category, multi=self.multi)
        else:
            raise InvalidInput("You have to configure instance to get response from API. Call help(NekoNeko) to get information.")