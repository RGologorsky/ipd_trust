import numpy as np
import matplotlib.pyplot as plt
import time

from class_one_games import S_2_Game, S_4_Game
from class_two_games import S_12_Game, S_16_Game
from helper_functions import *

from simulation_evolution_avgs import *

# Parameters
num_timesteps = 10**4

game = S_12_Game(c=1.0, b1=2.0, b2=1.2, \
				game_transition_dynamics = "EqualSay_G2_Default", num_timesteps= num_timesteps)
params_dict = {
	"game":game,
	"N": 100,
	"eps": 0.001,
	"beta": 2.0,
	"host": tuple(0.005 for _ in range(game.strat_len)),
	"strategy_type": "pure", # or "stochastic"
}


b1_list = np.arange(1.0, 3.2, 0.42)
start_time = time.time()
#g1_cc_avg, g2_cc_avg, g1_rate = get_evolution_avgs(num_timesteps, params_dict)
get_b1_evolution_data(num_timesteps, b1_list, params_dict)
elapsed_time = time.time() - start_time

print("Elapsed Time: {:.2f} min".format(elapsed_time/60.0))

# lp = LineProfiler()
# lp_wrapper = lp(get_evolution_avgs)
# lp_wrapper(num_timesteps, params_dict)
# lp.print_stats()