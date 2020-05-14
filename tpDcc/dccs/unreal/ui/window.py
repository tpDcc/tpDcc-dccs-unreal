#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""
Module that contains functionality for Unreal windows
"""

from __future__ import print_function, division, absolute_import

import unreal

from tpDcc import register
from tpDcc.libs.qt.core import window as core_window


class UnrealWindow(core_window.MainWindow, object):
    def __init__(self, *args, **kwargs):

        parent = kwargs.get('parent', None)

        super(UnrealWindow, self).__init__(*args, **kwargs)

        if not parent:
            unreal.parent_external_window_to_slate(self.winId())


register.register_class('Window', UnrealWindow)
register.register_class('DockWindow', UnrealWindow)
register.register_class('SubWindow', UnrealWindow)
