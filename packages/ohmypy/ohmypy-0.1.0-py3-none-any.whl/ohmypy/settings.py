import ast
import os
import re

# Main settings path
MAINCFG = os.path.expanduser("~/.ohmypy")

# Settings

## Python-related
ENV: dict[str] = {} # Environment variables
PS1: str = "" # Main prompt (Python's default is >>> + a space)
PS2: str = "" # Used for function/loop indention (Python's default is ... + a space)
PREEXE: list[str] = [] # Add even more startup scripts, not only this ohmypy

## Ohmypy settings
AUTO_UPDATE: bool = True
UPDATE_DELAY: str = "3 days"
ACCEPT_RISKS: bool = False
ADD_COLORS: bool
ASK_ONCE_FRIK: bool = False

try:
    import pretty_errors
except:
    PRETTY_EXP = False
else:
    PRETTY_EXP = True
    del pretty_errors

try:
    import colorama
except:
    ADD_COLORS = False
else:
    ADD_COLORS = True
    del colorama

PLUGINS_TO_LOAD: list[str] = [] # TODO: Plugins;)

# Basic usage for ya:D
BASIC = \
    "; Welcome to Ohmypy!\n" \
    "; Just like projects like Ohmybash, Ohmyzsh or Ohmyposh, Ohmypy customizes Python interpreter/shell.\n" \
    "; This will be ran before Python actually setup (by running this as a Python Startup file)\n\n" \
    "; Basic options:\n" \
    "; ENV: Environment variables. Set using os.environ.\n" \
    "; PS1: Edit Python's prompt\n" \
    "; PS2: Edit Python's indentation prompt\n" \
    "; PREEXE: Execute more startup scripts (absolute path required)\n" \
    "; PRESET: Modify variables.\n\n" \
    "; As you can see here lines with ; prefix are comments.\n" \
    "; Every objects else (settings etc) follow the Python's corresponding object type.\n" \
    "; For example: ADD_COLORS is a boolean so it accepts True or False values.\n" \
    "; ENV is a dictionary, so its value can be {'PATH': '/some/path/here'}.\n" \
    "; No multiple lines support.\n"

def read_ohmypyRC():
    """
    Reads ~/.ohmypy and execute needed codes.
    """
    global ENV, PS1, PS2, PREEXE, ACCEPT_RISKS, ADD_COLORS, PLUGINS_TO_LOAD

    def prefixremove(line: str) -> tuple[str, str]:
        match = re.match(r"([A-Z]+)([0-9])*(\s)*(=)\s*", line)
        return line.removeprefix(match[0]), match[0]

    if not os.path.isfile(MAINCFG):
        print("Ohmypy source file is not created. "
              "Will create a file with basic infomations inside instead.")
        open(MAINCFG, "w").write(BASIC)
    
    else:
        content = open(MAINCFG, "r").read()
        for line in content.splitlines():
            if line.startswith(";") or not line: # Comments / blank lines
                continue
            else:
                line_new, var = prefixremove(line)
                var = var.replace("=", "").replace(" ", "")
                if var.isupper():
                    globals()[var] = ast.literal_eval(line_new)