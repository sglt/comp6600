import os
import tornado.ioloop
import tornado.web

import ajax

application = tornado.web.Application([
    (r"/", tornado.web.RedirectHandler, {"url": "/static/index.html"}),
    (r"/static/(.*)", tornado.web.StaticFileHandler, {"path": "static"}),
    (r"/ajax/hvcnext", ajax.HVCNextHandler),
    (r"/ajax/cvcnext", ajax.CVCNextHandler),
    ("/(favicon.ico)", tornado.web.StaticFileHandler, {'path': "static"}),
])

if __name__ == "__main__":
    application.listen(os.environ["PORT"], os.environ["IP"])
    tornado.ioloop.IOLoop.instance().start()
