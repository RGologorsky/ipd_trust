# import seaborn as sns
# sns.set(style="ticks")
# exercise = sns.load_dataset("exercise")
# g = sns.catplot(x="time", y="pulse", hue="kind", data=exercise)

import matplotlib.pyplot as plt
import seaborn as sns

import pandas as pd
import pathlib


date = "date_2019_03_04_08_03_01" #date_2019_02_24_19_50_14"
strat_space = "S_12"
transition = "EqualSay_G2_Default"

data_filename =  "all.csv"

# Parameters
N, eps, beta = 100, 0.01, 10.0
num_timesteps = 10*(10**5)
c,  b2 = 1.0, 1.2


params = "eps_{:.2e}_beta_{:.2e}_T_{:.2e}_c_{:.2f}_b2_{:.2f}/{:s}/"\
		.format(eps, beta, num_timesteps, c, b2, date)

data_folder   = "data/b1_effect/" + params

#data_filename =  "{:s}_{:s}.csv".format(strat_space, transition)

print(data_folder)


img_format = "pdf"
img_folder = data_folder
img_filename  = "{:s}_{:s}.{:s}".format(strat_space, transition, img_format)

# check it exists
pathlib.Path(data_folder).mkdir(parents=True, exist_ok=True) 


# set plot style
sns.set(style="darkgrid", palette="pastel")

# Load the dataset
data = pd.read_csv(data_folder + data_filename)

data_strat_space = data.loc[data["strat_space"] == strat_space]

fig, ax1 = plt.subplots(nrows=1, ncols=1)


#ax1.set_xscale('log', basex=10)
#ax1.set(xscale="log", basex=2)


# lineplots
cc = sns.lineplot(x="b1", y="1CC rate", data=data_strat_space, ax = ax1, label = "1CC rate")
c  = sns.lineplot(x="b1", y="C rate", data=data_strat_space, ax = ax1, label = "C rate")
spe_rate  = sns.lineplot(x="b1", y="SPE rate", data=data_strat_space, ax = ax1, label = "SPE rate")

title = "{:s} {:s} Cooperation Rates".format(strat_space, transition)
ax1_xlabel = "b1 value"
ax1_ylabel = ""

# seaborn graph
ax1.set_title(title, fontsize=14, fontweight='bold')
ax1.set_xlabel(ax1_xlabel)
ax1.set_ylabel(ax1_ylabel)

fig.subplots_adjust(hspace=1, wspace=1)

plt.savefig(img_folder + img_filename, format=img_format)

plt.show()
