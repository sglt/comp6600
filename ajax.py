import tornado.web
import tornado.escape
import time

class HVCNextHandler(tornado.web.RequestHandler):
    def post(self):
        current = tornado.escape.json_decode(self.request.body)
        human = current[0]
        computer = current[1]
        # decide next step, change "human" and "computer"
        time.sleep(1)
        computer[0] = 0;
        response = {
            "selected_index": 0,
            "current": [human, computer],
        }
        self.write(tornado.escape.json_encode(response))