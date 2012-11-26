import pdb
import sys
from utils import Move, JustifyOver, printPebble
from techniques import Alpha_Beta
from nextstep import computer_next_step,Human_next_step
#!/usr/bin/python


def algorithm(input_n, d, currentlist):
    
    input_n = 3
    d = 5

    while input_n >= 2:

        computer_next_step(input_n,d,input_n)

        print '-------------------Now it is B turn'
        printPebble(game.RotateList)
        if(JustifyOver(game.RotateList,input_n)):
            break

        while 1:
            action_b = input("Enter the action: ") #MiniMax_Decision(RotateList,'B');
            action_b = int(action_b)
            if game.change(action_b):
                break

        print '-------------------Now it is A turn'
        printPebble(game.RotateList)
        if(JustifyOver(game.RotateList,input_n)):
            break
