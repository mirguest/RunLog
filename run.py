#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author: lintao

import os.path
import uuid
import time

import tornado.ioloop
import tornado.web

cache = []

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("index.html")

class MessageNewHandler(tornado.web.RequestHandler):

    def post(self):
        message = {
                "runid": str(uuid.uuid4()),
                "from": self.get_argument("user", "Anonymous")
                }
        cache.append(message)

    def get(self):
        self.render("new_msg.html")

class MessageReadHandler(tornado.web.RequestHandler):

    def post(self):
        line = ""
        for c in cache:
            line += "\nHello %s\n"%c["from"]
        self.write(line)

settings = dict(
        static_path=os.path.join(os.path.dirname(__file__), "static"),
)

application = tornado.web.Application([
    (r"/", MainHandler),
    (r"/new", MessageNewHandler),
    (r"/read", MessageReadHandler),
], **settings)

if __name__ == "__main__":
    application.listen(8888)
    tornado.ioloop.IOLoop.instance().start()
