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

#from test_parameters import *

# set folder name
folder_timestamp = time.strftime("date_%Y_%m_%d_%H_%M_%S")

data_folder = get_folder(folder_timestamp, directory="data/b1_effect")
img_folder  = get_folder(folder_timestamp, directory="imgs/b1_effect")

print("\nData Folder: {:s}\n".format(data_folder))


#b1_list = np.arange(1.0, 3.2, 0.56)

b1_list = np.arange(1.0, 3.2, 0.14)


games   = [
			#S_2_Game(c=1.0, b1=1.2), 
			#S_4_Game(c=1.0, b1=2.0), 
			S_8_Game(c=1.0, b1=2.0, b2=1.2,  game_transition_dynamics=transitions[0]), 
			S_12_Game(c=1.0, b1=2.0, b2=1.2, game_transition_dynamics=transitions[0]), 
			S_16_Game(c=1.0, b1=2.0, b2=1.2, game_transition_dynamics=transitions[0]), 
		]


def write_b1_effect_data():

	for game in games:

		for game_transition_dynamics in transitions:
			game.set_game_transition_dynamics(game_transition_dynamics)

			# set game, host strategy
			host_strat = (params_dict["eps"],) *  game.strat_len

			params_dict["game"] = game
			params_dict["host"] = host_strat

			# store b1-effect runs over strat + transition space
			strat_transition_dynamics = []
			data_filename = data_folder + str(game) + ".csv"

			for run in range(num_runs):

				# announce what we are calculating
				print("Game: {:s}, Run: {:d}".format(str(game), run))
				
				# get data
				start_time = time.time()
				g1_cc_avgs, g2_cc_avgs, g1_game_avgs = get_b1_evolution_data(num_timesteps, b1_list, params_dict)
				elapsed_time = time.time() - start_time

				print("Elapsed Time: {:.2f} min".format(elapsed_time/60.0))

				df = pd.DataFrame(np.column_stack([b1_list, g1_cc_avgs, g2_cc_avgs, g1_game_avgs]), 
	                               columns=['b1', '1CC rate', '2CC rate', 'Game 1 rate'])

				df['strat']       = str(game)
				df['strat_space'] = game.strat_str()
				df['transition']  = game.transition_str()

				strat_transition_dynamics.append(df)

			# turn list into df that holds all the runs for a particular strat + transition dynamics	
			strat_transition_dynamics = pd.concat(strat_transition_dynamics)
			strat_transition_dynamics.to_csv(data_filename, index=False)


def plot_b1_effect_data():

	sns.set(style="darkgrid", palette="pastel")

	# Load the example tips dataset
	data = pd.read_csv(folder + "all_df.csv")

	g = sns.lineplot(x="b1", y="1CC rate", hue="strat",
             data=data)

	g.set_title('Effect of b1 on Cooperation')
	g.set_xlabel("b1 value (b2 = 1.2, c1 = c2 = 1.0)")

	plt.tight_layout()
	plt.savefig("imgs/b1_effect/1cc.eps", format='eps', dpi=1000)

	plt.show()

def plot_all_b1_effect_data():

	data_folder = "data/b1_effect/long_time_two_game/eps_1.00e-03_beta_2.00e+00_T_3.00e+05_c_1.00_b2_1.20/date_2019_02_05/"
	data_filename = "all_two_game_df.csv"
	# seaborn data
	sns.set(style="darkgrid", palette="pastel")
	data = pd.read_csv(data_folder + data_filename)

	# parameters
	eps, beta = get_params(["eps", "beta"], params_dict)

	eps = r"$\epsilon$"  + " = {:2.2e}\n ".format(eps)
	beta = r"$\beta$"    + " = {:2.2e}\n ".format(beta)
	ts = r"$T$"             + " = {:2.2e}".format(num_timesteps)

	game_param = "b2 = {:.2f}\nc1 = c2 = {:.2f}".format(b2, c1)
	sep = "\n\n"
	param_str = "Evolution Parameters:\n " + eps + beta + ts + sep + \
				"Game Parameters:\n"  + game_param + sep + \
				"{:d} Runs".format(num_runs)

	
	# plot CC data
	fig, ((ax1, ax2, ax3, ax4)) = plt.subplots(nrows=1, ncols=4, figsize = (24,6))
													# sharex='col', sharey='row',
													 

	ax4.text(0.5, 0.5, param_str, horizontalalignment='center',
            fontsize=12, multialignment='left',
            bbox=dict(boxstyle="round", facecolor='#D8D8D8',
            ec="0.5", pad=0.5, alpha=1), fontweight='bold')

	ax4.axis('off')


	super_title = "Effect of b1 on the Evolution of Cooperation"

	fig.suptitle(super_title, fontsize=14, fontweight='bold')

	# axes labels
	ax_xlabel = "b1 value"
	
	ax1_ylabel = "Game 1 Rate"
	ax2_ylabel = "1CC Rate"
	ax3_ylabel = "2CC Rate"

	# lineplots
	game1_g = sns.lineplot(x="b1", y="Game 1 rate", hue="strat", data=data, ax = ax1)
	cc1_g = sns.lineplot(x="b1", y="1CC rate", hue="strat", data=data, ax = ax2)
	cc2_g = sns.lineplot(x="b1", y="2CC rate", hue="strat", data=data, ax = ax3)
	

	# set labels
	game1_g.set_xlabel(ax_xlabel)
	cc1_g.set_xlabel(ax_xlabel)
	cc2_g.set_xlabel(ax_xlabel)
	


	fig.subplots_adjust(hspace=1, wspace=1)
	#plt.tight_layout()

	fig.savefig(img_folder + img_filename, dpi=300)

	plt.show()
