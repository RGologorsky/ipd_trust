import numpy as np
import matplotlib.pyplot as plt
import time

from class_one_games import S_2_Game, S_4_Game
from class_two_games import S_12_Game, S_16_Game
from simulation_evolution_avgs import *

# add timestamp unique id to avoid overwriting old data
file_timestamp = time.strftime("date_%Y_%m_%d")

# Parameters
num_runs = 4
num_timesteps = 2*(10**5)

params_dict = {
	"N": 100,
	"eps": 0.001,
	"beta": 2.0,
	"strategy_type": "pure", # or "stochastic"
	"max_attempts": 10**4,
}


b1_list = np.arange(1.0, 3.2, 0.14)
# games   = [
# 			S_4_Game(c=1.0, b1=2.0), 
# 			S_12_Game(c=1.0, b1=2.0, b2=1.2), S_16_Game(c=1.0, b1=2.0, b2=1.2)
# 		]
games   = [
			S_2_Game(c=1.0, b1=1.2), S_4_Game(c=1.0, b1=2.0), 
			S_12_Game(c=1.0, b1=2.0, b2=1.2), S_16_Game(c=1.0, b1=2.0, b2=1.2)
		]


def get_filename(game_str, run, eps, beta, num_timesteps):
	#timestamp = time.strftime("date_%Y_%m_%d_time_%H_%M_%S")
	params_str = "game_{:s}_run_{:d}_eps_{:.2e}_beta_{:.2e}_T_{:.2e}_{:s}"\
							.format(game_str, run, eps, beta, num_timesteps, file_timestamp)

	filename = "data/b1_effect_{:s}.csv".format(params_str)
	return filename			


def write_b1_effect_data():

	eps, beta = get_params(["eps", "beta"], params_dict)

	for game in games:

		# set game, host strategy
		host_strat = (params_dict["eps"],) *  game.strat_len

		params_dict["game"] = game
		params_dict["host"] = host_strat

		for run in range(num_runs):

			# announce what we are calculating
			print("Game: {:s}, Run: {:d}".format(str(game), run))
			
			# get data
			start_time = time.time()
			cc_avgs, g1_avgs = get_b1_evolution_data(num_timesteps, b1_list, params_dict)
			elapsed_time = time.time() - start_time

			print("Elapsed Time: {:.2f} min".format(elapsed_time/60.0))

			# file where to save data
			filename = get_filename(str(game), run, eps, beta, num_timesteps)

			# save data
			with open(filename,'ab') as f:
			    np.savetxt(f, (b1_list, cc_avgs, g1_avgs), delimiter=",")


def get_avg_b1_effect_data():
	data = [None] * len(games)

	eps, beta = get_params(["eps", "beta"], params_dict)

	for index, game in enumerate(games):

		b1_list, cc_avgs, g1_avgs = None, None, None

		# take avg over all the runs
		for run in range(num_runs):

			# file where to save data
			filename = get_filename(str(game), run, eps, beta, num_timesteps)
			#print("filename", filename) #print("\n")

			# read data
			b1_list, round_cc_avgs, round_g1_avgs = np.loadtxt(filename, delimiter=',')

			if cc_avgs is None:
				cc_avgs = round_cc_avgs/(float(num_runs))
				g1_avgs = round_g1_avgs/(float(num_runs))
			else:
				cc_avgs += round_cc_avgs/(float(num_runs))
				g1_avgs += round_g1_avgs/(float(num_runs))


		# store this game's data
		data[index] = (b1_list, cc_avgs, g1_avgs)


	return data


def plot_all_b1_effect_data():

	# recover data
	(s_2_data, s_4_data, s_12_data, s_16_data) = get_avg_b1_effect_data()

	s_2_b1_list,  s_2_cc_avgs,  s_2_g1_avgs = s_2_data
	s_4_b1_list,  s_4_cc_avgs,  s_4_g1_avgs = s_4_data
	s_12_b1_list, s_12_cc_avgs, s_12_g1_avgs = s_12_data
	s_16_b1_list, s_16_cc_avgs, s_16_g1_avgs = s_16_data

	# plot CC data
	fig_cc, ((ax1, ax2), (ax3, ax4)) = plt.subplots(nrows=2, ncols=2, 
													# sharex='col', sharey='row',
													 figsize=(12, 12))

	# CC fig
	super_title = "Evolving Cooperation Rates"
	fig_cc.suptitle(super_title, fontsize=14, fontweight='bold')

	# axes labels
	xlabel = "b1/c ratio"
	ylabel = "Cooperation Rate"

	# axis titles
	axis_titles = ["{:s} Evolving Cooperation Rate".format(str(game)) for game in games]

	# parameters
	eps, beta = get_params(["eps", "beta"], params_dict)

	eps = r"$\epsilon$"  + " = {:2.2e}\n ".format(eps)
	beta = r"$\beta$"    + " = {:2.2e}\n ".format(beta)
	ts = r"$T$"             + " = {:2.2e}".format(num_timesteps)

	param_str = "Parameters:\n " + eps + beta + ts + "\n\n" + "Avg over {:d} Runs".format(num_runs)

	plt.subplots_adjust(bottom=0.20, top=0.92)

	plt.figtext(0.5, 0.05, param_str, horizontalalignment='center',
            fontsize=12, multialignment='left',
            bbox=dict(boxstyle="round", facecolor='#D8D8D8',
            ec="0.5", pad=0.5, alpha=1), fontweight='bold')

	# add data
	add_line_plot(ax1, s_2_b1_list, s_2_cc_avgs, xlabel=xlabel, ylabel=ylabel, title=axis_titles[0], text="", point_size=10)
	add_line_plot(ax2, s_4_b1_list, s_4_cc_avgs, xlabel=xlabel, ylabel=ylabel, title=axis_titles[1], text="", point_size=10)
	add_line_plot(ax3, s_12_b1_list, s_12_cc_avgs, xlabel=xlabel, ylabel=ylabel, title=axis_titles[2], text="", point_size=10)
	add_line_plot(ax4, s_16_b1_list, s_16_cc_avgs, xlabel=xlabel, ylabel=ylabel, title=axis_titles[3], text="", point_size=10)

	timestamp = time.strftime("date_%Y_%m_%d_time_%H_%M_%S")
	fig_cc.savefig('imgs/evolving_cc_rates_{:s}.png'.format(timestamp))

	# plot G1 data
	fig_g1, ((ax1, ax2), (ax3, ax4)) = plt.subplots(nrows=2, ncols=2, 
													# sharex='col', sharey='row',
													 figsize=(12, 12))

	# G1 fig
	super_title = "Evolving Game 1 Rates"
	fig_g1.suptitle(super_title, fontsize=14, fontweight='bold')

	# axes labels
	xlabel = "b1/c ratio"
	ylabel = "Game 1 Rate"

	# axis titles
	axis_titles = ["{:s} Evolving Game 1 Rate".format(str(game)) for game in games]


	plt.subplots_adjust(bottom=0.20, top=0.92)

	plt.figtext(0.5, 0.05, param_str, horizontalalignment='center',
            fontsize=12, multialignment='left',
            bbox=dict(boxstyle="round", facecolor='#D8D8D8',
            ec="0.5", pad=0.5, alpha=1), fontweight='bold')

	# add data
	add_line_plot(ax1, s_2_b1_list, s_2_g1_avgs, xlabel=xlabel, ylabel=ylabel, title=axis_titles[0], text="", point_size=10)
	add_line_plot(ax2, s_4_b1_list, s_4_g1_avgs, xlabel=xlabel, ylabel=ylabel, title=axis_titles[1], text="", point_size=10)
	add_line_plot(ax3, s_12_b1_list, s_12_g1_avgs, xlabel=xlabel, ylabel=ylabel, title=axis_titles[2], text="", point_size=10)
	add_line_plot(ax4, s_16_b1_list, s_16_g1_avgs, xlabel=xlabel, ylabel=ylabel, title=axis_titles[3], text="", point_size=10)

	fig_g1.savefig('imgs/evolving_g1_rates_{:s}.png'.format(timestamp))

	print("Done.")