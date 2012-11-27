from utils import Move, JustifyOver, printPebble
from techniques import Alpha_Beta

def computer_next_step(currentlist,input_n,d,Clever_Stupid):
    game =Alpha_Beta(input_n,d)
    game.re_construct_pebble(currentlist)
    action_a = game.Search(Clever_Stupid);
    game.change(action_a);
    return {'list':game.RotateList, 'index':action_a}
