# -*- coding: utf-8 -*-
from chaoslib.types import Configuration, Secrets
from chaoslib.exceptions import FailedActivity
from chaoslib.types import Configuration, Secrets
from consul import Consul

__all__ = ["empty_probe"]


def empty_probe(
        configuration: Configuration = None, secrets: Secrets = None
) -> bool:
    return True


def consul_get_service_status(service_name: str) -> bool:
    """
    Get the status of a service in Consul.

    The status is considered OK if the service is in the passing state.

    Parameters
    ----------
    service_name : str
        The name of the service to check the status of

    Returns
    -------
    bool
        True if the service is passing, False otherwise
    """

    configuration = Configuration.load()
    secrets = Secrets.load()

    client = Consul(
        host=secrets["consul_host"],
        port=secrets.get("consul_port", 8500),
        token=secrets.get("consul_token", None),
        scheme=secrets.get("consul_scheme", "http")
    )

    index, nodes = client.health.service(service_name)
    passing = [node for node in nodes if node["Status"] == "passing"]

    if not passing:
        raise FailedActivity(
            "Service '{s}' is not passing".format(s=service_name))

    return True
