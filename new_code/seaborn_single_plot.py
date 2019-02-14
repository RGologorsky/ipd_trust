# import seaborn as sns
# sns.set(style="ticks")
# exercise = sns.load_dataset("exercise")
# g = sns.catplot(x="time", y="pulse", hue="kind", data=exercise)

import matplotlib.pyplot as plt
import seaborn as sns

import pandas as pd
import pathlib


img_folder = "imgs/test/b1_effect/"
img_filename = "test.png"

# create img directory
pathlib.Path(img_folder).mkdir(parents=True, exist_ok=True) 

print("img folder: ", img_folder)
print("img filename: ", img_filename)

sns.set(style="darkgrid", palette="pastel")

# Load the dataset

folder = "data/b1_effect/eps_1.00e-03_beta_2.00e+00_T_1.00e+04_c_1.00_b2_1.20/date_2019_02_07_21_55_25/"

#"data/b1_effect/transition_g1_default/eps_1.00e-03_beta_2.00e+00_T_1.00e+04_c_1.00_b2_1.20/date_2019_02_06_19:11:23/"
#"data/b1_effect/long_time_one_game/s_4/eps_1.00e-03_beta_2.00e+00_T_3.00e+05_c_1.00_b2_1.20/date_2019_02_05_20:39:52/"

filename = "S_08_Random_Dictator.csv"
#"S_08_Transition_EqualSay_G1_Default_df.csv"
# folder_name = "data/b1_effect/s_2_high_b1/"
# params = "eps_1.00e-03_beta_2.00e+00_T_3.00e+05_c_1.00_b2_1.20"
# date = "/date_2019_02_05_07:55:47/"


#filename = folder_name + params + date

#data = pd.read_csv(filename + "all_one_game_df.csv")

data = pd.read_csv(folder + filename)

fig, ((ax1, ax2)) = plt.subplots(nrows=1, ncols=2, figsize = (12,6))

# seaborn graph
g = sns.lineplot(x="b1", y="1CC rate", ax=ax1, hue="strat", data=data)

#handles, labels = ax1.get_legend_handles_labels()

g.set_title('Effect of b1 on Cooperation Rate')
g.set_xlabel("b1_value")
g.set_ylabel("CC rate")

# parameters
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


eps, beta = params_dict["eps"], params_dict["beta"]

eps = r"$\epsilon$"  + " = {:2.2e}\n ".format(eps)
beta = r"$\beta$"    + " = {:2.2e}\n ".format(beta)
ts = r"$T$"             + " = {:2.2e}".format(num_timesteps)

game_param = "b2 = {:.2f}\nc1 = c2 = {:.2f}".format(b2, c1)
sep = "\n\n"
param_str = "Evolution Parameters:\n " + eps + beta + ts + sep + \
			"Game Parameters:\n"  + game_param + sep + \
			"{:d} Runs".format(num_runs)


#plt.subplots_adjust(bottom=0.20, top=0.92)

ax2.text(0.5, 0.5, param_str, horizontalalignment='center',
            fontsize=12, multialignment='left',
            bbox=dict(boxstyle="round", facecolor='#D8D8D8',
            ec="0.5", pad=0.5, alpha=1), fontweight='bold')

ax2.axis('off')
#plt.tight_layout()
plt.savefig(img_folder + img_filename, dpi=300)

plt.show()

# Game: S_02, Run: 0
# Elapsed Time: 14.08 min
# Game: S_02, Run: 1
# Elapsed Time: 21.87 min
# Game: S_02, Run: 2
# Elapsed Time: 25.33 min
# Game: S_02, Run: 3
# Elapsed Time: 20.50 min
# Game: S_02, Run: 4
# Elapsed Time: 19.79 min