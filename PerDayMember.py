#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author: lintao

import anydbm

class PerDayMemberManager(object):
    def __init__(self, dbname='cache'):
        self._db = anydbm.open(dbname, 'c')

    def __del__(self):
        self._db.close()

    def save(self, day, userlist):
        self._db[day] = '#'.join(userlist)

    def get(self, day):
        if self._db.has_key(day):
            return self._db[day].split('#')
        return []

if __name__ == "__main__":
    pdmm = PerDayMemberManager()
    pdmm.save("2012/12/20", ['a', 'b'])
    print pdmm.get("2012/12/20")
    print pdmm.get("2012/12/21")
