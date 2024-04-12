# -*- coding: utf-8 -*-
from unittest.mock import patch

from chaosconsul.kv.actions import set_value_for_key


@patch('chaosconsul.kv.actions.client.kv.put', autospec=True)
def test_set_value_for_key(mock_kv_get):
    mock_kv_get.return_value = True
    assert set_value_for_key("foo", "bar") is True
