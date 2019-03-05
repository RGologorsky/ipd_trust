import pandas as pd
import glob

date = "date_2019_03_04_08_03_01" #date_2019_02_24_19_50_14"

# Parameters
N, eps, beta = 100, 0.01, 10.0
num_timesteps = 10*(10**5)
c,  b2 = 1.0, 1.2


output = "all.csv"
#data_filename =  "{:s}_{:s}.csv".format(strat_space, transition)

params = "eps_{:.2e}_beta_{:.2e}_T_{:.2e}_c_{:.2f}_b2_{:.2f}/{:s}/"\
		.format(eps, beta, num_timesteps, c, b2, date)

data_folder   = "data/b1_effect/" + params

print(data_folder)


interesting_files = glob.glob(data_folder + "*.csv")
print("Merging " + str(len(interesting_files)) + " files.")
#print(interesting_files)

df_list = []
for filename in sorted(interesting_files):
    df_list.append(pd.read_csv(filename))
full_df = pd.concat(df_list)

full_df.to_csv(data_folder + output, index=False)