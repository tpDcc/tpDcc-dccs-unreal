#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""
Module that contains tests for tpDcc.dccs.unreal
"""

import pytest

from tpDcc.dccs.unreal import __version__


def test_version():
    assert __version__.get_version()
