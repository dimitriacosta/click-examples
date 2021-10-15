# pylint: disable=C0103
"""
Click file arguments
"""
import click  # pylint: disable=E0401


@click.command()
@click.argument('input_', type=click.File('rb'))
@click.argument('output_', type=click.File('wb'))
def inout(input_, output_):
    """Copy contents of INPUT to OUTPUT."""
    while True:
        chunk = input_.read(1024)
        if not chunk:
            break
        output_.write(chunk)


if __name__ == '__main__':
    inout()  # pylint: disable=E1120
