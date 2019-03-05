import numpy as np
import time

from class_two_games import S_8_Game, S_12_Game, S_16_Game
from find_spe_functions import *

import pathlib # create directory as needed

from helper_functions import save_dict, read_dict

# Parameters
c=1.00
b2=1.20

transitions = [
	#"EqualSay_G1_Default",
	#"Random_Dictator",
	#"Player1_Dictator",
	"EqualSay_G2_Default",
    #"EqualSay_G1_Default",
    #"Player1_Dictator",
    #"Random",
]

transition = transitions[0]

# 1.0 - 10**(-2) = 0.99 -> exponent = num decimal places
delta = 1.0 - 10**(-5)
S08_game  = S_8_Game(c=c,   b1=1.8, b2=b2, game_transition_dynamics=transition)
S12_game = S_12_Game(c=c,  b1=1.8, b2=b2, game_transition_dynamics=transition)
S16_game = S_16_Game(c=c,  b1=1.8, b2=b2, game_transition_dynamics=transition)

games = [S08_game, S12_game, S16_game]

s_08_strat = (1,0,0,1, 1,0,0,0)
s_12_strat = (1,0,0,0, 0,0,0,1, 1,0,0,0)

v_s08 = S08_game.get_stationary_dist(S08_game.get_f(), s_08_strat, s_08_strat)
v_s12 = S12_game.get_stationary_dist(S12_game.get_f(), s_12_strat, s_12_strat)

print("v_s08: ", v_s08[0])
print("v_s12: ", v_s12[0])

s_08_strat_allc = (1,1,1,1, 0,0,0,0)
s_08_strat_alld = (0,0,0,0, 0,0,0,0)

v_s08_allcd = S08_game.get_stationary_dist(S08_game.get_f(), s_08_strat_allc, s_08_strat_alld)
v_s08_alldc = S08_game.get_stationary_dist(S08_game.get_f(), s_08_strat_alld, s_08_strat_allc)


print("v_s08 ALLC vs ALLD: ", tuple(round(x,2) for x in v_s08_allcd))
print("v_s08 ALLD vs ALLC: ", tuple(round(x,2) for x in v_s08_alldc))

def epss_it(eps, lst):
	return tuple(eps + (1-2*eps) * x for x in lst)

epss = 0.001
s_08_strat = epss_it(epss, (1,0,0,1, 1,0,0,0))
s_12_strat = epss_it(epss, (1,0,0,0, 0,0,0,1, 1,0,0,0))

v_s08 = S08_game.get_stationary_dist(S08_game.get_f(), s_08_strat, s_08_strat)
v_s12 = S12_game.get_stationary_dist(S12_game.get_f(), s_12_strat, s_12_strat)

print("eps v_s08: ", tuple(round(x,2) for x in v_s08))
print("eps v_s12: ", tuple(round(x,2) for x in v_s12))

folder_timestamp = time.strftime("date_%Y_%m_%d_%H_%M_%S")
params_str = "c_{:.2f}_b2_{:.2f}_delta_{:.10f}".format(c, b2, delta)

#b1_list = np.arange(1.0, 3.2, 0.14)


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

#run(b1_list)