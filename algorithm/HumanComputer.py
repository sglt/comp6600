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
    input_n = len(human)

    computer.reverse()
    currentList = computer + human if Clever_Stupid == 'A' else human + computer

    dict = computer_next_step(currentList,input_n,d,Clever_Stupid)
    next_list = dict['list']
    selected_index = len(next_list)/2 - 1 - dict['index']
#    logger.debug("in algorithm current_list : %s",str(next_list))
#    logger.debug("in algorithm selected_index : %s",str(selected_index))

    computer = next_list[0:len(next_list) / 2]
    human = next_list[len(next_list) / 2 : len(next_list)]

    if Clever_Stupid == 'B':
        human, computer = computer, human
    
    computer.reverse()


    return [human, computer, selected_index]
