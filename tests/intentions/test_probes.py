# -*- coding: utf-8 -*-

from chaosconsul.intentions.probes import empty_probe


def test_empty_probe():
    assert empty_probe() is True
