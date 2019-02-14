import time
from pathlib import Path
import os

#from class_one_games import S_2_Game, S_4_Game
from class_two_games import S_8_Game, S_12_Game, S_16_Game
from simulation_evolution_avgs import *


# Parameters
num_runs = 5
num_timesteps_list = [2*10**5, 3*10**5]

params_dict = {
	"N": 100,
	"eps": 0.001,
	"beta": 2.0,
	"strategy_type": "pure", # or "stochastic"
}

# set folder name
eps, beta = get_params(["eps", "beta"], params_dict)
folder_timestamp = time.strftime("date_%Y_%m_%d")
folder = "data/num_timesteps/runs_{:d}_eps_{:.2e}_beta_{:.2e}/{:s}/".format(num_runs, eps, beta, folder_timestamp)

print("\nFolder: {:s}\n".format(folder))

b1_list = [1.8]

b1 = 1.8

c = 1.0
b2 = 1.2

#np.arange(1.0, 3.2, 0.14)
# games   = [
# 			S_4_Game(c=1.0, b1=2.0), 
# 			S_12_Game(c=1.0, b1=2.0, b2=1.2), S_16_Game(c=1.0, b1=2.0, b2=1.2)
# 		]
games   = [
			S_8_Game(c, b1, b2), S_12_Game(c, b1, b2), S_16_Game(c, b1, b2)
		]


def get_filepath(game_str, eps, beta, num_timesteps):
	params_str = "{:s}_T_{:.2e}".format(game_str, num_timesteps)
	filepath = folder + params_str + ".csv"
	return filepath		


def write_b1_effect_data():

	eps, beta = get_params(["eps", "beta"], params_dict)

	for num_timesteps in num_timesteps_list:

		for game in games:

			# file where to save data
			filepath = get_filepath(str(game), eps, beta, num_timesteps)

			# check if already data already calculated
			my_file = Path(filepath)
			
			try:

				if my_file.is_file():
					print("Already done")
					continue

				else:
					os.makedirs(os.path.dirname(filepath), exist_ok=True)
			except:
				os.makedirs(os.path.dirname(filepath), exist_ok=True)

			# set game, host strategy
			host_strat = (params_dict["eps"],) *  game.strat_len

			params_dict["game"] = game
			params_dict["host"] = host_strat

			# announce what we are calculating
			print("Game: {:s}, Num Timesteps: {:.2e}".format(str(game), num_timesteps))

			start_time = time.time()
			sampled_cc_avgs = [get_evolution_avgs(num_timesteps, params_dict)[0] 
						   for _ in range(num_runs)]
			elapsed_time = time.time() - start_time

			print("Elapsed Time: {:.2f} min".format(elapsed_time/60.0))

			# get statistics
			mean, sample_sd, string_description = get_sample_statistics(sampled_cc_avgs)
			print(string_description, "\n")

			# # file where to save data
			# filepath = get_filepath(str(game), eps, beta, num_timesteps)

			# save data
			with open(filepath,'ab') as f:
				    np.savetxt(f, sampled_cc_avgs, delimiter=",")

	print("Done.")

write_b1_effect_data()