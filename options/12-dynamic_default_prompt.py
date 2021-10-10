# pylint: disable=C0103
"""
Click dynamic default prompt
"""
import os
import click  # pylint: disable=E0401


@click.command()
@click.option('--username', prompt=True,
              default=lambda: os.environ.get('USER', ''),
              show_default='Current user')
def hello(username):
    """Starts CLI application"""
    print("Hello", username)


if __name__ == '__main__':
    hello()  # pylint: disable=E1120
