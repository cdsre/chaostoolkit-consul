# -*- coding: utf-8 -*-
from consul import Consul

__all__ = ["upsert_value_for_key", "delete_key"]

client = Consul()


def upsert_value_for_key(
    key: str,
    value: str,
) -> bool:
    """
    Set a key/value pair in the Consul KV store.
    """
    return bool(client.kv.put(key, value))


def delete_key(key: str) -> bool:
    """
    Delete a key in the Consul KV store.
    """
    return bool(client.kv.delete(key))
