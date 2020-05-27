#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""
Initialization module for tpDcc.dccs.unreal
"""

from __future__ import print_function, division, absolute_import

import os
import logging

# =================================================================================

PACKAGE = 'tpDcc.dccs.unreal'

# =================================================================================


def create_logger(dev=False):
    """
    Returns logger of current module
    """

    logger_directory = os.path.normpath(os.path.join(os.path.expanduser('~'), 'tpDcc', 'logs'))
    if not os.path.isdir(logger_directory):
        os.makedirs(logger_directory)

    logging_config = os.path.normpath(os.path.join(os.path.dirname(__file__), '__logging__.ini'))

    logging.config.fileConfig(logging_config, disable_existing_loggers=False)
    logger = logging.getLogger(PACKAGE.replace('.', '-'))
    if dev:
        logger.setLevel(logging.DEBUG)
        for handler in logger.handlers:
            handler.setLevel(logging.DEBUG)

    return logger


def init_dcc(dev=False):
    """
    Initializes module
    :param dev: bool, Whether to launch code in dev mode or not
    """

    from tpDcc.dccs.unreal import register
    from tpDcc.libs.python import importer

    if dev:
        register.cleanup()

    register_resources()

    logger = create_logger(dev=dev)
    register.register_class('logger', logger)

    skip_modules = ['{}.{}'.format(PACKAGE, name) for name in ['loader', 'ui']]
    importer.init_importer(package=PACKAGE, skip_modules=skip_modules)


def init_ui():
    from tpDcc.libs.python import importer

    skip_modules = ['{}.{}'.format(PACKAGE, name) for name in ['loader', 'core']]
    importer.init_importer(package=PACKAGE, skip_modules=skip_modules)


def register_resources():
    """
    Registers tpDcc.libs.qt resources path
    """

    import tpDcc

    resources_manager = tpDcc.ResourcesMgr()
    resources_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'resources')
    resources_manager.register_resource(resources_path, key=tpDcc.Dccs.Unreal)

