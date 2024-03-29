# pylint: disable=C0103
"""
Click values from environment variables
"""
import click  # pylint: disable=E0401


#  @click.command()
#  @click.option('--username')
#  def greet(username):
#      click.echo('Hello %s!' % username)

#  if __name__ == '__main__':
#      greet(auto_envvar_prefix='GREETER')

#  @click.group()
#  @click.option('--debug/--no-debug')
#  def cli(debug):
#      click.echo('Debug mode is %s' % ('on' if debug else 'off'))

#  @cli.command()
#  @click.option('--username')
#  def greet(username):
#      click.echo(f"Hello {username}")

@click.command()
@click.option('--username', envvar='USERNAME')
def greet(username):
    """Starts CLI application"""
    click.echo(f"Hello {username}!")


if __name__ == '__main__':
    greet()  # pylint: disable=E1120
