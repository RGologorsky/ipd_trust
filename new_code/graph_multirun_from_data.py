import numpy as np
import matplotlib.pyplot as plt
from helper_functions import *

# recover data

# S12
# filename0 = "b1_effect_eps_0.001_beta_2.0_T_400000_game_S_12 Game_run_0_date_2019_01_08_time_20_47_55"
# filename1 = "b1_effect_eps_0.001_beta_2.0_T_400000_game_S_12 Game_run_1_date_2019_01_08_time_22_55_35"
# filename2 = "b1_effect_eps_0.001_beta_2.0_T_400000_game_S_12 Game_run_2_date_2019_01_09_time_00_37_42"
# filename3 = "b1_effect_eps_0.001_beta_2.0_T_400000_game_S_12 Game_run_3_date_2019_01_09_time_02_18_23"

filename0 = "b1_effect_eps_0.001_beta_2.0_T_400000_game_S_16 Game_run_0_date_2019_01_09_time_03_30_32"
filename1 = "b1_effect_eps_0.001_beta_2.0_T_400000_game_S_16 Game_run_1_date_2019_01_09_time_04_44_23"
filename2 = "b1_effect_eps_0.001_beta_2.0_T_400000_game_S_16 Game_run_2_date_2019_01_09_time_05_58_40"
filename3 = "b1_effect_eps_0.001_beta_2.0_T_400000_game_S_16 Game_run_3_date_2019_01_09_time_07_12_37"

# add folder location/data type
filename0 = "data/" + filename0 + ".csv"
filename1 = "data/" + filename1 + ".csv"
filename2 = "data/" + filename2 + ".csv"
filename3 = "data/" + filename3 + ".csv"


# take average over 4 rounds
b1_list, round0_cc_avgs, round0_g1_avgs = np.loadtxt(filename0, delimiter=',')
_, round1_cc_avgs, round1_g1_avgs = np.loadtxt(filename1, delimiter=',')
_, round2_cc_avgs, round2_g1_avgs = np.loadtxt(filename2, delimiter=',')
_, round3_cc_avgs, round3_g1_avgs = np.loadtxt(filename3, delimiter=',')


cc_avgs = (round0_cc_avgs + round1_cc_avgs + round2_cc_avgs + round3_cc_avgs)/4.0
g1_avgs = (round0_g1_avgs + round1_g1_avgs + round2_g1_avgs + round3_g1_avgs)/4.0

# from filename, fill in parameters
game_str = "S_16 Game"
eps = 0.001
beta = 2.0
num_timesteps = 400000

print("== CC Avgs ==\n", cc_avgs, "\n== G1 Avgs ==\n", g1_avgs, "\n== END ==")

# plot data
fig, (ax1, ax2, ax3) = plt.subplots(nrows=1, ncols=3, figsize=(12, 6))

# fig
super_title = "b1 effect on {:s}".format(game_str)
fig.suptitle(super_title, fontsize=14, fontweight='bold')

# Ax1
xlabel = "b1"
ylabel = "Avg. CC rate"
title = "CC vs. b1 value"

add_line_plot(ax1, b1_list, cc_avgs, xlabel, ylabel, title, text="", point_size=10)

#Ax2
eps = r"$\epsilon$"  + " = {:2.2e}\n ".format(eps)
beta = r"$\beta$"    + " = {:2.2e}\n ".format(beta)
ts = "T"             + " = {:2.2e}".format(num_timesteps)

param_str = "Parameters:\n " + eps + beta + ts
#dd_titlebox(ax2, param_str)
ax2.text(0.38, 0.80, param_str, horizontalalignment='center',
     verticalalignment='center', transform=ax2.transAxes)
ax2.set_axis_off()

# Ax3
xlabel = "b1"
ylabel = "Avg. Game 1 rate"
title = "Game 1 vs. b1 value"

add_line_plot(ax3, b1_list, g1_avgs, xlabel, ylabel, title, text="", point_size=10)

#fig.subplots_adjust(wspace=2)
plt.show()