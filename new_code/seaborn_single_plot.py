# import seaborn as sns
# sns.set(style="ticks")
# exercise = sns.load_dataset("exercise")
# g = sns.catplot(x="time", y="pulse", hue="kind", data=exercise)

import matplotlib.pyplot as plt
import seaborn as sns

import pandas as pd
import pathlib


data_folder   = "data/param_effect_fixed/eps/date_2019_02_20_08_54_27/"
data_filename =  "eps.csv"

img_format = "pdf"
img_folder = data_folder
img_filename  = "eps" + ".{:s}".format(img_format)

# check it exists
pathlib.Path(data_folder).mkdir(parents=True, exist_ok=True) 


# set plot style
sns.set(style="darkgrid", palette="pastel")

# Load the dataset
data = pd.read_csv(data_folder + data_filename)

fig, ax1 = plt.subplots(nrows=1, ncols=1)

ax1.set(xscale="log")

# seaborn graph
g = sns.lineplot(x="eps", y="CC rate", ax=ax1, data=data)

g.set_title("Effect of Noise")
g.set_xlabel("Noise Level, {:s}".format(r'$\epsilon$'))
g.set_ylabel("CC rate")


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