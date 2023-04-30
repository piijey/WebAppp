import tornado.ioloop
import tornado.web
import response

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("index.html")

class PiePieHandler(tornado.web.RequestHandler):
    def post(self):
        input_text = self.get_body_argument("input_text")
        print("PiePieHandler --", input_text)
        piepie_text = "input:\t" + input_text + "\nresponse:\t" + response.piepie_response(input_text)
        self.write(piepie_text)

def make_app():
    return tornado.web.Application([
        (r"/", MainHandler),
        (r"/piepie", PiePieHandler),
    ])

if __name__ == "__main__":
    app = make_app()
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()
