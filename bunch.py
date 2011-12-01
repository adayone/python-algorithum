#!/usr/bin/env python2.7
#!coding=utf-8
class Bunch(dict):
    def __init__(self, *args,  **kwds):
        super(Bunch, self).__init__(self, *args, **kwds)
        self.__dict__ = self

