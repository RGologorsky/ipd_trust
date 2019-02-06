# import seaborn as sns
# sns.set(style="ticks")
# exercise = sns.load_dataset("exercise")
# g = sns.catplot(x="time", y="pulse", hue="kind", data=exercise)

import matplotlib.pyplot as plt
import seaborn as sns

import numpy as np
import pandas as pd
import pathlib # to create directory if needed

img_folder = "imgs/num_timesteps/"
img_filename = "1cc_convergence.png"
	
# create img directory
pathlib.Path(img_folder).mkdir(parents=True, exist_ok=True) 


# plot CC data
fig, ax = plt.subplots(nrows=1, ncols=1)
													# sharex='col', sharey='row',
						
# make seaborn graph
sns.set(style="ticks", palette="pastel")

# Load dataset
data = pd.read_csv("data/num_timesteps/runs_5_eps_1.00e-03_beta_2.00e+00/date_2019_02_03/data_num_timesteps.csv")


# Draw a nested boxplot to show bills by day and time
ts = "No. Timesteps"
strat = "Strat"

g = sns.boxplot(x=strat, y="1CC rate", 
			hue=ts, data=data, ax = ax, showmeans=True)


m1 = data.groupby([strat, ts])['1CC rate'].median().values
mL1 = [str(np.round(s, 2)) for s in m1]

means = data.groupby([strat, ts])['1CC rate'].mean().values
stds = data.groupby([strat, ts])['1CC rate'].std().values

#str_means = ["{:.2f}".format(s) for s in means]
#str_stds  = ["{:.2f}".format(s) for s in stds]

str_labels = ["{:.2f}".format(means[i]) + r"$\pm$" + "{:.2f}".format(stds[i]) for i in range(len(means))]
# for patch in ax.patches:
# 	print("width ", patch.get_width())

# width = ax.patches[0].get_width()
# print("patch width: ", width)

ind = 0
nudge = 1.0/6.0
up_nudge = 0.005
side_nudge = 2.0/3.0 * nudge

for tick in range(len(g.get_xticklabels())):
	#g.text(tick+  -3*nudge + side_nudge, m1[ind+0]+ up_nudge, mL1[ind+0], horizontalalignment='center', color='black', weight='semibold', fontsize="8")
	#g.text(tick+  -2*nudge + side_nudge, m1[ind+1]+ up_nudge, mL1[ind+1], horizontalalignment='center', color='black', weight='semibold', fontsize="8")
	#g.text(tick+  -1*nudge + side_nudge, m1[ind+2]+ up_nudge, mL1[ind+2], horizontalalignment='center', color='black', weight='semibold', fontsize="8")
	#g.text(tick+   1*nudge - side_nudge, m1[ind+3]+ up_nudge, mL1[ind+3], horizontalalignment='center', color='black', weight='semibold', fontsize="8")
	# g.text(tick+   2*nudge - side_nudge, m1[ind+4]+ up_nudge, mL1[ind+4],  horizontalalignment='center', color='black', weight='semibold', fontsize="8")
	# g.text(tick+   3*nudge - side_nudge, m1[ind+5]+ up_nudge, mL1[ind+5],  horizontalalignment='center', color='black', weight='semibold', fontsize="8")
	g.text(tick+2*nudge - side_nudge, means[ind+4]+up_nudge, str_labels[ind+4],  horizontalalignment='center', color='black', weight='semibold', fontsize="8")
	g.text(tick+3*nudge - side_nudge, means[ind+5]+up_nudge, str_labels[ind+5],  horizontalalignment='center', color='black', weight='semibold', fontsize="8")
    

	ind += 6

# g = sns.stripplot(x=strat, y="1CC rate", hue=ts,
#                     data=data, jitter=True,
#                     palette="Set2", dodge=True)

# medians = data.groupby([strat])['1CC rate'].median().values
# median_labels = [str(np.round(s, 2)) for s in medians]


# pos = range(len(medians))
# for tick,label in zip(pos,ax.get_xticklabels()):
# 	print("label ", label)
# 	print("medians", median_labels[tick])

# 	ax.text(pos[tick], medians[tick] + 0.5, median_labels[tick], 
# 		horizontalalignment='center', size='x-small', color='b', weight='semibold')


#handles, labels = ax1.get_legend_handles_labels()

#sns.despine(offset=10)
ax.set_title('How many timesteps until the Cooperation Rate converges?')
ax.set_xlabel("Strategy Space")

# my_labels = ['1.00e+03', '1.00e+04', '1.00e+05', '2.00e+05', '3.00e+05', '1.00e+06']
# g.legend(handles=handles, loc='upper right', bbox_to_anchor=(1.25, 0.5), ncol=1, labels=my_labels, title="No. Timesteps")
# g._legend(loc='upper right', bbox_to_anchor=(1.25, 0.5), ncol=1)

# g._legend.set_title('No. Timesteps')
# my_labels = ['1.00e+03', '1.00e+04', '1.00e+05', '2.00e+05', '3.00e+05', '1.00e+06']


#ax.legend(loc='lower right') #, labels = my_labels)

# Put a legend to the right side
#ax1.legend(handles=[leg], loc='upper right', bbox_to_anchor=(1.25, 0.5), ncol=1)



# for t, l in zip(g._legend.texts, my_labels):
# 	print("t is ", t, "l is ", l) 
# 	t.set_text(l)

# print("t", g._legend.texts)

plt.tight_layout()
plt.savefig(img_folder + img_filename, dpi=300)

plt.show()

# import numpy as np
# import matplotlib.pyplot as plt
# import seaborn as sns
# import time

# from class_one_games import S_2_Game, S_4_Game
# from class_two_games import S_8_Game, S_12_Game, S_16_Game
# from simulation_evolution_avgs import *

# import pandas as pd
# import pathlib # to create directory if needed

# # Parameters
# num_runs = 5
# num_timesteps = 3*(10**5)

# params_dict = {
# 	"N": 100,
# 	"eps": 0.001,
# 	"beta": 2.0,
# 	"strategy_type": "pure", # or "stochastic"
# 	"max_attempts": 10**4,
# }


# c = 1.0
# b2 = 1.2

# c1 = c
# c2 = c

# folder = "data/b1_effect/long_time_two_game/eps_1.00e-03_beta_2.00e+00_T_3.00e+05_c_1.00_b2_1.20/date_2019_02_05/"
# filename = "S_08_df.csv"

# img_folder = "imgs/b1_effect/long_time/"
# img_filename = "S_08.png"
	
# # create img directory
# pathlib.Path(img_folder).mkdir(parents=True, exist_ok=True) 

# def plot_one_b1_effect_data():

# 	# seaborn data
# 	sns.set(style="darkgrid", palette="pastel")
# 	data = pd.read_csv(folder + filename)

# 	# parameters
# 	eps, beta = get_params(["eps", "beta"], params_dict)

# 	eps = r"$\epsilon$"  + " = {:2.2e}\n ".format(eps)
# 	beta = r"$\beta$"    + " = {:2.2e}\n ".format(beta)
# 	ts = r"$T$"             + " = {:2.2e}".format(num_timesteps)

# 	game_param = "b2 = {:.2f}\nc1 = c2 = {:.2f}".format(b2, c1)
# 	sep = "\n\n"
# 	param_str = "Evolution Parameters:\n " + eps + beta + ts + sep + \
# 				"Game Parameters:\n"  + game_param + sep + \
# 				"{:d} Runs".format(num_runs)

	
# 	# plot CC data
# 	fig, ((ax1, ax2, ax3, ax4)) = plt.subplots(nrows=1, ncols=4, figsize = (24,6))
# 													# sharex='col', sharey='row',
													 

# 	ax4.text(0.5, 0.5, param_str, horizontalalignment='center',
#             fontsize=12, multialignment='left',
#             bbox=dict(boxstyle="round", facecolor='#D8D8D8',
#             ec="0.5", pad=0.5, alpha=1), fontweight='bold')

# 	ax4.axis('off')


# 	super_title = "Effect of b1 on the Evolution of Cooperation"

# 	fig.suptitle(super_title, fontsize=14, fontweight='bold')

# 	# axes labels
# 	ax_xlabel = "b1 value"
	
# 	ax1_ylabel = "Game 1 Rate"
# 	ax2_ylabel = "1CC Rate"
# 	ax3_ylabel = "2CC Rate"

# 	# lineplots
# 	game1_g = sns.lineplot(x="b1", y="Game 1 rate", hue="strat", data=data, ax = ax1)
# 	cc1_g = sns.lineplot(x="b1", y="1CC rate", hue="strat", data=data, ax = ax2)
# 	cc2_g = sns.lineplot(x="b1", y="2CC rate", hue="strat", data=data, ax = ax3)
	
# 	# set labels
# 	cc1_g.set_xlabel(ax_xlabel)
# 	cc2_g.set_xlabel(ax_xlabel)
# 	game1_g.set_xlabel(ax_xlabel)


# 	fig.subplots_adjust(hspace=1, wspace=1)
# 	#plt.tight_layout()


# 	fig.savefig(img_folder + img_filename, dpi=300)

# 	plt.show()

# plot_one_b1_effect_data()
