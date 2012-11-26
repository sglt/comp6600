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


        action_b = game.Search('B')
        game.change(action_b)
        print 'action_b = ', action_b
        print '-------------------Now it is A turn'
        printPebble(game.RotateList)
        if(JustifyOver(game.RotateList,input_n)):
            break
