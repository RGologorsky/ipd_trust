import pandas as pd

# Load the dataset

folder = "data/b1_effect/long_time_all/eps_1.00e-03_beta_2.00e+00_T_3.00e+05_c_1.00_b2_1.20/"
save_folder = folder + "/added_cols/"

save_filenames = [
	"S_04_EqualSay_G2_Default.csv",
	# "S_08_EqualSay_G2_Default.csv",
	# "S_12_EqualSay_G2_Default.csv",
	# "S_16_EqualSay_G2_Default.csv",
]

data1 = pd.read_csv(folder + "S_04_df.csv")
# data2 = pd.read_csv(folder + "S_08_df.csv")
# data3 = pd.read_csv(folder + "S_12_df.csv")
# data4 = pd.read_csv(folder + "S_16_df.csv")

all_datas =  [data1] #[data2, data3, data4]
strats = ["S_04"]
#strats = ["S_08", "S_12", "S_16"]

transition = "NA"
for i, df in enumerate(all_datas):
	df = df.rename(columns={'strat': 'strat_space'})
	df["transition"] = transition

	strat = strats[i]
	df["strat"] = "{:s}_{:s}".format(strat, transition)

	# save
	save_filename = save_filenames[i]
	df.to_csv(save_folder + save_filename, index=False)
