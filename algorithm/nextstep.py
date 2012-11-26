from utils import Move, JustifyOver, printPebble
from techniques import Alpha_Beta

def computer_next_step(currentlist,input_n,d):
    game =Alpha_Beta(input_n,d)
    game.re_construct_pebble(currentlist)
    action_a = game.Search('A');
    if(action_a <0): print 'it can not get any actions'
        print 'action_a = ', action_a
    game.change(action_a);
    return game.RotateList
    
    
    
def Human_next_step(currentlist,action,input_n,d):
    game =Alpha_Beta(input_n,d)
    game.re_construct_pebble(currentlist)
    game.change(action);
    return game.RotateList