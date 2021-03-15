import click
import sys

@click.command()
@click.option('--shout', is_flag=True)
def info(shout):
    rv = sys.platform
    if shout:
        rv = rv.upper() + '!!!!!'
    click.echo(rv)

if __name__ == '__main__':
    info()
