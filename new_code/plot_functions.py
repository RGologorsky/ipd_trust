import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

import os.path
from pathlib import Path

types =["all", "within_strategy", "within_transition"]

specifics_a = ["s_08", "s_12", "s_16"]
specifics_b = ["full_set_g1_default", "full_set_g2_default", "full_set_random", "full_set_random_dictator", "full_set_unilateral_dictator"]


folder_type = types[2]
specific = specifics_b[4]

parent_folder = "data/full_set_{:s}/".format(folder_type)
sub_folder = "{:s}/".format(specific)

folder_path = parent_folder + sub_folder

hue = "strat"

save_df_filename ="{:s}_combined.csv".format(specific)
img_filename = "{:s}_{:s}".format(specific, "all_transitions")

##### IMPORTANT ####
##### CHECK PARAMETERS ARE CORRECT ####
from parameters import *

def get_param_str():
	eps, beta = params_dict["eps"], params_dict["beta"]

	eps = r"$\epsilon$"  + " = {:2.2e}\n ".format(eps)
	beta = r"$\beta$"    + " = {:2.2e}\n ".format(beta)
	ts = r"$T$"             + " = {:2.2e}".format(num_timesteps)

	game_param = "b2 = {:.2f}\nc1 = c2 = {:.2f}".format(b2, c1)
	sep = "\n\n"
	param_str = "Evolution Parameters:\n " + eps + beta + ts + sep + \
				"Game Parameters:\n"  + game_param + sep + \
				"{:d} Runs".format(num_runs)
	return param_str

def get_files(folder_path):
	source_dir = Path(folder_path)
	files = source_dir.iterdir()
	return list(files)

def combine_files_into_df(folder_path, save, save_df_filename):

	save_loc = folder_path + save_df_filename

	# check if data already combined
	if os.path.isfile(save_loc):
		return pd.read_csv(save_loc)

	# if not, combine all files in folder path
	files = get_files(folder_path)
	combined_data = [pd.read_csv(file) for file in files]
	combined_data = pd.concat(combined_data, sort=False)

	if save:
		combined_data.to_csv(save_loc, index=False)

	return combined_data

def plot_by_transition(df, img_folder, img_filename="transition", img_format="svg"):

	# create img directory, if doesn't exist
	Path(img_folder).mkdir(parents=True, exist_ok=True) 

	sns.set(style="darkgrid", palette="pastel")


	# fig, ((ax1, ax2, ax3, ax4)) = plt.subplots(nrows=1, ncols=4, figsize = (24,6))
	fig, ((ax1, ax2, ax3, ax4)) = plt.subplots(nrows=1, ncols=4, figsize = (24,6))
	
	# set title							
	super_title = "Effect of b1 on the Evolution of Cooperation"
	fig.suptitle(super_title, fontsize=14, fontweight='bold')



	# last axis describes parameters

	## CHECK PARAMETERS ARE CORRECT FOR THIS DATA!!!!!
	param_str = get_param_str()

	ax4.text(0.5, 0.3, param_str, horizontalalignment='center',
	        fontsize=10, multialignment='left',
	        bbox=dict(boxstyle="round", facecolor='#D8D8D8',
	        ec="0.5", pad=0.30, alpha=1), fontweight='bold')

	ax4.axis('off')
	
	#loc="upper left", bbox_to_anchor=(1.05, 1)


	# axes labels
	ax_xlabel = "b1 value"

	ax1_ylabel = "Game 1 Rate"
	ax2_ylabel = "1CC Rate"
	ax3_ylabel = "2CC Rate"


	# lineplots
	game1_g = sns.lineplot(x="b1", y="Game 1 rate", hue=hue, data=df, ax = ax1, legend=False)
	cc1_g = sns.lineplot(x="b1", y="1CC rate", 		hue=hue, data=df, ax = ax2, legend=False)
	cc2_g = sns.lineplot(x="b1", y="2CC rate", 		hue=hue, data=df, ax = ax3) #, legend=True)


	# set labels
	game1_g.set_xlabel(ax_xlabel)
	cc1_g.set_xlabel(ax_xlabel)
	cc2_g.set_xlabel(ax_xlabel)

	# set legend
	legend = cc2_g.legend(loc="upper left", bbox_to_anchor=(1.05, 1))
	legend.texts[0].set_text("Strategy/Transition Type")

	# save figure	
	fig.subplots_adjust(hspace=0.50, wspace=0.50)
	fig.savefig("{:s}{:s}.{:s}".format(img_folder, img_filename, img_format), format=img_format)

	# show the plot
	plt.show()


def plot_all(df, img_folder, img_filename="all", img_format="svg"):

	# create img directory, if doesn't exist
	Path(img_folder).mkdir(parents=True, exist_ok=True) 

	sns.set(style="darkgrid", palette="pastel")


	# fig, ((ax1, ax2, ax3, ax4)) = plt.subplots(nrows=1, ncols=4, figsize = (24,6))
	fig, ((ax1, ax2)) = plt.subplots(nrows=1, ncols=2, figsize = (24,6))
	
	# set title							
	super_title = "Effect of b1 on the Evolution of Cooperation"
	fig.suptitle(super_title, fontsize=14, fontweight='bold')


	# last axis describes parameters

	## CHECK PARAMETERS ARE CORRECT FOR THIS DATA!!!!!
	param_str = get_param_str()

	ax2.text(0.0, 0.0, param_str, horizontalalignment='center',
	        fontsize=10, multialignment='left',
	        bbox=dict(boxstyle="round", facecolor='#D8D8D8',
	        ec="0.5", pad=0.30, alpha=1), fontweight='bold')

	ax2.axis('off')
	
	#loc="upper left", bbox_to_anchor=(1.05, 1)


	# axes labels
	ax_xlabel = "b1 value"
	ax1_ylabel = "1CC Rate"

	# lineplots
	cc1_g = sns.lineplot(x="b1", y="1CC rate", hue=hue, data=df, ax = ax1)


	# set labels
	cc1_g.set_xlabel(ax_xlabel)

	# set legend
	legend = cc1_g.legend(loc="upper left", bbox_to_anchor=(1.05, 1))
	legend.texts[0].set_text("Strategy/Transition Type")

	# save figure	
	fig.subplots_adjust(hspace=0.50, wspace=0.50)
	fig.savefig("{:s}{:s}.{:s}".format(img_folder, img_filename, img_format), format=img_format)

	# show the plot
	plt.show()

#df = pd.read_csv(folder_path + "combined.csv")
df = combine_files_into_df(folder_path, save=True, save_df_filename=save_df_filename)
#plot_by_transition(df, img_folder=folder_path, img_filename=img_filename, img_format="pdf")

#df = pd.read_csv(folder_path + "all_combined.csv")
plot_all(df, img_folder=folder_path, img_filename=img_filename, img_format="pdf")