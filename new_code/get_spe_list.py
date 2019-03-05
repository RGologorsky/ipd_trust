import numpy as np
#import pandas as pd

# load SPE strategies from file


g2_default_folder = "data/full_coop_spe/transitions/EqualSay_G2_Default/c_1.00_b2_1.20_delta_0.9999900000/date_2019_02_26_21_00_57/"
g1_default_folder = "data/full_coop_spe/transitions/EqualSay_G1_Default/c_1.00_b2_1.20_delta_0.9999900000/date_2019_02_26_21_01_29/"

na_default_folder = "data/full_coop_spe/transitions/NA/c_1.00_b2_1.20_delta_0.9999900000/date_2019_02_26_21_01_29/"
# transition = "EqualSay_G1_Default"
# folder = g1_default_folder

def get_spe_dict(transition, game_str, b1_list, eps):

	# set parent folder
	if transition == "EqualSay_G2_Default":
		folder = g2_default_folder
	elif transition == "EqualSay_G1_Default":
		folder = g1_default_folder

	elif transition == "NA":
		folder = na_default_folder
	else:
		raise Exception("unrecognized transition for spe list")

	folder += game_str + "/"

	#"{:s}_{:s}_num_strat_{:d}.csv".format(strat_space, transition, num_strat)

	d = {}
	for b1 in b1_list:
		file_name = folder + "b1_{:.2f}.csv".format(b1)

		# convert to lst
		spe_lst = np.loadtxt(file_name, delimiter=',')
		spe_lst = [tuple(eps + (1-2*eps) * x for x in arr) for arr in spe_lst]

		# print("spe_list")
		# print(spe_lst)

		# save
		d[round(b1,2)] = spe_lst

		#print("Recovered {:d} strategies in {:s}".format(len(spe_lst), strat_space))
		#print(spe_lst)
	#print(d)
	return d

def epss_it(eps, lst):
	return tuple(eps + (1-2*eps) * x for x in lst)

# epss = 0.001
# b1_lists = np.arange(1.0, 3.0, 0.14)
# s8_g2_spe_d = get_spe_dict("EqualSay_G2_Default", "S_08_EqualSay_G2_Default", b1_lists, epss)
# s8_g1_spe_d= get_spe_dict("EqualSay_G1_Default", "S_08_EqualSay_G1_Default", b1_lists, epss)

# s12_g2_spe_d = get_spe_dict("EqualSay_G2_Default", "S_12_EqualSay_G2_Default", b1_lists, epss)
# s12_g1_spe_d= get_spe_dict("EqualSay_G1_Default", "S_12_EqualSay_G1_Default", b1_lists, epss)

# s16_g2_spe_d = get_spe_dict("EqualSay_G2_Default", "S_16_EqualSay_G2_Default", b1_lists, epss)
# s16_g1_spe_d= get_spe_dict("EqualSay_G1_Default", "S_16_EqualSay_G1_Default", b1_lists, epss)

# for b1 in b1_lists:
# 	l = s16_g1_spe_d[round(b1,2)]
# 	print("b1 = {:.2f}, len = {:d}".format(b1, len(l)))

# 	if len(l) > 5:
# 		print(l[:5])
# 	else:
# 		print(l)

### G2 Default ###
# s8_pure_spe_lst = get_spe_list("S_08", 4)
# s12_pure_spe_lst = get_spe_list("S_12", 36)
# s16_pure_spe_lst = get_spe_list("S_16", 108)

#print(s8_g2_spe_d.keys())
#print(s8_g2_spe_d[1.7])
#print(epss_it(epss, [1,0,0,1,1,1,1,0]))
### G1 Default


#print(epss_it(epss, [1,0,0,1,1,1,1,0]) in s8_g2_spe_d[1.7])
#print(epss_it(epss, [1,0,0,1,1,1,1,0]) in s8_g2_spe_d[1.14])
# print([1,0,0,1,1,0,1,0] in s8_spe_lst)
# print([0,1,0,1,1,1,1,0] in s8_spe_lst)