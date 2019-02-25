import pathlib # to create directory if needed
#import numpy as np
from helper_functions import get_params

# Parameters
num_runs = 5
num_timesteps = 3*(10**5)

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
    #"Unilateral_Dictator",
    #"Random_Dictator",
    #"Random",
]

N, eps, beta = get_params(["N", "eps", "beta"], params_dict)

save_params_dict = {

	# test params
	"num_runs": num_runs,
	"num_timesteps": num_timesteps,

	# evolutionary params
	"N": 100,
	"eps": 0.001,
	"beta": 2.0,
	"strategy_type": "pure", # or "stochastic"
	
	# game params
	"c": c,
	"b2": b2,
	"c1": c,
	"c2": c,
}