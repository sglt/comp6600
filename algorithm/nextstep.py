from utils import Move, JustifyOver, printPebble
from techniques import Alpha_Beta


def computer_next_step(A,B,d,Clever_Stupid,who_s_turn):

    
    input_n = len(A)
    game =Alpha_Beta(input_n,d)
    game.re_construct_pebble(A,B)
    action_a = game.Search(Clever_Stupid,who_s_turn);

    game.change(action_a);
    return {'list':game.RotateList, 'index':action_a}
