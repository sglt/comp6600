import tornado.web
import tornado.escape
import time
import algorithm.HumanComputer
import logging

agents_mapping = {
    "Artificial Stupidity": 'B',
    "Artificial Intelligence": 'A',
}

class HVCNextHandler(tornado.web.RequestHandler):
    def post(self):
        current = tornado.escape.json_decode(self.request.body)
        human = current["human"]
        computer = current["computer"]
        ret_Pebble = algorithm.HumanComputer.HvsC(human,computer, agents_mapping[current["agent"]])
        human = ret_Pebble[0]
        computer = ret_Pebble[1]
        response = {
            "selected_index": ret_Pebble[2],
            "current": [human, computer],
            "ret_Pebble_temp": ret_Pebble,
        }
        self.write(tornado.escape.json_encode(response))