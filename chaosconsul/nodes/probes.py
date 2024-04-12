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
