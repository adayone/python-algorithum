#!/usr/bin/env python2.7
#!coding=utf-8
class Bunch:
    def __init__(self,  **kwds):
        self.__dict__.update(kwds)

