# -*- coding: utf-8 -*-
from consul import Consul

__all__ = ["set_value_for_key"]

client = Consul()


def set_value_for_key(
    key: str,
    value: str,
) -> bool:
    """
    Set a key/value pair in the Consul KV store.
    """
    return bool(client.kv.put(key, value))
