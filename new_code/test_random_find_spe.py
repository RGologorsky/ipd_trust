import numpy as np

from random_find_spe import *
from helper_functions   import *
from class_two_games    import *

import pprint as pp

delta = 1.0 - 10**-5


s12_game = S_12_Game(b1=1.8, b2=1.2, c1=1.0, c2=1.0, resolution_rule = "Random")
strat = (1,0,0,0,1,0,0,1,1,1,1,1)

payoff_dict = get_p2_payoff_dict(strat, s12_game)
Q_dict      = get_Q_dict(strat, s12_game) 

print("p2 payoff dict")
pp.pprint(payoff_dict)

print("Q dict")
pp.pprint(Q_dict)

print("state values")
state_values = get_state_values(strat, s12_game, delta, tol=10**-5)
pp.pprint(state_values)