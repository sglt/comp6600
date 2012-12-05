import tornado.web
import tornado.escape
import time
import algorithm.HumanComputer
import algorithm.ComputerComputer
import logging

agents_mapping = {
    "Artificial Stupidity": 'stupid',
    "Artificial Intelligence": 'intelligent',
    "A": 'stupid',
    "B": 'intelligent',
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
        ret_Pebble = algorithm.ComputerComputer.CvsC(current["A"], current["B"], agents_mapping[current["whos_turn"]], current["whos_turn"])
        response = {
            "selected_index": ret_Pebble["selected_index"],
            "current": {
                "A": ret_Pebble["computer_A"],
                "B": ret_Pebble["computer_B"],
            },
            "ret_Pebble_temp": None,
            "previous_temp": current,
        }
        self.write(tornado.escape.json_encode(response))