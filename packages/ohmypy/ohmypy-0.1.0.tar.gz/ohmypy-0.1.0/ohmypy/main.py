import os
import sys

from colorama import init, deinit
from ohmypy.settings import read_ohmypyRC

orig_ps1: object = ">>> "
orig_ps2: object = "... "

read_ohmypyRC()

from ohmypy.settings import *
from ohmypy.printtext import *
from ohmypy.prompts import *

ps1 = PromptString(PS1) if PS1 else orig_ps1
ps2 = PromptString(PS2) if PS2 else orig_ps2

def initialize():
    """
    Initialize the toolkit.
    """
    init(True)
    sys.path.append(os.path.dirname(__file__) + "/..")
    sys.path.append(os.path.expanduser("~/.oh-my-py"))

    sys.ps1 = ps1
    sys.ps2 = ps2

    if ENV:
        for key in ENV: os.environ[key] = str(ENV[key])
    
    if PREEXE:
        for path in PREEXE: exec(open(path, "r").read())

def deinitialize():
    """
    Run this on ohmypy/Python exit.
    """
    sys.ps1 = orig_ps1
    sys.ps2 = orig_ps2
    deinit()

if ("PYTHONSTARTUP" in os.environ) and (os.environ["PYTHONSTARTUP"] != __file__):
    warning("Not running as a Python startup script")

initialize()