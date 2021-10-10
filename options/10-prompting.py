# pylint: disable=C0103
"""
Click prompting
"""
import click  # pylint: disable=E0401


@click.command()
@click.option('--name', prompt="Your name please")
def hello(name):
    """Starts CLI application"""
    click.echo(f"Hello {name}")


if __name__ == '__main__':
    hello()  # pylint: disable=E1120
