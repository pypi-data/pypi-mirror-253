from colorama import Fore, Back, Style

def print_colored_background(color: str, message: str, style: str = "NORMAL"):
    return print_colored_backfore(color, "", message, style)

def print_colored_foreground(color: str, message: str, style: str = "NORMAL"):
    return print_colored_backfore("", color, message, style)

def print_colored_backfore(back: str, fore: str, message: str, style: str = "NORMAL"):
    target_color = getattr(Back, back.upper()) if back else ""
    target_fore = getattr(Fore, fore.upper()) if fore else ""
    target_style = getattr(Style, style.upper()) if style else ""
    print(f"{target_style}{target_color}{target_fore}{message}")
    print(Style.RESET_ALL, end=None)

def clear_screen(): print("\033[H\033[2J")
def debug(message: str): print_colored_foreground("megenta", f"[DEBUG-OMP] {message}", "bright")
def info(message: str): print_colored_foreground("blue", f"[INFO-OMP] {message}", "bright")
def error(message: str): print_colored_foreground("red", f"[ERROR-OMP] {message}", "bright")
def warning(message: str): print_colored_foreground("yellow", f"[WARN-OMP] {message}", "bright")