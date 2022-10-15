def print_colored(txt,color='blue',typeface='n'):
    color_codes = {
        'none' : '',
        'header' : '\033[95m',
        'blue' : '\033[94m',
        'cyan' : '\033[96m',
        'green' : '\033[92m',
        'warning' : '\033[93m',
        'fail' : '\033[91m',
        'red' : '\033[91m',
    }
    typefaces = {
        'n' : '',
        'b' : '\033[1m',
        'u' : '\033[4m'
    }
    tf = typefaces[typeface]
    endc = '\033[0m'
    col = color_codes[color]
    print(f'{col}{tf}{txt}{endc}')

