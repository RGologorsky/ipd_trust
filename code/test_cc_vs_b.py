# CC vs. b

import numpy as np

from sim_class import Sim

from pure_12_game_class import Pure_12_Game
from pure_16_game_class import Pure_16_Game
from pure_one_game_class import Pure_One_Game

def test_cc_vs_b(cls, T=10**5, b1_start=1, b1_end=3, num_test_pts=5):

    b1_list = np.linspace(b1_start, b1_end, num_test_pts)
    cc_list = np.zeros(num_test_pts)

    for index, b1 in enumerate(b1_list):
        game = cls(c=1.0, b1=b1, b2=1.2)
        sim  = Sim(T = T, game = game, do_plots = False)
        sim.init_strategy_population(s_initial = 0)
        cc_list[index] = sim.simulate_timesteps()

    print("b1_list ", b1_list)
    print("cc_list", cc_list)

    return (b1_list, cc_list)



# # Game settings, parameters
# from init_game import *

# # initialize strategy population with ALL-D
# init_strategy_population(0)


# def print_strategy_result(s1, s2):
#     s1_str = strat_to_str(s1)
#     s2_str = strat_to_str(s2)
#     print("Results for: s1 vs s2, where \n")
#     print("s1 = {:s}\n".format(s1_str))
#     print("s2 = {:s}\n".format(s2_str))

#     s1_pi, s2_pi, avg_CC = play_n_rounds(s1, s2, n = 10, initial_state = 0)

#     print("s1 Payoff: {}, s2 Payoff: {}, CC rate: {}\n".format(s1_pi, s2_pi, avg_CC))

# print_strategy_result(0,0)
# print_strategy_result(2**16-1, 2**16-1)
# print_strategy_result(0, 2**16-1)
