import numpy as np

from sim_class import Sim

new_simulation = Sim(T=10**4)

new_simulation.init_strategy_population(s_initial = 0)
new_simulation.simulate_timesteps()


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
