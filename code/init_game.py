from constants import *
from strategy_helpers import *

# 8 states, ranging from 0 to 7, corresponding to 1CC to 2DD.
states = {
    (1,1,1): 0, # 1CC
    (1,1,0): 1, # 1CD
    (1,0,1): 2, # 1DC
    (1,0,0): 3, # 1DD

    (2,1,1): 4, # 2CC
    (2,1,0): 5, # 2CD
    (2,0,1): 6, # 2DC
    (2,0,0): 7, # 2DD
}

# player1, player2 payoffs for outcomes 1CC, ..., 1DD, 2CC, ..., 2DD
p1_payoffs = [b1-c, -c, b1, 0, b2-c, -c, b2, 0];
p2_payoffs = [b1-c, b1, -c, 0, b2-c, b2, -c, 0];

max_num_strategies = 2**16;

def to_strategy(num):
    return [int(x) for x in format(num, '016b')]

def strat_to_str(num):
    arr = to_strategy(num)
    return str(arr[0:4])   + "," + \
            str(arr[4:8])  + ". Transition: " + \
            str(arr[8:12])  + "," + \
            str(arr[12:16])

def mc_estimate(s1, s2, n = 10, initial_state = 0):
    '''
        Return avg payoffs when s1 plays s2 and CC rate
    '''
    s1_total_payoff = 0.0
    s2_total_payoff = 0.0

    cc_rate     = 0.0
    game_1_rate = 0.0

    prev_state = initial_state

    s1 = to_strategy(s1)
    s2 = to_strategy(s2)

    for i in range(n):
        s1_move, s1_game_pref = s1[prev_state], s1[prev_state + 8]
        s2_move, s2_game_pref = s2[prev_state], s2[prev_state + 8]
        
        curr_game = 1 if s1_game_pref and s2_game_pref else 2
        curr_state = states[(curr_game, s1_move, s2_move)]

        s1_total_payoff += p1_payoffs[curr_state]
        s2_total_payoff += p2_payoffs[curr_state]

        # mutual cooperation = 1CC or 2CC
        if curr_state % 4 == 0:
            cc_rate += 1

        if curr_game == 1:
            game_1_rate += 1

    # return s1 avg payoff, s2 avg payoff, avg CC ratex
    return (s1_total_payoff/n, s2_total_payoff/n, cc_rate/n, game_1_rate/n)
