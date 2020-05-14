#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""
Module that contains functionality for Unreal dialogs
"""

from __future__ import print_function, division, absolute_import

import os

from tpDcc import register
from tpDcc.libs.python import path as path_utils
from tpDcc.libs.qt.core import dialog as core_dialog


class UnrealDialog(core_dialog.Dialog, object):
    def __init__(self, name='UnrealDialog', parent=None, **kwargs):
        super(UnrealDialog, self).__init__(name=name, parent=parent, **kwargs)


class UnrealOpenFileDialog(core_dialog.OpenFileDialog, object):
    def __init__(self, name='UnrealOpenFileDialog', parent=None, **kwargs):
        super(UnrealOpenFileDialog, self).__init__(name=name, parent=parent, **kwargs)


class UnrealSaveFileDialog(core_dialog.SaveFileDialog, object):
    def __init__(self, name='UnrealSaveFileDialog', parent=None, **kwargs):
        super(UnrealSaveFileDialog, self).__init__(name=name, parent=parent, **kwargs)


class UnrealSelectFolderDialog(core_dialog.SelectFolderDialog, object):
    def __init__(self, name='UnrealSelectFolderDialog', parent=None, **kwargs):
        super(UnrealSelectFolderDialog, self).__init__(name=name, parent=parent, **kwargs)


class UnrealNativeDialog(core_dialog.NativeDialog, object):

    @staticmethod
    def open_file(title='Open File', start_directory=None, filters=None):
        """
        Function that shows open file Max native dialog
        :param title: str
        :param start_directory: str
        :param filters: str
        :return: str
        """

        start_directory = start_directory if start_directory else os.path.expanduser('~')
        clean_path = path_utils.clean_path(start_directory)
        # file_path = directory.select_file_dialog(title=title, start_directory=clean_path, pattern=filters)

        return file_path

    @staticmethod
    def save_file(title='Save File', start_directory=None, filters=None):
        """
        Function that shows save file Max native dialog
        :param title: str
        :param start_directory: str
        :param filters: str
        :return: str
        """

        start_directory = start_directory if start_directory else os.path.expanduser('~')
        clean_path = path_utils.clean_path(start_directory)
        # file_path = directory.save_file_dialog(title=title, start_directory=clean_path, pattern=filters)

        return file_path

    @staticmethod
    def select_folder(title='Select Folder', start_directory=None):
        """
        Function that shows select folder Maya dialog
        :param title: str
        :param start_directory: str
        :return: str
        """

        start_directory = start_directory if start_directory else os.path.expanduser('~')
        clean_path = path_utils.clean_path(start_directory)
        # folder_path = directory.select_folder_dialog(title=title, start_directory=clean_path)

        return folder_path


register.register_class('Dialog', UnrealDialog)
register.register_class('OpenFileDialog', UnrealOpenFileDialog)
register.register_class('SaveFileDialog', UnrealSaveFileDialog)
register.register_class('SelectFolderDialog', UnrealSelectFolderDialog)
register.register_class('NativeDialog', UnrealNativeDialog)
