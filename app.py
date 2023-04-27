import tornado.ioloop
import tornado.web
import tornado.websocket
import os
import modifier

clients = set()

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("index.html")

class WebSocketHandler(tornado.websocket.WebSocketHandler):
    def open(self):
        clients.add(self)
        print("WebSocket opened")

    def on_message(self, message):
        modified_message = modifier.adds(message)
        for client in clients:
            client.write_message(modified_message)

    def on_close(self):
        clients.remove(self)
        print("WebSocket closed")

def make_app():
    return tornado.web.Application([
        (r"/", MainHandler),
        (r"/websocket", WebSocketHandler),
        (r"/static/(.*)", tornado.web.StaticFileHandler, {'path': 'static'}),
    ])

if __name__ == "__main__":
    app = make_app()
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()
