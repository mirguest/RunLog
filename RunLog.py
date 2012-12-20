#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author: lintao

import datetime

import tornado.ioloop
import tornado.web

class RunLogEveryDay(tornado.web.RequestHandler):
    def get(self, year, month, day):
        year, month, day = int(year), int(month), int(day)
        try:
            d = datetime.date(year, month, day)
        except:
            self.write("This day is not exist!")
            return
        self.write(d.strftime("%Y/%m/%d"))
