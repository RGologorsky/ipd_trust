# import seaborn as sns
# sns.set(style="ticks")
# exercise = sns.load_dataset("exercise")
# g = sns.catplot(x="time", y="pulse", hue="kind", data=exercise)

import matplotlib.pyplot as plt
import seaborn as sns

import pandas as pd
import pathlib



data_folder =  "⁨data/b1_effect/eps_1.00e-03_beta_2.00e+00_T_5.00e+03_c_1.00_b2_1.20/date_2019_02_27_13_29_30/"

img_format = "pdf"
img_folder = data_folder
img_filename  = "hm.{:s}".format(img_format)

# check it exists
pathlib.Path(data_folder).mkdir(parents=True, exist_ok=True) 


# set plot style
sns.set(style="darkgrid", palette="pastel")

# Load the dataset

filename = "S_16_EqualSay_G2_Default_run_0.csv"
print(data_folder + filename)
data = pd.read_csv(data_folder + filename)
fig, ax1 = plt.subplots(nrows=1, ncols=1)

#ax1.set_xscale('log', basex=10)
#ax1.set(xscale="log", basex=2)

# seaborn graph
g = sns.lineplot(x="b1", y="1CC rate", ax=ax1, data=data)

# g.set_title("Effect of Selection")
# g.set_xlabel("Selection Pressure, {:s}".format(r'$\beta$'))
# g.set_ylabel("Individual Cooperation Rate")


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