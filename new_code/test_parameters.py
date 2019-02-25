import pathlib # to create directory if needed
#import numpy as np
from helper_functions import get_params

# Parameters
num_runs = 1
num_timesteps = 1*(10**4)

params_dict = {
	"N": 100,
	"eps": 0.001,
	"beta": 2.0,
	"strategy_type": "pure", # or "stochastic"
}

c = 1.0
b2 = 1.2

c1 = c
c2 = c

transitions = [
	"EqualSay_G2_Default",
    #"EqualSay_G1_Default",
    #"Player1_Dictator",
    #"Random_Dictator",
]

eps, beta = get_params(["eps", "beta"], params_dict)

# loc = "data" or "imgs"
# experiment = "b1_effect" or "spe"

def get_folder(timestamp, directory="data/test/b1_effect"):
	# set folder name
	folder = "{:s}/eps_{:.2e}_beta_{:.2e}_T_{:.2e}_c_{:.2f}_b2_{:.2f}/{:s}/"\
		.format(directory, eps, beta, num_timesteps, c, b2, timestamp)

	# create directory
	pathlib.Path(folder).mkdir(parents=True, exist_ok=True) 

	return folder