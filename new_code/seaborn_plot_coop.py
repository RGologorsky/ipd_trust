# import seaborn as sns
# sns.set(style="ticks")
# exercise = sns.load_dataset("exercise")
# g = sns.catplot(x="time", y="pulse", hue="kind", data=exercise)

import matplotlib.pyplot as plt
import seaborn as sns

import pandas as pd
import pathlib


date = "date_2019_02_24_19_50_14"
strat_space = "S_16"

# date = "date_2019_02_24_19_49_44"
# strat_space = "S_12"

# date = "date_2019_02_24_19_48_50"
# strat_space = "S_08"

data_folder   = "data/b1_effect/eps_1.00e-03_beta_2.00e+00_T_3.00e+05_c_1.00_b2_1.20/{:s}/".format(date)

print(data_folder)

data_filename =  "{:s}_EqualSay_G2_Default.csv".format(strat_space)

img_format = "pdf"
img_folder = data_folder
img_filename  = "{:s}_EqualSay_G2_Default.{:s}".format(strat_space, img_format)

# check it exists
pathlib.Path(data_folder).mkdir(parents=True, exist_ok=True) 


# set plot style
sns.set(style="darkgrid", palette="pastel")

# Load the dataset
data = pd.read_csv(data_folder + data_filename)

fig, ax1 = plt.subplots(nrows=1, ncols=1)


#ax1.set_xscale('log', basex=10)
#ax1.set(xscale="log", basex=2)


# lineplots
cc = sns.lineplot(x="b1", y="1CC rate", data=data, ax = ax1, label = "1CC rate")
c  = sns.lineplot(x="b1", y="Cooperation rate", data=data, ax = ax1, label = "C rate")
spe_rate  = sns.lineplot(x="b1", y="SPE rate", data=data, ax = ax1, label = "SPE rate")

title = "{:s} Cooperation Trends".format(strat_space)
ax1_xlabel = "b1 value"
ax1_ylabel = ""

# seaborn graph
ax1.set_title(title, fontsize=14, fontweight='bold')
ax1.set_xlabel(ax1_xlabel)
ax1.set_ylabel(ax1_ylabel)

fig.subplots_adjust(hspace=1, wspace=1)

plt.savefig(img_folder + img_filename, format=img_format)

plt.show()
