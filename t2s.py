#!/usr/local/bin/python2.7
# -*- coding: utf-8 -*-

import os
import codecs

RootPath = os.path.dirname(__file__)

class TrandSimp(object):
    _Trandition = []
    _Simpled = []

    with codecs.open(RootPath + '/data/ft.txt', 'r', 'utf-8') as f:
        _Trandition = f.read().strip()

    with codecs.open(RootPath + '/data/jt.txt', 'r', 'utf-8') as f:
        _Simpled = f.read().strip()

    _T2S = dict(zip(_Trandition, _Simpled))
    _S2T = dict(zip(_Simpled, _Trandition))

    def __init__(self):
        pass

    @staticmethod
    def T2S(unc):
        return TrandSimp._T2S.get(unc, unc)

    @staticmethod
    def S2T(unc):
        return TrandSimp._S2T.get(unc, unc)


if __name__ == "__main__":
    # the simplied to the tranditional
    print TrandSimp.S2T(u'师')
    # the tranditional to the simplied
    print TrandSimp.T2S(u'師')
