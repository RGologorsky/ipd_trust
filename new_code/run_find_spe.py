import numpy as np
import time

from class_two_games import S_8_Game, S_12_Game, S_16_Game
from find_spe_functions import *

import pathlib # create directory as needed

# Parameters
c=1.00
b1=1.61
b2=1.20

transitions = [
	#"EqualSay_G1_Default",
	#"Random_Dictator",
	#"Player1_Dictator",
	#"EqualSay_G2_Default",
    "EqualSay_G1_Default",
    #"Player1_Dictator",
    #"Random_Dictator",
]

transition = transitions[0]

# 1.0 - 10**(-2) = 0.99 -> exponent = num decimal places
delta = 1.0 - 10**(-5)
S8_game  = S_8_Game(c,  b1, b2, game_transition_dynamics=transitions[0])
S12_game = S_12_Game(c, b1, b2, game_transition_dynamics=transitions[0])
S16_game = S_16_Game(c, b1, b2, game_transition_dynamics=transitions[0])

games = [S8_game, S12_game, S16_game]

folder_timestamp = time.strftime("date_%Y_%m_%d_%H_%M_%S")
params_str = "delta_{:.10f}_c_{:.2f}_b1_{:.2f}_b2_{:.2f}".format(delta, c, b1, b2)

folder = "data/full_coop_spe/transitions/{:s}/{:s}/{:s}/".format(transition, params_str, folder_timestamp)

# create directory
pathlib.Path(folder).mkdir(parents=True, exist_ok=True) 


def run():

	# print folder
	print(folder)

	# print parameters
	print("Parameters: delta = {:.10f}, c={:.2f}, b1 = {:.2f}, b2 = {:.2f}".format(delta, c, b1, b2))

	for game in games:
		for game_transition_dynamics in transitions:

			# set transition dyamics
			game.set_game_transition_dynamics(game_transition_dynamics)

			
			# S8, all SPE
			start_time = time.time()
			spe_lst = np.asarray(find_all_spe(game, delta))
			full_coop_spe_lst = [strat for strat in spe_lst if is_full_coop_strat(strat, game)]
			elapsed_time = time.time() - start_time

			print("Elapsed Time: {:.2f} min. {:s}, find all coop SPE ({:d})."
					.format(elapsed_time/60.0, str(game), len(full_coop_spe_lst)))

			filename = folder + "{:s}_num_strat_{:d}.csv".format(str(game), len(full_coop_spe_lst))

			with open(filename,'ab') as f:
			    np.savetxt(f, full_coop_spe_lst, fmt="%d", delimiter=",")

run()