import click

@click.command()
@click.argument('src', nargs=-1)
@click.argument('dst', nargs=1)
def copy(src, dst):
    """Move file SRC to DST."""
    for fn in src:
        click.echo('Move %s to folder %s' % (fn, dst))

if __name__ == '__main__':
    copy()
