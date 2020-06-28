#!/usr/bin/python
# -*- encoding:utf-8 -*-

from __future__ import (absolute_import, division, print_function, unicode_literals)

__metaclass__ = type

import sys
from ansible.plugins.callback import CallbackBase
from ansible import __version__ as ansible_version


def print_red_bold(text):
    print('\x1b[31;1m' + text + '\x1b[0m')


class CallbackModule(CallbackBase):
    CALLBACK_VERSION = 2.0
    CALLBACK_TYPE = 'stdout'

    def __init__(self):
        required_version = '2.9'
        if ansible_version[:ansible_version.rindex(".")] != required_version:
            print_red_bold(
                "Restriction: only Ansible ={version}.X is supported."
                "You should install it with:\n\n"
                "\tpip install ansible=={version}.*\n".format(version=required_version)
            )
            sys.exit(1)


ansible_version = CallbackModule()
