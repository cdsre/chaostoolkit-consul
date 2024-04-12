# -*- coding: utf-8 -*-
from chaoslib.exceptions import FailedActivity
from chaoslib.types import Configuration, Secrets
from consul import Consul

__all__ = ["key_exists", "get_value_for_key"]

client = Consul()


def key_exists(key: str) -> bool:
    """
    Check if a key exists in the Consul KV store.
    """

    index, data = client.kv.get(key)
    return data is not None


def get_value_for_key(key: str) -> str:
    """
    Get the value for a key in the Consul KV store.
    """

    index, data = client.kv.get(key)
    if data is None:
        raise FailedActivity(f"Key '{key}' does not exist in the Consul KV store")
    return data["Value"].decode("utf-8")
