# import seaborn as sns
# sns.set(style="ticks")
# exercise = sns.load_dataset("exercise")
# g = sns.catplot(x="time", y="pulse", hue="kind", data=exercise)

import matplotlib.pyplot as plt
import seaborn as sns

import pandas as pd
import pathlib

import numpy as np

img_format = "pdf"
img_folder = "data/misc/"
img_filename  = "sigmoid" + ".{:s}".format(img_format)

# check it exists
pathlib.Path(img_folder).mkdir(parents=True, exist_ok=True) 

# Probability Helpers
def get_prob_imitation(beta, diff):
    return 1.0/(1.0 + np.exp(-1.0 * beta * diff))

def get_label(num):
	return r'$\beta$' + " = {:.1f}".format(num)

x = np.arange(-1.0, 1.0, 0.05)

# set plot style
sns.set(style="darkgrid", palette="pastel")

fig, ax1 = plt.subplots(nrows=1, ncols=1)

#plt.plot(x, get_prob_imitation(beta=0.1, diff=x), label=get_label(0.1))
plt.plot(x, get_prob_imitation(beta=0.5, diff=x), label=get_label(0.5))
#plt.plot(x, get_prob_imitation(beta=1.0, diff=x), label=get_label(1.0))
plt.plot(x, get_prob_imitation(beta=2.0, diff=x), label=get_label(2.0))
plt.plot(x, get_prob_imitation(beta=10.0, diff=x), label=get_label(10.0))


plt.xlabel("Fitness Difference, " + r'$\pi_r - \pi_l$')
plt.ylabel('Prob[Learner imititates Rolemodel]')

plt.title("Imitation Probability and " + "Selection Pressure " + r'$\beta$')

plt.legend()

plt.savefig(img_folder + img_filename, format=img_format)

plt.show()
