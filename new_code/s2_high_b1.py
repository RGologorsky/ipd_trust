import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import time

from class_one_games import S_2_Game, S_4_Game
from class_two_games import S_8_Game, S_12_Game, S_16_Game
from simulation_evolution_avgs import *

import pandas as pd
import pathlib # to create directory if needed

# Parameters
num_runs = 5
num_timesteps = 3*(10**5)

params_dict = {
	"N": 100,
	"eps": 0.001,
	"beta": 2.0,
	"strategy_type": "pure", # or "stochastic"
	"max_attempts": 10**4,
}


c = 1.0
b2 = 1.2

c1 = c
c2 = c

# set folder name
folder_timestamp = time.strftime("date_%Y_%m_%d_%H:%M:%S")
eps, beta = get_params(["eps", "beta"], params_dict)

folder = "data/b1_effect/long_time_one_game/s_4/eps_{:.2e}_beta_{:.2e}_T_{:.2e}_c_{:.2f}_b2_{:.2f}/{:s}/"\
		.format(eps, beta, num_timesteps, c, b2, folder_timestamp)

print("\nFolder: {:s}\n".format(folder))

# create directory
pathlib.Path(folder).mkdir(parents=True, exist_ok=True) 

b1_list = np.arange(1.0, 3.2, 0.14) #[2, 4, 6, 8, 10]

strategy_space = "one_game_s4"


games   = [
			#S_2_Game(c=1.0, b1=1.2), 
			S_4_Game(c=1.0, b1=2.0), 
			#S_8_Game(c=1.0, b1=2.0, b2=1.2), 
			#S_12_Game(c=1.0, b1=2.0, b2=1.2), 
			#S_16_Game(c=1.0, b1=2.0, b2=1.2)
		]



def write_b1_effect_data():

	# get parameters
	eps, beta = get_params(["eps", "beta"], params_dict)

	# store all data in dataframe
	all_game_data = []

	for game in games:

		# dataframe for this game/strategy space
		game_data = []

		# set game, host strategy
		host_strat = (params_dict["eps"],) *  game.strat_len

		params_dict["game"] = game
		params_dict["host"] = host_strat

		for run in range(num_runs):

			# announce what we are calculating
			print("Game: {:s}, Run: {:d}".format(str(game), run))
			
			# get data
			start_time = time.time()
			g1_cc_avgs, g2_cc_avgs, g1_game_avgs = get_b1_evolution_data(num_timesteps, b1_list, params_dict)
			elapsed_time = time.time() - start_time

			print("Elapsed Time: {:.2f} min".format(elapsed_time/60.0))

			# convert later into Pandas Dataframe
			df = pd.DataFrame(np.column_stack([b1_list, g1_cc_avgs, g2_cc_avgs, g1_game_avgs]), 
                               columns=['b1', '1CC rate', '2CC rate', 'Game 1 rate'])

			df['strat'] = str(game)

			game_data.append(df)

		game_data = pd.concat(game_data)
		game_data.to_csv(folder + '{:s}_df.csv'.format(str(game)), index=False)

		all_game_data.append(game_data)

	all_game_data = pd.concat(all_game_data)
	all_game_data.to_csv(folder + "all_" + strategy_space + "_df.csv", index=False)


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

	# seaborn data
	sns.set(style="darkgrid", palette="pastel")
	data = pd.read_csv(folder + "all_df.csv")

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
	
	ax1_ylabel = "1CC Rate"
	ax2_ylabel = "2CC Rate"
	ax3_ylabel = "Game 1 Rate"

	# lineplots
	cc1_g = sns.lineplot(x="b1", y="1CC rate", hue="strat", data=data, ax = ax1)
	cc2_g = sns.lineplot(x="b1", y="2CC rate", hue="strat", data=data, ax = ax2)
	game1_g = sns.lineplot(x="b1", y="Game 1 rate", hue="strat", data=data, ax = ax3)

	# set labels
	cc1_g.set_xlabel(ax_xlabel)
	cc2_g.set_xlabel(ax_xlabel)
	game1_g.set_xlabel(ax_xlabel)


	fig.subplots_adjust(hspace=1, wspace=1)
	#plt.tight_layout()

	fig.savefig("imgs/b1_effect/all.eps", format='eps', dpi=1000)

	plt.show()

write_b1_effect_data()
