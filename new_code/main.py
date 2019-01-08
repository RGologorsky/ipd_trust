import numpy as np
import matplotlib.pyplot as plt
import time

from class_one_games import S_2_Game, S_4_Game
from class_two_games import S_12_Game, S_16_Game
from helpers import *
from simulations import *


# Parameters
num_trials = 1000
game = S_12_Game(c=1.0, b1=2.0, b2=1.2)
params_dict = {
	"game":game,
	"N": 100,
	"eps": 0.005,
	"beta": 2.0,
	"host": tuple(0.005 for _ in range(game.strat_len)),
	"strategy_type": "pure", # or "stochastic"
	"max_attempts": 10**4,
}

######### Plot Successful Invaders ##########
# start_time = time.time()
# strategies, num_invasion_attempts = get_invasion_distr(num_trials, params_dict)
# elapsed_time = time.time() - start_time

# print("Elapsed Time: {:.2f} min".format(elapsed_time/60.0))

# mean, sample_sd, string_description = get_sample_statistics(num_invasion_attempts)
# print("Num. Invasion Attempts:\n" + string_description)

# # Plot
# ps, qs = zip(*strategies)
# titlebox_str = "Num. Invasion Attempts:\n" + string_description
# plot_scatter(ps, qs, "p", "q", "Successful ALL-D Invader Strategies", titlebox_str)
#############


num_timesteps = 10**5
data_collection_freq = 100
data_collection_points = np.arange(num_timesteps, step = data_collection_freq)

start_time = time.time()
host_seq, host_timespans, cc_timestep_data, g1_timestep_data = \
	get_evolution_data(num_timesteps, data_collection_freq, params_dict)

elapsed_time = time.time() - start_time

print("Elapsed Time: {:.2f} min".format(elapsed_time/60.0))
#print("host timespans\n", host_timespans)
#print_matrix("host_seq", host_seq)
print("=== CC Rates ===")
print(cc_timestep_data)
print("=== G1 Rates ===")
print(g1_timestep_data)

# Plot
titlebox_str = "Params:\n $\epsilon = {:.4f}$\n $\beta = {:.4f}$"\
				.format(params_dict["eps"], params_dict["beta"])

plot_line(data_collection_points, cc_timestep_data, \
			"Timestep", "CC rate", "Evolution of Mutual Cooperation", titlebox_str)
