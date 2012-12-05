import pdb
import sys
from utils import Move, JustifyOver, printPebble
from techniques import Alpha_Beta
from nextstep import computer_next_step
#!/usr/bin/python



def HvsC(human, computer, Clever_Stupid):

    d = 3
    who_s_turn = 'A'
    dict = computer_next_step(computer, human, d, Clever_Stupid, who_s_turn)
    next_list = dict['list']
    
    if who_s_turn=='B':
        selected_index = len(next_list) - 1 - dict['index']
    else:
        selected_index = dict['index']
    
    computer = next_list[0:len(next_list) / 2]
    human = next_list[len(next_list) / 2 : len(next_list)]
    human.reverse()

    return {
        "human": human, 
        "computer": computer,
        "selected_index": selected_index
        }
