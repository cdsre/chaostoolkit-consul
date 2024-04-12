# -*- coding: utf-8 -*-
from unittest.mock import patch
from chaosconsul.kv.probes import key_exists, get_value_for_key
from chaoslib.exceptions import FailedActivity
import pytest


@patch('chaosconsul.kv.probes.client.kv.get', autospec=True)
def test_kv_exists_true(mock_kv_get):
    key = "foo"
    mock_kv_get.return_value = (0, {"key": key})
    assert key_exists(key) is True


@patch('chaosconsul.kv.probes.client.kv.get', autospec=True)
def test_kv_exists_false(mock_kv_get):
    key = "foo"
    mock_kv_get.return_value = (0, None)
    assert key_exists(key) is False


@patch('chaosconsul.kv.probes.client.kv.get', autospec=True)
def test_get_value_for_key(mock_kv_get):
    key = "foo"
    value = "bar"
    mock_kv_get.return_value = (0, {"key": key, "Value": value.encode()})
    assert get_value_for_key(key) == value


@patch('chaosconsul.kv.probes.client.kv.get', autospec=True)
def test_get_value_for_key_failed(mock_kv_get):
    key = "foo"
    mock_kv_get.return_value = (0, None)
    with pytest.raises(FailedActivity) as f:
        get_value_for_key(key)
