import numpy as np
import time

from class_two_games import S_8_Game, S_12_Game, S_16_Game
from find_spe_functions import *

import pathlib # create directory as needed

from helper_functions import save_dict, read_dict

# Parameters
c=1.00
b2=1.20


transition = "NA"

# 1.0 - 10**(-2) = 0.99 -> exponent = num decimal places
delta = 1.0 - 10**(-5)
S4_game  = S_8_Game(c=c,   b1=1.8)

folder_timestamp = time.strftime("date_%Y_%m_%d_%H_%M_%S")
params_str = "c_{:.2f}_b2_{:.2f}_delta_{:.10f}".format(c, b2, delta)

b1_list = np.arange(1.0, 3.2, 0.14)


def run_dict(b1_list):
	d = {}

	parent_folder = "data/full_coop_spe/dict/{:s}/"\
						.format(params_str)

	# create directory
	pathlib.Path(parent_folder).mkdir(parents=True, exist_ok=True) 


	print("Parent folder: ", parent_folder)

	# print parameters
	print("Parameters: delta = {:.10f}, c={:.2f}, b2 = {:.2f}".format(delta, c, b2))

	for game in games:

		game_str = str(game)
		d[game_str] = {}

		print("game = {:s}".format(game_str))
	
		for b1 in b1_list:

			print("b1 = {:.2f}".format(b1))

			# reset b1 value
			game.reset_b1(b1)

			# remember spe list for this game and b1 value
			d[game_str][b1] = find_all_coop_spe(game, delta, transition)

	
	filename = parent_folder + transition + "_spe_dict"
	save_dict(d, filename)

#run_dict(b1_list)

def run(b1_list):
	parent_folder = "data/full_coop_spe/transitions/{:s}/{:s}/{:s}/"\
						.format(transition, params_str, folder_timestamp)

	print("Parent folder: ", parent_folder)

	# print parameters
	print("Parameters: delta = {:.10f}, c={:.2f}, b2 = {:.2f}".format(delta, c, b2))

	for game in games:

		print("game = {:s}".format(str(game)))
	
		folder = parent_folder + "{:s}/".format(str(game))

		# create directory
		pathlib.Path(folder).mkdir(parents=True, exist_ok=True) 

		for b1 in b1_list:

			print("b1 = {:.2f}".format(b1))

			# reset b1 value
			game.reset_b1(b1)

			# time it
			start_time = time.time()
			full_coop_spe_lst = find_all_coop_spe(game, delta, transition)
			elapsed_time = time.time() - start_time

			print("Elapsed Time: {:.2f} min. {:s}, find all coop SPE ({:d})."
					.format(elapsed_time/60.0, str(game), len(full_coop_spe_lst)))

			# filename = folder + "b1_{:.2f}_num_strat_{:d}.csv".format(b1, len(full_coop_spe_lst))
			filename = folder + "b1_{:.2f}.csv".format(b1)

			with open(filename,'ab') as f:
			    np.savetxt(f, full_coop_spe_lst, fmt="%d", delimiter=",")

run(b1_list)