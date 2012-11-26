import pdb
import sys
from utils import Move, JustifyOver, printPebble
from techniques import Alpha_Beta
#!/usr/bin/python


if __name__ == '__main__':
    input_n = 3
    d = 5
    game =Alpha_Beta(input_n,d)

    while input_n >= 2:

        action_a = game.Search('A');
        if(action_a <0): print 'it can not get any actions'
        print 'action_a = ', action_a
        game.change(action_a);

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
