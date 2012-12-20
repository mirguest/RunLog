#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author: lintao

from datetime import date, timedelta

class ModelDate(object):
    cache = None
    def __init__(self, indate=None):
        self._date = indate if indate else date.today()

        self._users = set()

    @property
    def date(self):
        return self._date

    @property
    def users(self):
        return self._users

    def appendUser(self, user):
        self._users.add(user)

    def removeUser(self, user):
        if user in self._users:
            self._users.remove(user)

class ModelDateManager(object):
    def __init__(self):
        self._cache = {}

    def add(self, md):
        if str(md.date) not in self._cache:
            self._cache[str(md.date)] = md

    def dateDelta(self, indate, delta):
        tmpdate = indate.date + delta
        if str(tmpdate) in self._cache:
            return self._cache[tmpdate]
        else:
            md = ModelDate(tmpdate)
            self._cache[str(tmpdate)] = md
            return md

    def getToday(self):
        md = ModelDate()
        self.add(md)
        return self._cache[str(md.date)]
        



if __name__ == "__main__":
    md = ModelDate()
    print md.date
    md.appendUser("lintao")
    md.appendUser("lin")
    for i in md.users:
        print i

    mdm = ModelDateManager()
    mdm.add(md)
    new_md = mdm.dateDelta(md, timedelta(2))
    print new_md.date
    for i in new_md.users:
        print i

    print mdm.getToday().date
    
