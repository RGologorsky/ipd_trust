import numpy as np
import time

from class_two_games import S_12_Game, S_16_Game
from find_spe import *

# Parameters
c=1.00
b1=1.61
b2=1.20

delta = 0.999
S12_game = S_12_Game(c, b1, b2)
S16_game = S_16_Game(c, b1, b2)

def run():

	# print parameters
	print("Parameters: delta = {:.3f}, c={:.2f}, b1 = {:.2f}, b2 = {:.2f}".format(delta, c, b1, b2))

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
	prefix, suffix = "spe/", ".csv"
	params_str = "_delta_{:.3f}_c_{:.2f}_b1_{:.2f}_b2_{:.2f}".format(delta, c, b1, b2)
	names = ["S12_all_SPE", "S12_full_coop_SPE", "S16_all_SPE", "S16_full_coop_SPE"]
	data = [s_12_spe_lst, s_12_full_coop_spe_lst, s_16_spe_lst, s_16_full_coop_spe_lst]
	for i, lst in enumerate(data):
		filename = prefix + names[i] + params_str + "_num_strat_{:d}".format(len(lst)) + suffix

		with open(filename,'ab') as f:
		    np.savetxt(f, lst, fmt="%d", delimiter=",")


run()