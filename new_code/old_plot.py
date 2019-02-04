def get_avg_b1_effect_data():
	data = [None] * len(games)

	eps, beta = get_params(["eps", "beta"], params_dict)

	for index, game in enumerate(games):

		b1_list, g1_cc_avgs, g2_cc_avgs, g1_game_avgs = None, None, None, None

		# take avg over all the runs
		for run in range(num_runs):

			# file where to save data
			filename = get_filename(str(game), run)
			#print("filename", filename) #print("\n")

			# read data
			b1_list, round_g1_cc_avgs, round_g2_cc_avgs, round_g1_game_avgs = \
				np.loadtxt(filename, delimiter=',')

			if g1_cc_avgs is None:
				g1_cc_avgs = round_g1_cc_avgs/(float(num_runs))
				g2_cc_avgs = round_g2_cc_avgs/(float(num_runs))
				g1_game_avgs = round_g1_game_avgs/(float(num_runs))
			else:
				g1_cc_avgs += round_g1_cc_avgs/(float(num_runs))
				g2_cc_avgs += round_g2_cc_avgs/(float(num_runs))
				g1_game_avgs += round_g1_game_avgs/(float(num_runs))


		# store this game's data
		data[index] = (b1_list, g1_cc_avgs, g2_cc_avgs, g1_game_avgs)


	return data


def plot_all_b1_effect_data():

	# recover data
	(s_2_data, s_4_data, s_8_data, s_12_data, s_16_data) = get_avg_b1_effect_data()

	s_2_b1_list,  s_2_g1_cc_avgs, s_2_g2_cc_avgs, s_2_g1_game_avgs = s_2_data
	s_4_b1_list,  s_4_g1_cc_avgs, s_4_g2_cc_avgs, s_4_g1_game_avgs = s_4_data
	s_8_b1_list,  s_8_g1_cc_avgs, s_8_g2_cc_avgs, s_8_g1_game_avgs = s_8_data
	s_12_b1_list,  s_12_g1_cc_avgs, s_12_g2_cc_avgs, s_12_g1_game_avgs = s_12_data
	s_16_b1_list,  s_16_g1_cc_avgs, s_16_g2_cc_avgs, s_16_g1_game_avgs = s_16_data

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