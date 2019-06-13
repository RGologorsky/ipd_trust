import numpy as np
import pandas as pd

from helper_functions import save_dict
from get_spe_list import *
from simulation_evolution_avgs import *

import multiprocessing as mp
import time

# IMPORTANT CHANGE THIS BACK TO REAL PARAM - from test_parameters import *
from parameters import *


# set folder name
folder_timestamp = time.strftime("date_%Y_%m_%d_%H_%M_%S")
data_folder = get_b1_effect_folder(folder_timestamp, directory="data/b1_effect")

print("\nData Folder: {:s}\n".format(data_folder))


def do_run(run_id, game_str, strat_str, transition_str, params_dict, spe_d):
	
	np.random.seed()

	data_filename = data_folder + game_str + "_run_{:d}".format(run_id) + ".csv"

	# announce what we are calculating
	print("Game: {:s}, Run: {:d}".format(game_str, run_id))
	
	# get data
	start_time = time.time()
	g1_cc_avgs, g2_cc_avgs, g1_game_avgs, player_c_avgs, spe_avgs, host_ds  = \
		get_b1_evolution_data(num_timesteps, game_params_list, params_dict, spe_d)
	
	elapsed_time = time.time() - start_time

	print("Elapsed Time: {:.2f} min".format(elapsed_time/60.0))

	df = pd.DataFrame(np.column_stack([alpha1_col, c1_col, g1_cc_avgs, g2_cc_avgs, g1_game_avgs, player_c_avgs, spe_avgs]), 
                       columns=['alpha1', 'c1', '1CC rate', '2CC rate', 'Game 1 rate', 'C rate', 'CoopSPE rate'])

	df['strat']       = game_str
	df['strat_space'] = strat_str
	df['transition']  = transition_str

	df.to_csv(data_filename, index=False)

	# for i, host_d in enumerate(host_ds):
	# 	str_key_d = {str(k): v for k, v in host_d.items()}
	# 	d_filename = data_folder + game_str + "_run_{:d}_alpha1_{:.2f}_c1_{:.2f}".format(run_id, game_params_list[i])
	# 	save_dict(str_key_d, d_filename)


def parallel_write_alpha1_effect_data():

	for game in games:

		# update game
		host_strat = (params_dict["eps"],) *  game.strat_len
		params_dict["host"] = host_strat
		params_dict["game"] = game

		for game_transition_dynamics in transitions:

			# update game transition dynamics
			game.set_game_transition_dynamics(game_transition_dynamics)

			game_str, strat_str, transition_str = str(game), game.strat_str(), game.transition_str()
			spe_d = get_spe_dict(transition_str, str(game), b1_list, eps)

			jobs = []
			for run_id in range(num_runs):
				p = mp.Process(target=do_run, args=(run_id, game_str, strat_str, transition_str, \
													params_dict, spe_d)) 
				p.start()
				jobs.append(p)
			
			# wait until all jobs done
			for p in jobs:
				p.join()


parallel_write_alpha1_effect_data()
