import numpy as np
import time

from class_two_games import S_8_Game, S_12_Game, S_16_Game
from find_spe_functions import *

import pathlib # create directory as needed

# Parameters
c=1.00
b1=1.61
b2=1.20

# 1.0 - 10**(-2) = 0.99 -> exponent = num decimal places
delta = 1.0 - 10**(-5)
S8_game  = S_8_Game(c,  b1, b2)
S12_game = S_12_Game(c, b1, b2)
S16_game = S_16_Game(c, b1, b2)

folder_timestamp = time.strftime("date_%Y_%m_%d_%H:%M:%S")
params_str = "delta_{:.10f}_c_{:.2f}_b1_{:.2f}_b2_{:.2f}".format(delta, c, b1, b2)

folder = "data/spe/{:s}/{:s}/".format(params_str, folder_timestamp)

# create directory
pathlib.Path(folder).mkdir(parents=True, exist_ok=True) 


def run():

	# print parameters
	print("Parameters: delta = {:.10f}, c={:.2f}, b1 = {:.2f}, b2 = {:.2f}".format(delta, c, b1, b2))

	# S8, all SPE
	start_time = time.time()
	s_8_spe_lst = np.asarray(find_all_spe(S8_game, delta))
	elapsed_time = time.time() - start_time

	print("Elapsed Time: {:.2f} min. S8, find all SPE ({:d})."
			.format(elapsed_time/60.0, len(s_8_spe_lst)))

	# S8, all fully cooperative SPE
	start_time = time.time()
	s_8_full_coop_spe_lst = [strat for strat in s_8_spe_lst if is_full_coop_strat(strat, S8_game)]
	elapsed_time = time.time() - start_time

	print("Elapsed Time: {:.2f} min. S8, all full_coop SPE ({:d})."
			.format(elapsed_time/60.0, len(s_8_full_coop_spe_lst)))


	# S12, all SPE
	start_time = time.time()
	s_12_spe_lst = np.asarray(find_all_spe(S12_game, delta))
	elapsed_time = time.time() - start_time

	print("Elapsed Time: {:.2f} min. S12, find all SPE ({:d})."
			.format(elapsed_time/60.0, len(s_12_spe_lst)))

	# S12, all fully cooperative SPE
	start_time = time.time()
	s_12_full_coop_spe_lst = [strat for strat in s_12_spe_lst if is_full_coop_strat(strat, S12_game)]
	elapsed_time = time.time() - start_time

	print("Elapsed Time: {:.2f} min. S12, all full_coop SPE ({:d})."
			.format(elapsed_time/60.0, len(s_12_full_coop_spe_lst)))

	# S16, all SPE
	start_time = time.time()
	s_16_spe_lst = np.asarray(find_all_spe(S16_game, delta))
	elapsed_time = time.time() - start_time

	print("Elapsed Time: {:.2f} min. S16, find all SPE ({:d})."
		.format(elapsed_time/60.0, len(s_16_spe_lst)))

	# S16, all fully cooperative SPE
	start_time = time.time()
	s_16_full_coop_spe_lst = [strat for strat in s_16_spe_lst if is_full_coop_strat(strat, S16_game)]
	elapsed_time = time.time() - start_time

	print("Elapsed Time: {:.2f} min. S16, all full_coop SPE ({:d})."
		.format(elapsed_time/60.0, len(s_16_full_coop_spe_lst)))

	# save data to file
	names = [
		"S08_all_SPE", "S08_full_coop_SPE", 
		"S12_all_SPE", "S12_full_coop_SPE", 
		"S16_all_SPE", "S16_full_coop_SPE"
	]

	data = [
		s_8_spe_lst, s_8_full_coop_spe_lst, 
		s_12_spe_lst, s_12_full_coop_spe_lst, 
		s_16_spe_lst, s_16_full_coop_spe_lst
	]
	
	for i, lst in enumerate(data):
		filename = folder + names[i] + "_num_strat_{:d}.csv".format(len(lst))

		with open(filename,'ab') as f:
		    np.savetxt(f, lst, fmt="%d", delimiter=",")


run()