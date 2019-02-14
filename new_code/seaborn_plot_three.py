# import seaborn as sns
# sns.set(style="ticks")
# exercise = sns.load_dataset("exercise")
# g = sns.catplot(x="time", y="pulse", hue="kind", data=exercise)

import matplotlib.pyplot as plt
import seaborn as sns

import pandas as pd
import pathlib


img_folder = "imgs/b1_effect/{:s}/test/".format(transition)
img_filename = "test.png"

# create img directory
pathlib.Path(img_folder).mkdir(parents=True, exist_ok=True) 

print("img folder: ", img_folder)
print("img filename: ", img_filename)

sns.set(style="darkgrid", palette="pastel")

# Load the dataset
folder = "data/b1_effect/{:s}/eps_{:.2e}_beta_{:.2e}_T_{:.2e}_c_{:.2f}_b2_{:.2f}/{:s}/"\
		.format(transition, eps, beta, num_timesteps, c, b2, folder_timestamp)

folder = "data/b1_effect/transition_g1_default/eps_1.00e-03_beta_2.00e+00_T_1.00e+04_c_1.00_b2_1.20/date_2019_02_06_19:11:23/"


#folder_name = "data/b1_effect/long_time_one_game/s_4/eps_1.00e-03_beta_2.00e+00_T_3.00e+05_c_1.00_b2_1.20/date_2019_02_05_20:39:52/"
filename = "S_08_Transition_EqualSay_G1_Default_df.csv"
# folder_name = "data/b1_effect/s_2_high_b1/"
# params = "eps_1.00e-03_beta_2.00e+00_T_3.00e+05_c_1.00_b2_1.20"
# date = "/date_2019_02_05_07:55:47/"


# parameters
num_runs = 1
num_timesteps = 1*(10**4)

params_dict = {
	"N": 100,
	"eps": 0.001,
	"beta": 2.0,
	"strategy_type": "pure", # or "stochastic"
}


c = 1.0
b2 = 1.2

c1 = c
c2 = c


eps, beta = params_dict["eps"], params_dict["beta"]

eps = r"$\epsilon$"  + " = {:2.2e}\n ".format(eps)
beta = r"$\beta$"    + " = {:2.2e}\n ".format(beta)
ts = r"$T$"             + " = {:2.2e}".format(num_timesteps)

game_param = "b2 = {:.2f}\nc1 = c2 = {:.2f}".format(b2, c1)
sep = "\n\n"
param_str = "Evolution Parameters:\n " + eps + beta + ts + sep + \
			"Game Parameters:\n"  + game_param + sep + \
			"{:d} Runs".format(num_runs)


#filename = folder_name + params + date

#data = pd.read_csv(filename + "all_one_game_df.csv")

data = pd.read_csv(folder + filename)

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
