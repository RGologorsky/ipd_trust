import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import time

from class_one_games import S_2_Game, S_4_Game
from class_two_games import S_8_Game, S_12_Game, S_16_Game

# NOT USING PARALLEL
from simulation_evolution_avgs import *

import pandas as pd
import pathlib # to create directory if needed

from parameters import *
# IMPORTANT CHANGE THIS BACK TO REAL PARAM - from test_parameters import *

from get_spe_list import *

import multiprocessing as mp
#import threading

# define folder name
def get_folder(timestamp, directory="data/b1_effect"):
	folder = "{:s}/eps_{:.2e}_beta_{:.2e}_T_{:.2e}_c_{:.2f}_b2_{:.2f}/{:s}/"\
		.format(directory, eps, beta, num_timesteps, c, b2, timestamp)

	# create directory
	pathlib.Path(folder).mkdir(parents=True, exist_ok=True) 
	return folder

# set folder name
folder_timestamp = time.strftime("date_%Y_%m_%d_%H_%M_%S")

data_folder = get_folder(folder_timestamp, directory="data/b1_effect")
img_folder  = get_folder(folder_timestamp, directory="imgs/b1_effect")

print("\nData Folder: {:s}\n".format(data_folder))


#b1_list = np.arange(1.0, 3.2, 0.56)
#b1_list = [1.8]
b1_list = np.arange(1.0, 3.2, 0.14)

transition = transitions[0]
games   = [
			#S_2_Game(c=1.0, b1=1.2), 
			#S_4_Game(c=1.0, b1=2.0), 
			#S_8_Game(c=1.0, b1=2.0, b2=1.2,  game_transition_dynamics=transitions[0]), 
			S_12_Game(c=1.0, b1=2.0, b2=1.2, game_transition_dynamics=transitions[0]), 
			S_16_Game(c=1.0, b1=2.0, b2=1.2, game_transition_dynamics=transitions[0]), 
		]


#spe_lst = get_eps_spe_list(eps, s8_pure_spe_lst)
#spe_lst = get_eps_spe_list(eps, s12_pure_spe_lst)
#spe_lst = get_eps_spe_list(eps, s16_pure_spe_lst)

#spe_lst = s12_spe_lst
#spe_lst = s16_spe_lst

def do_run(run_id, data_folder, game_str, strat_str, transition_str, num_timesteps, b1_list, params_dict, spe_d):
	data_filename = data_folder + game_str + "_run_{:d}".format(run_id) + ".csv"

	# announce what we are calculating
	print("Game: {:s}, Run: {:d}".format(game_str, run_id))
	
	# get data
	start_time = time.time()
	g1_cc_avgs, g2_cc_avgs, g1_game_avgs, player_c_avgs, spe_avgs  = \
		get_b1_evolution_data(num_timesteps, b1_list, params_dict, spe_d)
	
	elapsed_time = time.time() - start_time

	print("Elapsed Time: {:.2f} min".format(elapsed_time/60.0))

	df = pd.DataFrame(np.column_stack([b1_list, g1_cc_avgs, g2_cc_avgs, g1_game_avgs, player_c_avgs, spe_avgs]), 
                       columns=['b1', '1CC rate', '2CC rate', 'Game 1 rate', 'C rate', 'SPE rate'])

	df['strat']       = game_str
	df['strat_space'] = strat_str
	df['transition']  = transition_str

	df.to_csv(data_filename, index=False)


def parallel_write_b1_effect_data():

	for game in games:

		spe_d = get_spe_dict(transition, str(game), b1_list, eps)

		for game_transition_dynamics in transitions:
			game.set_game_transition_dynamics(game_transition_dynamics)

			# set game, host strategy
			host_strat = (params_dict["eps"],) *  game.strat_len

			params_dict["game"] = game
			params_dict["host"] = host_strat

			# store b1-effect runs over strat + transition space
			#strat_transition_dynamics = []
			#data_filename = data_folder + str(game) + ".csv"


			game_str, strat_str, transition_str = str(game), game.strat_str(), game.transition_str()

			jobs = []

			for run_id in range(num_runs):

				# start the process
				p = mp.Process(target=do_run, args=(run_id, data_folder, game_str, strat_str, transition_str, num_timesteps, b1_list, params_dict, spe_d)) 

				#p = threading.Thread(target=do_run, args=(run_id, data_folder, game_str, strat_str, transition_str, num_timesteps, b1_list, params_dict, spe_d)) 
				p.start()
				# keep track of process, to wait for it later
				jobs.append(p)
			# wait until all jobs done
			for p in jobs:
				p.join()

  

			# for run in range(num_runs):

			# 	data_filename = data_folder + game_str + "_run_{:d}".format(run) + ".csv"

			# 	# announce what we are calculating
			# 	print("Game: {:s}, Run: {:d}".format(str(game), run))
				
			# 	# get data
			# 	start_time = time.time()
			# 	g1_cc_avgs, g2_cc_avgs, g1_game_avgs, player_c_avgs, spe_avgs  = \
			# 		get_b1_evolution_data(num_timesteps, b1_list, params_dict, spe_d)
				
			# 	elapsed_time = time.time() - start_time

			# 	print("Elapsed Time: {:.2f} min".format(elapsed_time/60.0))

			# 	df = pd.DataFrame(np.column_stack([b1_list, g1_cc_avgs, g2_cc_avgs, g1_game_avgs, player_c_avgs, spe_avgs]), 
	  #                              columns=['b1', '1CC rate', '2CC rate', 'Game 1 rate', 'C rate', 'SPE rate'])

			# 	df['strat']       = game_str
			# 	df['strat_space'] = strat_str
			# 	df['transition']  = transition_str

			# 	df.to_csv(data_filename, index=False)

				#strat_transition_dynamics.append(df)

			# turn list into df that holds all the runs for a particular strat + transition dynamics	
			#strat_transition_dynamics = pd.concat(strat_transition_dynamics)
			#strat_transition_dynamics.to_csv(data_filename, index=False)


parallel_write_b1_effect_data()
