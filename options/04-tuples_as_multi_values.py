import click

@click.command()
@click.option('--item', type=(str, int))
def putitem(item):
    click.echo('name=%s id=%d' % item)

if __name__ == '__main__':
    putitem()
