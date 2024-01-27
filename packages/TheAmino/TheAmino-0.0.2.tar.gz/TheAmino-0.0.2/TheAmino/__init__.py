from json import loads
from requests import get

__title__ = 'TheAmino'
__author__ = 'Codex'
__license__ = 'MIT'
__copyright__ = 'Copyright 2023-2024 Codex'
__version__ = '0.0.2'


from .TheAmino import *

__newest__ = loads(get("https://pypi.python.org/pypi/TheAmino/json").text)["info"]["version"]

if __version__ != __newest__:
    print(f"New version of {__title__} available: {__newest__} (Using {__version__})")
else:
    print(f"version : {__version__}")