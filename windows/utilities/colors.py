def colors():
    '''Function give some of Color in Terminal'''
    from colorama import Fore, Style
    global red,green, white, yellow, reset_color
    red = Fore.RED + Style.BRIGHT 
    green = Fore.GREEN + Style.BRIGHT
    white = Fore.WHITE + Style.BRIGHT
    yellow = Fore.YELLOW + Style.BRIGHT
    reset_color = Style.RESET_ALL
colors()
