folder = "data/full_coop_compare/"

f1 = folder + "S_12_Player1_Dictator_num_strat_32.csv"
f2 = folder + "S12_EqualSay_G2_Default_num_strat_36.csv"

with open(f1, 'r') as new, open(f2, 'r') as old:
    new_strats = new.readlines()
    old_strats = old.readlines()

with open('diff_new_is_missing_strat_32.csv', 'w') as outFile:
    for strat in old_strats:
        if strat not in new_strats:
        	print("new_strats is missing strat: {:s}".format(strat))
        	outFile.write(strat)

with open('diff_new_added_strat_32.csv', 'w') as outFile:
    for strat in new_strats:
        if strat not in old_strats:
        	print("new_strats added strat: {:s}".format(strat))
        	outFile.write(strat)