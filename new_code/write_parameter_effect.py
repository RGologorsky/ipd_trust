import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import time

from class_one_games import S_2_Game, S_4_Game
from class_two_games import S_8_Game, S_12_Game, S_16_Game
from simulation_evolution_avgs import *

import pandas as pd
import pathlib # to create directory if needed

from parameters import *
from helper_functions import save_dict, read_dict

param_to_change, param_list = ("N", [8, 16])

b1_list = np.arange(1.0, 3.2, 0.14)
game    = S_12_Game(c=c, b1=1.8, b2=b2, game_transition_dynamics="EqualSay_G2_Default")


# define folder name
folder_timestamp = time.strftime("date_%Y_%m_%d_%H_%M_%S")
subfolder = "param_effect/{:s}/{:s}/".format(param_to_change, folder_timestamp)

data_folder = "data/{:s}".format(subfolder)
img_folder  = data_folder

def save_params(folder, params_filename="params"):
	# create directory
	pathlib.Path(folder).mkdir(parents=True, exist_ok=True) 

	dict_to_save = {key: val for key, val in save_params_dict.items()}
	dict_to_save["game"] = str(game)
	
	save_dict(dict_to_save, params_filename)

save_params(folder=data_folder)

print("\nData Folder: {:s}\n".format(data_folder))


# filenames within folder
def get_filename(param_value):
	return "{:s}{:s}_{:s}.csv".format(data_folder, param_to_change, str(param_value))

def write_param_effect_data():

	params_dict["game"] = game

	for param_value in param_list:
		params_dict[param_to_change] = param_value

		# set game, host strategy
		host_strat = (params_dict["eps"],) *  game.strat_len
		params_dict["host"] = host_strat

		# store b1-effect runs over param space
		param_dynamics = []
		data_filename = get_filename(param_value)

		for run in range(num_runs):

			# announce what we are calculating
			print("{:s} = {:s}, Run: {:d}".format(param_to_change, str(param_value), run))
			
			# get data
			start_time = time.time()
			g1_cc_avgs, g2_cc_avgs, g1_game_avgs = get_b1_evolution_data(num_timesteps, b1_list, params_dict)
			elapsed_time = time.time() - start_time

			print("Elapsed Time: {:.2f} min".format(elapsed_time/60.0))

			df = pd.DataFrame(np.column_stack([b1_list, g1_cc_avgs, g2_cc_avgs, g1_game_avgs]), 
                               columns=['b1', '1CC rate', '2CC rate', 'Game 1 rate'])

			df['CC rate'] = df['1CC rate'] + df['2CC rate']

			df['strat']       = str(game)
			df['strat_space'] = game.strat_str()
			df['transition']  = game.transition_str()
			df['N'] = param_value
			df['eps'] = params_dict["eps"]
			df['beta'] = params_dict["beta"]


			param_dynamics.append(df)

		# turn list into df that holds all the runs for a particular strat + transition dynamics	
		param_dynamics = pd.concat(param_dynamics)
		param_dynamics.to_csv(data_filename, index=False)


write_param_effect_data()