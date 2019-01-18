import numpy as np
import matplotlib.pyplot as plt
from helper_functions import *

# recover data
filename = "data/" + \
				"b1_effect_eps_0.001_beta_2.0_T_400000_game_S_12 Game_run_0_date_2019_01_08_time_20_47_55" \
			+ ".csv"

b1_list, cc_avgs, g1_avgs = np.loadtxt(filename, delimiter=',')

# from filename, fill in parameters
game_str = "S_12 Game"
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