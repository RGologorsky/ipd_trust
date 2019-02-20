import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

import os.path
from pathlib import Path


date = "date_2019_02_18_22_02_00"

data_folder = "data/param_effect/N/{:s}/".format(date)
img_folder = data_folder

df = pd.read_csv(data_folder + "N_8.csv")

hue = "N"
img_filename = "{:s}".format(hue)

##### IMPORTANT ####
##### CHECK PARAMETERS ARE CORRECT ####
from parameters import *

def plot_param(df, img_folder, img_filename="all", img_format="svg"):

	# create img directory, if doesn't exist
	Path(img_folder).mkdir(parents=True, exist_ok=True) 

	# set graph style
	sns.set(style="darkgrid", palette="pastel")


	# fig, ((ax1, ax2, ax3, ax4)) = plt.subplots(nrows=1, ncols=4, figsize = (24,6))
	fig, ax1 = plt.subplots(nrows=1, ncols=1)
	
	# set title							
	title = "Cooperation robustness w.r.t. parameter N"
	ax1.set_title(title, fontsize=14, fontweight='bold')

	# last axis describes parameters

	## CHECK PARAMETERS ARE CORRECT FOR THIS DATA!!!!!
	
	
	#loc="upper left", bbox_to_anchor=(1.05, 1)


	# axes labels
	ax1_xlabel = "b1 value"
	ax1_ylabel = "CC rate"

	# lineplots
	cc_g = sns.lineplot(x="b1", y="CC rate", hue=hue, data=df, ax = ax1)


	# set labels
	cc_g.set_xlabel(ax1_xlabel)

	# set legend
	legend = cc_g.legend(loc="upper left", bbox_to_anchor=(1.05, 1))
	legend.texts[0].set_text("N")

	# save figure	
	fig.tight_layout()
	fig.savefig("{:s}{:s}.{:s}".format(img_folder, img_filename, img_format), format=img_format)

	# show the plot
	plt.show()

plot_param(df, img_folder, img_filename, img_format="svg")