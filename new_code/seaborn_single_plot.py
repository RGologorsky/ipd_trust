# import seaborn as sns
# sns.set(style="ticks")
# exercise = sns.load_dataset("exercise")
# g = sns.catplot(x="time", y="pulse", hue="kind", data=exercise)

import matplotlib.pyplot as plt
import seaborn as sns

import pandas as pd
import pathlib


date = "date_2019_02_22_07_52_54"
param_to_change = "beta"

data_folder   = "data/param_effect_fixed/{:s}/{:s}/".format(param_to_change, date)
data_filename =  "{:s}.csv".format(param_to_change)

img_format = "pdf"
img_folder = data_folder
img_filename  = "{:s}.{:s}".format(param_to_change, img_format)

# check it exists
pathlib.Path(data_folder).mkdir(parents=True, exist_ok=True) 


# set plot style
sns.set(style="darkgrid", palette="pastel")

# Load the dataset
data = pd.read_csv(data_folder + data_filename)

fig, ax1 = plt.subplots(nrows=1, ncols=1)

ax1.set_xscale('log', basex=10)
#ax1.set(xscale="log", basex=2)

# seaborn graph
g = sns.lineplot(x=param_to_change, y="player_c_avg", ax=ax1, data=data)

g.set_title("Effect of Selection")
g.set_xlabel("Selection Pressure, {:s}".format(r'$\beta$'))
g.set_ylabel("Individual Cooperation Rate")


plt.savefig(img_folder + img_filename, format=img_format)

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