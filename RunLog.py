#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author: lintao

import datetime
import calendar

import tornado.ioloop
import tornado.web

from PerDayMember import PerDayMemberManager

class Runner(tornado.web.RequestHandler):
    def initialize(self, dbname='runlog'):
        self.pdmm = PerDayMemberManager(dbname)

    @tornado.web.removeslash
    def get(self, userid=None):
        if userid is None:
            self.redirect("/register")
            return
        result = self.pdmm.user_get_by_id(int(userid))
        if not result:
            return
        self.render("runner.html",
                    userinfo=result.items(),
                    runlog=self.pdmm.getlog(int(userid)))

class RunnerRegister(tornado.web.RequestHandler):
    def initialize(self, dbname='runlog'):
        self.pdmm = PerDayMemberManager(dbname)

    @tornado.web.removeslash
    def get(self):
        self.render('register.html')

    def post(self):
        user = self.get_argument('user')
        email = self.get_argument('email')
        if self.pdmm.user_add(user=user, email=email):
            # if the email does not exist, add the user:
            self.write("Register Success")
        else:
            self.write("The email has been registered.")

class RunLogEveryDay(tornado.web.RequestHandler):
    def initialize(self, dbname='runlog'):
        self.pdmm = PerDayMemberManager(dbname)
        self.calendar = calendar.HTMLCalendar()

    def get(self, year, month, day):
        year, month, day = int(year), int(month), int(day)
        try:
            d = datetime.date(year, month, day)
        except:
            self.write("This day is not exist!")
            return
        strdate = d.strftime("%Y/%m/%d")

        this_month = self.calendar.formatmonth(d.year, d.month)

        self.render("runlog.html", 
                    userlist=self.pdmm.get(strdate),
                    strdate=strdate,
                    wholeusers=self.pdmm.getusers(),
                    this_month=this_month)


    def post(self, year, month, day):
        year, month, day = int(year), int(month), int(day)
        try:
            d = datetime.date(year, month, day)
        except:
            self.write("This day does not exist!")
            return
        strdate = d.strftime("%Y/%m/%d")
        user = self.get_argument("user", None)
        if user:
            self.pdmm.add(strdate, user)
        self.redirect("/%s"%strdate)
        pass
