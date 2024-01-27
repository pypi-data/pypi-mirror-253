import builtins
import getpass
import os
import platform
import sys
import time

from ohmypy.printtext import *
from ohmypy.settings import ADD_COLORS
from colorama import Fore, Back, Style

# Colors
Colors: dict[str, str] = {}

for attr in dir(Back):
    if attr.isupper():
        Colors[attr + "_BACK"] = getattr(Back, attr)

for attr in dir(Fore):
    if attr.isupper():
        Colors[attr + "_FORE"] = getattr(Fore, attr)

for attr in dir(Style):
    if attr.isupper():
        Colors[attr + "_STYLE"] = getattr(Style, attr)

# More things
Attrs: dict[str] = {
    "USERNAME": getpass.getuser,
    "HOSTNAME": platform.node,
    "ASCTIME": time.asctime,
    "CURRDIR": os.getcwd,
    "OS": platform.platform,
    "ARCH": platform.architecture,
    "PYVER": platform.python_version
}

class PromptString:
    """
    General class for prompt strings on Python.
    """

    target: str

    def __init__(this, what_to_use: str): this.target = what_to_use
    def __str__(this):
        newdict = {}
        for key in Attrs:
            newdict[key] = Attrs[key]()
        if ADD_COLORS: return this.target % {**newdict, **Colors}
        else: return this.target % newdict