# -*- coding: utf-8 -*-
from unittest.mock import patch

from chaosconsul.kv.actions import upsert_value_for_key, delete_key


@patch('chaosconsul.kv.actions.client.kv.put', autospec=True)
def test_set_value_for_key(mock_kv_get):
    mock_kv_get.return_value = True
    assert upsert_value_for_key("foo", "bar") is True


@patch('chaosconsul.kv.actions.client.kv.delete', autospec=True)
def test_delete_key(mock_kv_delete):
    """
    Delete a key in the Consul KV store.
    """
    mock_kv_delete.return_value = True
    return delete_key("foo")
