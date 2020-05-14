#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""
Initialization module for tpDcc.dccs.unreal
"""

from __future__ import print_function, division, absolute_import

import os
import inspect
import logging

from tpDcc.libs.python import importer
from tpDcc.dccs.unreal import register


class tpUnrealLib(importer.Importer, object):
    def __init__(self, *args, **kwargs):
        super(tpUnrealLib, self).__init__(module_name='tpDcc.dccs.unreal', *args, **kwargs)

    def get_module_path(self):
        """
        Returns path where tpDcc.dccs.unreal module is stored
        :return: str
        """

        try:
            mod_dir = os.path.dirname(inspect.getframeinfo(inspect.currentframe()).filename)
        except Exception:
            try:
                mod_dir = os.path.dirname(__file__)
            except Exception:
                try:
                    import tpDcc.dccs.unreal
                    mod_dir = tpDcc.dccs.unreal.__path__[0]
                except Exception:
                    return None

        return mod_dir


def create_logger(dev=False):
    """
    Returns logger of current module
    """

    logging.config.fileConfig(get_logging_config(), disable_existing_loggers=False)
    logger = logging.getLogger('tpDcc-dccs-unreal')
    if dev:
        logger.setLevel(logging.DEBUG)
        for handler in logger.handlers:
            handler.setLevel(logging.DEBUG)

    return logger


def create_logger_directory():
    """
    Creates tpDcc.dccs.unreal logger directory
    """

    logger_path = os.path.normpath(os.path.join(os.path.expanduser('~'), 'tpDcc', 'logs'))
    if not os.path.isdir(logger_path):
        os.makedirs(logger_path)


def get_logging_config():
    """
    Returns logging configuration file path
    :return: str
    """

    create_logger_directory()

    return os.path.normpath(os.path.join(os.path.dirname(__file__), '__logging__.ini'))


def init_dcc(do_reload=False, dev=False):
    """
    Initializes module
    :param do_reload: bool, Whether to reload modules or not
    """

    from tpDcc.libs.qt.core import resource as resource_utils

    class tpUnrealLibResource(resource_utils.Resource, object):
        RESOURCES_FOLDER = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'resources')

    logger = create_logger(dev=dev)

    unreal_importer = importer.init_importer(importer_class=tpUnrealLib, do_reload=False)

    register.register_class('resource', tpUnrealLibResource)
    register.register_class('logger', logger)

    unreal_importer.import_modules(skip_modules=['tpDcc.dccs.unreal.ui'])
    unreal_importer.import_packages(only_packages=True, skip_modules=['tpDcc.dccs.unreal.ui'])
    if do_reload:
        unreal_importer.reload_all()


def init_ui(do_reload=False):
    unreal_importer = importer.init_importer(importer_class=tpUnrealLib, do_reload=False)

    unreal_importer.import_modules(skip_modules=['tpDcc.dccs.unreal.core'])
    unreal_importer.import_packages(only_packages=True, skip_modules=['tpDcc.dccs.unreal.core'])
    if do_reload:
        unreal_importer.reload_all()
