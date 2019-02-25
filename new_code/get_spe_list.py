import numpy as np
#import pandas as pd

# load SPE strategies from file
folder = "data/spe/delta_0.9999900000_c_1.00_b1_1.61_b2_1.20/"
date = "date_2019_02_06_12_00_36/"

def get_spe_list(strat_space, num_strat):
	file_name = folder + date + \
							"{:s}_full_coop_SPE_num_strat_{:d}.csv".format(strat_space, num_strat)

	spe_lst = np.loadtxt(file_name, delimiter=',')

	# convert to lst
	spe_lst = [tuple(int(a) for a in arr) for arr in spe_lst]

	print("Recovered {:d} strategies in {:s}".format(len(spe_lst), strat_space))
	#print(spe_lst)
	return spe_lst


s8_pure_spe_lst = get_spe_list("S08", 4)
s12_pure_spe_lst = get_spe_list("S12", 36)
s16_pure_spe_lst = get_spe_list("S16", 108)

def get_eps_spe_list(eps, spe_lst):
	return [tuple(eps + (1-2*eps) * x for x in arr) for arr in spe_lst]

# print([1,0,0,1,1,1,1,0] in s8_spe_lst)
# print([1,0,0,1,1,0,1,0] in s8_spe_lst)
# print([0,1,0,1,1,1,1,0] in s8_spe_lst)