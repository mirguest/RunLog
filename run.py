#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author: lintao

import os.path
import uuid
import time
import datetime

import tornado.ioloop
import tornado.web

# My own:
from DefineData import *
from RunLog import *

gMDM = ModelDateManager()

class MainHandler(tornado.web.RequestHandler):
    def get(self):

        d = datetime.date.today()
        strdate = d.strftime("%Y/%m/%d")
        self.redirect("/%s"%strdate)

class MessageNewHandler(tornado.web.RequestHandler):

    def post(self):
        message = {
                "runid": str(uuid.uuid4()),
                "from": self.get_argument("user", None)
                }
        if message["from"]:
            md = gMDM.getToday()
            md.appendUser( message["from"] )


    def get(self):
        self.render("new_msg.html")

class MessageReadHandler(tornado.web.RequestHandler):

    def post(self):
        line = "<ul>"
        cache = gMDM.getToday().users
        for c in cache:
            line += "<li>%s</li>"%c
        line += "</ul>"
        self.write(line)

settings = dict(
        static_path=os.path.join(os.path.dirname(__file__), "static"),
        template_path=os.path.join(os.path.dirname(__file__), "template"),
)

application = tornado.web.Application([
    (r"/new", MessageNewHandler),
    (r"/read", MessageReadHandler),
    (r"/(\d+)/(\d+)/(\d+)", RunLogEveryDay),
    (r"/user/(\d+)", Runner),
    (r"/user/?", Runner),
    (r"/register", RunnerRegister),
    (r"/.*", MainHandler),
], **settings)

if __name__ == "__main__":
    application.listen(8888)
    tornado.ioloop.IOLoop.instance().start()
