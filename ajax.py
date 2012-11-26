import tornado.web
import tornado.escape

class HVCNextHandler(tornado.web.RequestHandler):
    def post(self):
        current = tornado.escape.json_decode(self.request.body)
        human = current[0]
        computer = current[1]
        # decide next step, change "human" and "computer"
        computer[0] = 0;
        response = {
            "selected_index": 0,
            "current": [human, computer],
        }
        self.write(tornado.escape.json_encode(response))