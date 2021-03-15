import click

def print_version(ctx, param, value):
    if not value or ctx.resilient_parsing:
        return
    click.echo('Version 1.0')
    ctx.exit()

@click.command()
@click.option('-V', '--version', is_flag=True, callback=print_version,
              expose_value=False, is_eager=True)
#  @click.version_option(version='1.0', prog_name='click')
def hello():
    click.echo('Hello world!')

if __name__ == '__main__':
    hello()
