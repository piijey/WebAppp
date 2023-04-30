import os
import tornado.ioloop
import tornado.web

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Hello, world")

def make_app():
    return tornado.web.Application([
        (r"/", MainHandler),
    ])

application = make_app()

if __name__ == "__main__":
    port = int(os.environ.get('PORT', 8889))
    application.listen(port)
    tornado.ioloop.IOLoop.current().start()
