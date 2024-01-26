import subprocess

import click

from . import p4, tools, ue
from .p4 import p4 as p4_grp
from .py import python as python_grp
from .ue import ue as ue_grp


@click.group()
@click.option("--verbose", "-v", is_flag=True, help="Enables verbose mode.")
@click.pass_context
def cli(ctx, verbose):
    ctx.ensure_object(dict)
    ctx.obj["verbose"] = verbose


@cli.command()
def initial_setup():
    print("welcome to initial_setup_paxo")


@cli.command()
def self_update():
    """Update paxo."""
    # pipx is a bat file, so we need to run it in a shell
    subprocess.run("pipx upgrade mainframe-paxo", shell=True, check=True)
    print("paxo updated, now running post_update actions...")
    subprocess.run("paxo post-update", shell=True, check=True)


@cli.command()
def post_update():
    """Run actions to refresh settings after updating paxo."""
    print("welcome to post_update_paxo")


@cli.group()
def location():
    """work with current location"""
    pass


@location.command()
@click.option("--verbose", "-v", is_flag=True, help="Enables verbose mode.")
def list(verbose):
    """list the available locations."""
    print("Available locations:")
    if not verbose:
        for location in tools.locations:
            print(f" - {location}")
    else:
        for location, info in tools.locations.items():
            print(f" - {location}")
            for key, value in info.items():
                print(f"   - {key}: {value}")


@location.command("set")
@click.option(
    "--location",
    prompt="Location",
    type=click.Choice(tools.locations.keys()),
    default=None,
)
def location_set(location):
    """set the location."""
    p4.set_location(location)
    ue.set_location(location)
    tools.location_set(location)
    print(f"Location set to {location}")


@location.command("show")
@click.pass_context
def location_show(ctx):
    """show the current location."""
    loc = tools.location_get()
    if ctx.obj["verbose"]:
        print(f"Current location: {loc}")
        for key, value in tools.locations[loc].items():
            print(f" - {key}: {value}")
    else:
        print(loc)


cli.add_command(p4_grp)
cli.add_command(ue_grp)
cli.add_command(python_grp)

paxo = cli
if __name__ == "__main__":
    cli(obj={})
