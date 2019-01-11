import numpy as np
import matplotlib.pyplot as plt
import time

from class_one_games import S_2_Game, S_4_Game
from class_two_games import S_12_Game, S_16_Game
from simulation_evolution_avgs import *

# Parameters
game = S_16_Game(c=1.0, b1=2.0, b2=1.2)
num_timesteps = 10**5

params_dict = {
	"game":game,
	"N": 100,
	"eps": 0.001,
	"beta": 2.0,
	"host": tuple(0.005 for _ in range(game.strat_len)),
	"strategy_type": "pure", # or "stochastic"
	"max_attempts": 10**4,
}


b1_list = np.arange(1.0, 3.2, 0.2)

def run():
	start_time = time.time()
	cc_avgs, g1_avgs = get_b1_evolution_data(num_timesteps, b1_list, params_dict)
	elapsed_time = time.time() - start_time
	print("Elapsed Time: {:.2f} min".format(elapsed_time/60.0))

	# file to save data
	timestamp = time.strftime("date_%Y_%m_%d_time_%H_%M_%S")
	params_str = "eps_{eps}_beta_{beta}_T_{T}_game_{game_str}"\
					.format(T=num_timesteps, game_str = str(game), **params_dict)
	
	filename = "data/b1_effect_{:s}_{:s}.csv".format(params_str, timestamp)

	with open(filename,'ab') as f:
	    np.savetxt(f, (b1_list, cc_avgs, g1_avgs), delimiter=",")


#run()