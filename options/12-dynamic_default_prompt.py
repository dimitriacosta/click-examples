import click
import os

@click.command()
@click.option('--username', prompt=True,
              default=lambda: os.environ.get('USER', ''),
              show_default='Current user')
def hello(username):
    print("Hello", username)

if __name__ == '__main__':
    hello()
