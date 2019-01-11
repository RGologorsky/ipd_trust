import numpy as np
import matplotlib.pyplot as plt
import time

from class_one_games import S_2_Game, S_4_Game
from class_two_games import S_12_Game, S_16_Game
from simulation_evolution_avgs import *

# Parameters
num_timesteps = 4*(10**5)

params_dict = {
	"N": 100,
	"eps": 0.001,
	"beta": 2.0,
	"strategy_type": "pure", # or "stochastic"
	"max_attempts": 10**4,
}


b1_list = np.arange(1.0, 3.2, 0.14)

def run():
	for game in [S_12_Game(c=1.0, b1=2.0, b2=1.2), S_16_Game(c=1.0, b1=2.0, b2=1.2)]:

		# choose S12 or S16 game
		params_dict["game"] = game

		host_strat = (params_dict["eps"],) *  game.strat_len
		print("host strat: ", host_strat)

		params_dict["host"] = host_strat

		print(str(game), "strat len", str(game.strat_len))
		print(params_dict["host"])

		for index in range(4):

			# announce what we are calculating
			print("Game: {:s}, Run: {:d}".format(str(game), index))
			
			# get data
			start_time = time.time()
			cc_avgs, g1_avgs = get_b1_evolution_data(num_timesteps, b1_list, params_dict)
			elapsed_time = time.time() - start_time

			print("Elapsed Time: {:.2f} min".format(elapsed_time/60.0))

			# file where to save data
			params_str = "eps_{eps}_beta_{beta}_T_{T}_game_{game_str}_run_{run}"\
							.format(T=num_timesteps, game_str = str(game), run = index, **params_dict)
			
			timestamp = time.strftime("date_%Y_%m_%d_time_%H_%M_%S")

			filename = "data/b1_effect_{:s}_{:s}.csv".format(params_str, timestamp)

			# save data
			with open(filename,'ab') as f:
			    np.savetxt(f, (b1_list, cc_avgs, g1_avgs), delimiter=",")

run()