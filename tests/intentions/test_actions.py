# -*- coding: utf-8 -*-

from chaosconsul.intentions.actions import empty_action


def test_empty_action():
    assert empty_action() is None
