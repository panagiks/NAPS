"""Console script for naps."""
import anyio
import sys
import click
import ipaddress

from naps import schedule


@click.command()
@click.argument("network", type=str)
@click.argument("port_range_start", type=int)
@click.argument("port_range_end", type=int)
def main(**kwargs):
    """Console script for naps."""
    network = ipaddress.ip_network(kwargs["network"])
    anyio.run(schedule, network, kwargs["port_range_start"], kwargs["port_range_end"] + 1)
    return 0


if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover
