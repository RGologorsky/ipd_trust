import numpy as np

from sim_class import Sim

from pure_12_game_class import Pure_12_Game
from pure_16_game_class import Pure_16_Game
from pure_one_game_class import Pure_One_Game

from test_cc_vs_b import test_cc_vs_b
from plotting import plot

# game = Pure_16_Game(c=1.0, b1=1.9, b2=1.2)
T = 10**5

game = Pure_One_Game(c=1.0, b1=20.0, eps=0.01)
new_simulation = Sim(T=T, game = game, do_plots = False)
new_simulation.init_strategy_population(s_initial = 0)

new_simulation.simulate_timesteps()
plot(np.arange(new_simulation.T), new_simulation.avg_cc_data, \
    title = "Prob[C] over Time", xlabel = "Timestep", ylabel = "Prob[C]")

print(new_simulation.avg_cc_data)
print("avg ", np.mean(new_simulation.avg_cc_data))

# file = open("avg_c_data.txt","w") 
# file.write("avg c data") 

# for i in range(int(T/20)):
#     last_index = 20 * i
#     file.write(str(new_simulation.avg_cc_data[last_index:last_index+20]))
# file.close() 

# (b1_list, cc_list) = test_cc_vs_b(Pure_One_Game, T=10**5, b1_start=1, b1_end=3, \
#                                     num_test_pts=5)

# plot(b1_list, cc_list, title = "CC v. b1 value", xlabel = "b1 value", ylabel = "CC")

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
