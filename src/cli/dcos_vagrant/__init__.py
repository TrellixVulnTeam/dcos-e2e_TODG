"""
A CLI for controlling DC/OS clusters on Vagrant.
"""

import click

import dcos_e2e
from cli.common.commands import download_artifact

from .commands.create import create
from .commands.destroy import destroy, destroy_list
from .commands.doctor import doctor
from .commands.inspect_cluster import inspect_cluster
from .commands.list_clusters import list_clusters
from .commands.run_command import run
from .commands.sync import sync_code
from .commands.wait import wait
from .commands.web import web


@click.group(name='dcos-vagrant')
# We set the ``version`` parameter because in PyInstaller binaries,
# ``pkg_resources`` is not available.
#
# Click uses ``pkg_resources`` to determine the version if it is not given.
@click.version_option(version=dcos_e2e.__version__)
def dcos_vagrant() -> None:
    """
    Manage DC/OS clusters on Vagrant.
    """


dcos_vagrant.add_command(create)
dcos_vagrant.add_command(destroy)
dcos_vagrant.add_command(destroy_list)
dcos_vagrant.add_command(doctor)
dcos_vagrant.add_command(download_artifact)
dcos_vagrant.add_command(inspect_cluster)
dcos_vagrant.add_command(list_clusters)
dcos_vagrant.add_command(run)
dcos_vagrant.add_command(sync_code)
dcos_vagrant.add_command(wait)
dcos_vagrant.add_command(web)
