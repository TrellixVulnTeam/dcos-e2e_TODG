"""
Clean all Docker artefacts from using the Docker backend.
"""

import click

from ._common import (
    NODE_TYPE_LABEL_KEY,
    NODE_TYPE_LOOPBACK_SIDECAR_LABEL_VALUE,
    docker_client,
)


@click.command('clean')
def clean():
    """
    Remove containers, volumes and networks created by this tool.
    """
    client = docker_client()

    filters = {
        'label': [
            '{key}={value}'.format(
                key=NODE_TYPE_LABEL_KEY,
                value=NODE_TYPE_LOOPBACK_SIDECAR_LABEL_VALUE,
            ),
        ],
    }
    loopback_sidecars = client.containers.list(filters=filters)
    for loopback_sidecar in loopback_sidecars:
        DockerLoopbackVolume.destroy(container=loopback_sidecar)

    node_filters = {'name': 'dcos-e2e'}

    node_containers = client.containers.list(filters=filters, all=True)

    for container in node_containers:
        container.stop()
        container.remove(v=True)

    network_filters = {'name': 'dcos-e2e'}
    networks = client.networks.list(filters=filters)
    for network in networks:
        network.remove()
