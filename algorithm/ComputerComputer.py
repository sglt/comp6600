import pdb
import sys
from utils import Move, JustifyOver, printPebble
from techniques import Alpha_Beta
from nextstep import computer_next_step
#!/usr/bin/python


def CvsC(computer_A, computer_B, Clever_Stupid, who_s_turn):

    d = 5
#    who_s_turn = 'A'
    dict = computer_next_step(computer_A, computer_B, d, Clever_Stupid, who_s_turn)
    next_list = dict['list']
    
    if who_s_turn=='B':
        selected_index = len(next_list) - 1 - dict['index']
    else:
        selected_index = dict['index']
    
    computer_A = next_list[0:len(next_list) / 2]
    computer_B = next_list[len(next_list) / 2 : len(next_list)]
    computer_B.reverse()

    return {
        "computer_B": computer_B, 
        "computer_A": computer_A,
        "selected_index": selected_index
        }
