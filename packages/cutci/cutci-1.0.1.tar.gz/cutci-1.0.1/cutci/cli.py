"""Console script for cutci."""
import sys
import click


@click.command()
def main(args=None):
    """Console script for cutci."""
    click.echo("Cutci is a library to calculate Human Thermal Comfort Index (UTCI) "
               "by GPU-accelerated computing with CuPy."
               "cutci.cli.main")
    return 0


if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover
