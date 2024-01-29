from rich import style
from rich.console import Console

styles = {
    'info': 'bold blue',
    'warn': 'italic yellow',
    'err': 'bold red',
    'serr': style.Style(color='#FA6E69', style='bold'),
    'note': 'dim italic',
    'worry': style.Style(color='#fdff8e'),
    'invalid': style.Style(color='#ff3d3d', style='underline italic'),
    'marked1': 'reverse yellow',
    'marked2': 'reverse green',
    'no_intr': 'strikethrough dim',
    'comment': style.Style(color='#186218', style='dim'),
}

def print(message, style):
    shell = Console()
    stil = styles.get(style, '')
    shell.print(f'[{stil}]{message}[/{stil}]')
