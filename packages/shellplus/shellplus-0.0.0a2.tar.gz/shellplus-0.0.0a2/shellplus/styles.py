from rich import style
from rich.console import Console

styles = {
    'info': 'bold blue',
    'warn': 'italic yellow',
    'err': 'bold red',
    'serr': style(color='#FA6E69', style='bold'),
    'note': 'dim italic',
    'worry': style(color='#fdff8e'),
    'invalid': style(color='#ff3d3d', style='underline italic'),
    'marked1': 'reverse yellow',
    'marked2': 'reverse green',
    'no_intr': 'strikethrough dim',
    'comment': style(color='#186218', style='dim'),
}
