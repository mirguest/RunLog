#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author: lintao

import datetime

import tornado.ioloop
import tornado.web

from PerDayMember import PerDayMemberManager

class RunLogEveryDay(tornado.web.RequestHandler):
    def initialize(self, dbname='cache'):
        self.pdmm = PerDayMemberManager(dbname)

    def get(self, year, month, day):
        year, month, day = int(year), int(month), int(day)
        try:
            d = datetime.date(year, month, day)
        except:
            self.write("This day is not exist!")
            return
        strdate = d.strftime("%Y/%m/%d")

        line = "<ul>"
        for user in self.pdmm.get(strdate):
            line += "<li>%s</li>"%user
        line += "</ul>"

        line += '<form action="/%s" method="post">' % strdate
        line += '<input type="text" name="user" />'
        line += '<input type="submit" value="Add" />'
        line += '</form>'
        self.write(line)

    def post(self, year, month, day):
        year, month, day = int(year), int(month), int(day)
        try:
            d = datetime.date(year, month, day)
        except:
            self.write("This day is not exist!")
            return
        strdate = d.strftime("%Y/%m/%d")
        user = self.get_argument("user", None)
        if user:
            self.pdmm.add(strdate, user)
        self.get(year, month, day)
        pass
