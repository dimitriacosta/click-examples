# pylint: disable=C0103
"""
Click callbacks and eager
"""
import click  # pylint: disable=E0401


def print_version(ctx, param, value):  # pylint: disable=W0613
    """Prints application's version"""
    if not value or ctx.resilient_parsing:
        return
    click.echo('Version 1.0')
    ctx.exit()


@click.command()
@click.option('-V', '--version', is_flag=True, callback=print_version,
              expose_value=False, is_eager=True)
#  @click.version_option(version='1.0', prog_name='click')
def hello():
    """Starts CLI application"""
    click.echo('Hello world!')


if __name__ == '__main__':
    hello()  # pylint: disable=E1120
