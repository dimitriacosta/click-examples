import click

#  def abort_if_false(ctx, param, value):
#      if not value:
#          ctx.abort()

@click.command()
#  @click.option('--yes', is_flag=True, callback=abort_if_false,
#                expose_value=False,
#                prompt='Are you sure you want to drop the database?')
@click.confirmation_option(prompt='Are you sure you want to drop the database?')
def dropdb():
    click.echo('Dropped all tables')

if __name__ == '__main__':
    dropdb()
