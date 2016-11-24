# -*- coding: utf-8 -*-
# @Author: cody kochmann
# @Date:   2016-11-23 07:52:40
# @Last Modified 2016-11-24
# @Last Modified time: 2016-11-24 10:10:01

from functools import wraps
import logging

class default_output(object):
    """ returns the backup plan if the decorated method fails
        by: Cody Kochmann """
    def __init__(self, backup_output):
        self.backup_output = backup_output
    def __call__(self,f):
        assert callable(f), "default_output needs a callable target to wrap"
        def wrapper(*args, **kwargs):
            try:
                return f(*args, **kwargs)
            except Exception, e:
                # this is where logging would happen
                logging.exception(e)
                # ====================================
                return self.backup_output
        return wrapper
