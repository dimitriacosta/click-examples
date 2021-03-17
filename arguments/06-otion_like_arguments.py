import click

@click.command()
@click.argument('files', nargs=-1, type=click.Path())
def touch(files):
    """Print all FILES names."""
    for filename in files:
        click.echo(filename)

if __name__ == '__main__':
    touch()
