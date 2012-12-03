import pdb
import sys
from utils import Move, JustifyOver, printPebble
from techniques import Alpha_Beta
from nextstep import computer_next_step
#!/usr/bin/python
#import logging


def HvsC(human, computer, Clever_Stupid):
#    logger = logging.getLogger()
#    handler=logging.FileHandler("Log_game_2.txt")
#    logger.addHandler(handler)
#    logger.setLevel(logging.NOTSET)

    d = 5
    who_s_turn = 'A'
    dict = computer_next_step(computer, human, d, Clever_Stupid, who_s_turn)
    next_list = dict['list']
    if who_s_turn=='B':
        selected_index = len(next_list) - 1 - dict['index']
    else:
        selected_index = dict['index']
    human = next_list[0:len(next_list) / 2]
    computer = next_list[len(next_list) / 2 : len(next_list)]
    computer.reverse()

    return {
        "human": human, 
        "computer": computer,
        "selected_index": selected_index
        }
