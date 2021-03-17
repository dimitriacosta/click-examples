import click

@click.command()
@click.argument('src', envvar='SRC', type=click.File('r'))
def echo(src):
    """Print the value of the SRC environment variable."""
    click.echo(src.read())


if __name__ == '__main__':
    echo()
