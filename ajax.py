import tornado.web
import tornado.escape
import time
import algorithm.HumanComputer
import logging

agents_mapping = {
    "Artificial Stupidity": 'stupid',
    "Artificial Intelligence": 'intelligent',
}

class HVCNextHandler(tornado.web.RequestHandler):
    def post(self):
        current = tornado.escape.json_decode(self.request.body)
        human = current["human"]
        computer = current["computer"]
        ret_Pebble = algorithm.HumanComputer.HvsC(human,computer, agents_mapping[current["agent"]])
        response = {
            "selected_index": ret_Pebble["selected_index"],
            "current": {
                "human": ret_Pebble["human"],
                "computer": ret_Pebble["computer"],
                },
            "ret_Pebble_temp": ret_Pebble,
        }
        self.write(tornado.escape.json_encode(response))
        
class CVCNextHandler(tornado.web.RequestHandler):
    def post(self):
        current = tornado.escape.json_decode(self.request.body)
        response = {
            "selected_index": 0,
            "current": {
                "A": current["A"],
                "B": current["B"],
            },
            "ret_Pebble_temp": None,
            "previous": current,
        }
        self.write(tornado.escape.json_encode(response))