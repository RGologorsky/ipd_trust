# import seaborn as sns
# sns.set(style="ticks")
# exercise = sns.load_dataset("exercise")
# g = sns.catplot(x="time", y="pulse", hue="kind", data=exercise)

import matplotlib.pyplot as plt
import seaborn as sns

import pandas as pd
import pathlib

from parameters import *

#data_folder = "data/b1_effect/figs/all/" 
#data_file   = "all_eps_1.00e-03_beta_2.00e+00_T_5.00e+05_c_1.00_b2_1.20_date_2019_03_08_17_11_57"

# HIGH PRESSURE

# EQ G2
#data_file = "s08_all_eps_1.00e-02_beta_1.00e+01_T_1.00e+06_c_1.00_b2_1.20_date_2019_03_04_08_03_01"

# EQ G1
#data_file    = "all_eps_1.00e-02_beta_1.00e+01_T_1.00e+06_c_1.00_b2_1.20_date_2019_03_12_20_11_14"

#data_file += ".csv"

# HACK
eps = 2
T=6
b2=1.2
c2=1.0
date = "date_2019_06_05_14_45_40"

data_folder = "data/b1_effect/eps_1.00e-0{:d}_beta_1.00e+01_T_1.00e+0{:d}_b2_{:.2f}_c2_{:.2f}/{:s}/"\
                .format(eps,T,b2,c2,date)

#data_file = "all.csv"


# data_file = "all_S_08_EqualSay_G2_Default.csv"

run_num = 4
data_file = "S_08_EqualSay_G2_Default" + "_run_{:d}".format(run_num) + ".csv"

img_folder = data_folder 
img_filename = "contour_S_08_EqualSay_G2_Default" + "_run_{:d}".format(run_num)
img_format = "pdf"

labels_dict = {
    "EqualSay_G1_Default": "D-G1",
    "EqualSay_G2_Default": "D-G2"
}

def plot_contour(transition):

    data = pd.read_csv(data_folder + data_file)

    # create img directory
    pathlib.Path(img_folder).mkdir(parents=True, exist_ok=True) 

    #sns.set(style="darkgrid", palette="pastel")

    fig, ax1 = plt.subplots(nrows=1, ncols=1)

    #setosa = iris.loc[iris.species == "setosa"]
    #virginica = iris.loc[iris.species == "virginica"]

    X,Y,Z = alpha1_list, c1_list, data["C rate"].values.reshape((len(alpha1_list), len(c1_list)))    

    print(X)
    print(Y)
    print(Z)
    cp = plt.contourf(X, Y, Z)
    plt.colorbar(cp)
    plt.title(transition + " (Run {:d})".format(run_num))
    plt.xlabel(r"$\alpha_1$")
    plt.ylabel(r"$c_1$")
    #plt.show()
    plt.savefig(img_folder + img_filename + "_{:s}.{:s}".format(transition, img_format), format=img_format, bbox_inches="tight")


transition = "EqualSay_G2_Default" #"EqualSay_G2_Default" # "EqualSay_G1_Default"
plot_contour(transition)

# date = "date_2019_03_04_08_03_01" #date_2019_02_24_19_50_14"
# strat_space = "S_12"
# transition = "EqualSay_G2_Default"

# data_filename =  "all.csv"

# Parameters
# N, eps, beta = 100, 0.001, 2.0
# num_timesteps = 5*(10**5)
# c,  b2 = 1.0, 1.2


# params = "eps_{:.2e}_beta_{:.2e}_T_{:.2e}_c_{:.2f}_b2_{:.2f}/{:s}/"\
# 		.format(eps, beta, num_timesteps, c, b2, date)

# data_folder   = "data/b1_effect/" + params

#data_filename =  "{:s}_{:s}.csv".format(strat_space, transition)

# print(data_folder)


# img_format = "pdf"
# img_folder = data_folder
# img_filename  = "{:s}_{:s}.{:s}".format(strat_space, transition, img_format)

# # check it exists
# pathlib.Path(data_folder).mkdir(parents=True, exist_ok=True) 


# # set plot style
# sns.set(style="darkgrid", palette="pastel")

# # Load the dataset
# data = pd.read_csv(data_folder + data_filename)

# data_strat_space = data.loc[data["strat_space"] == strat_space]

# fig, ax1 = plt.subplots(nrows=1, ncols=1)


#ax1.set_xscale('log', basex=10)
#ax1.set(xscale="log", basex=2)


# lineplots
# cc = sns.lineplot(x="b1", y="1CC rate", data=data_strat_space, ax = ax1, label = "1CC rate")
# c  = sns.lineplot(x="b1", y="C rate", data=data_strat_space, ax = ax1, label = "C rate")
# spe_rate  = sns.lineplot(x="b1", y="SPE rate", data=data_strat_space, ax = ax1, label = "SPE rate")

# title = "{:s} {:s} Cooperation Rates".format(strat_space, transition)
# ax1_xlabel = "b1 value"
# ax1_ylabel = ""

# # seaborn graph
# ax1.set_title(title, fontsize=14, fontweight='bold')
# ax1.set_xlabel(ax1_xlabel)
# ax1.set_ylabel(ax1_ylabel)

# fig.subplots_adjust(hspace=1, wspace=1)

# plt.savefig(img_folder + img_filename, format=img_format)

#plt.show()
