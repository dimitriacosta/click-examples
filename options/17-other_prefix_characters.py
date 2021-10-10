# pylint: disable=C0103
"""
Click other prefix characters
"""
import click  # pylint: disable=E0401


@click.command()
@click.option('+w/-w')
def chmod(w):
    """Starts CLI application"""
    click.echo(f"writable={w}")


if __name__ == '__main__':
    chmod()  # pylint: disable=E1120
