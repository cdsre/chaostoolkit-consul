# -*- coding: utf-8 -*-

from chaosconsul.services.probes import empty_probe


def test_empty_probe():
    assert empty_probe() is True
