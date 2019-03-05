import pandas as pd
import glob

date = "date_2019_03_03_18_37_03" #date_2019_02_24_19_50_14"
strat_space = "S_08"
transition = "EqualSay_G2_Default"

eps = 2

output = "{:s}_{:s}.csv".format(strat_space, transition)
#data_filename =  "{:s}_{:s}.csv".format(strat_space, transition)

data_folder   = "data/b1_effect/eps_1.00e-0{:d}_beta_2.00e+00_T_5.00e+05_c_1.00_b2_1.20/{:s}/".format(eps, date)

print(data_folder)


interesting_files = glob.glob(data_folder + "*.csv")
print("Merging " + str(len(interesting_files)) + " files.")
#print(interesting_files)

df_list = []
for filename in sorted(interesting_files):
    df_list.append(pd.read_csv(filename))
full_df = pd.concat(df_list)

full_df.to_csv(data_folder + output, index=False)