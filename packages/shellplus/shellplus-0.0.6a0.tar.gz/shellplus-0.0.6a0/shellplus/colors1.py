from rich import color
from rich.console import Console

colors = {
    'forest': color('#0e3a0e'),

    'hot pink': color('#ff0055'),

    'sky blue': color('#0face9'),

    'chili': color('#df3b28'),
    'salmon': color('#df3b28'),

    'gum pink': color('#f8369d'),
    'bubblegum': color('#f8369d'),

    'green apple': color('#b3e52a'),
    'sour apple': color('#b3e52a'),
    'greenyellow': color('#b3e52a'),

    'diva': color('#ccace3'),

    'navy': color('#020563'),

    'dark teal': color('#55aa88'),
    'dteal': color('#55aa88')
}

def print(message, color):
    shell = Console()
    stil = colors.get(color, '')
    shell.print(f'[{stil}]{message}[/{stil}]')