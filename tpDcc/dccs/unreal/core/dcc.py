#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""
Module that contains DCC functionality for standalone applications
"""

from __future__ import print_function, division, absolute_import

from Qt.QtWidgets import *

import tpDcc
from tpDcc import register
from tpDcc.abstract import dcc as abstract_dcc

import unreal
from tpDcc.dccs.unreal.core import helpers


class UnrealDcc(abstract_dcc.AbstractDCC, object):

    @staticmethod
    def get_name():
        """
        Returns the name of the DCC
        :return: str
        """

        return tpDcc.Dccs.Unreal

    @staticmethod
    def get_extensions():
        """
        Returns supported extensions of the DCC
        :return: list(str)
        """

        return ['.uproject']

    @staticmethod
    def get_dpi(value=1):
        """
        Returns current DPI used by DCC
        :param value: float
        :return: float
        """

        return 1.0

    @staticmethod
    def get_dpi_scale(value):
        """
        Returns current DPI scale used by DCC
        :return: float
        """

        return 1.0

    @staticmethod
    def get_version():
        """
        Returns version of the DCC
        :return: int
        """

        return helpers.get_unreal_version()


    @staticmethod
    def get_version_name():
        """
        Returns version of the DCC
        :return: str
        """

        return helpers.get_unreal_version_name()

    @staticmethod
    def is_batch():
        """
        Returns whether DCC is being executed in batch mode or not
        :return: bool
        """

        return False

    @staticmethod
    def enable_component_selection():
        """
        Enables DCC component selection mode
        """

        pass

    @staticmethod
    def get_main_window():
        """
        Returns Qt object that references to the main DCC window
        :return:
        """

        return None

    @staticmethod
    def get_main_menubar():
        """
        Returns Qt object that references to the main DCC menubar
        :return:
        """

        return None

    @staticmethod
    def confirm_dialog(title, message, button=None, cancel_button=None, default_button=None, dismiss_string=None):
        """
        Shows DCC confirm dialog
        :param title:
        :param message:
        :param button:
        :param cancel_button:
        :param default_button:
        :param dismiss_string:
        :return:
        """

        from tpDcc.libs.qt.widgets import messagebox

        buttons = button or QDialogButtonBox.Yes | QDialogButtonBox.No
        if cancel_button:
            buttons = buttons | QDialogButtonBox.Cancel

        return messagebox.MessageBox.question(None, title=title, text=message, buttons=buttons)

    @staticmethod
    def warning(message):
        """
        Prints a warning message
        :param message: str
        :return:
        """

        unreal.log_warning(message)

    @staticmethod
    def error(message):
        """
        Prints a error message
        :param message: str
        :return:
        """

        unreal.log_error(message)

    @staticmethod
    def is_window_floating(window_name):
        """
        Returns whether or not DCC window is floating
        :param window_name: str
        :return: bool
        """

        return False


register.register_class('Dcc', UnrealDcc)
