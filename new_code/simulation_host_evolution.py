import numpy as np
import time

from stochastic_dynamics import *
from helpers import *


# returns the sequence of host strategies, each strategy's timespan as host, CC and G1 timestep data
def simulate_host_evolution(num_timesteps, data_collection_freq, params_dict):

    # get needed parameters
    params_needed = ("N", "eps", "beta", "host", "game", "strategy_type", "max_attempts")
    N, eps, beta, host, Game, strategy_type, max_attempts = get_params(params_needed, params_dict)

    # set up arrays to store evolution data
    num_data_pts  = int(num_timesteps/data_collection_freq)
    cc_timestep_data = np.zeros(num_data_pts)
    g1_timestep_data = np.zeros(num_data_pts)
    data_index = 0
    #host_timestep_data  = np.zeros(num_data_pts, Game.strat_len)
    
    # keep track of sequence of hosts and how long each host lasted
    host_seq = [host]
    host_timespans = []

    # set up random variables
    random_floats  = np.random.random(size=num_timesteps)
    mutants        = generate_pure_strategy_mutants(num_timesteps, Game.strat_len, eps) \
                     if strategy_type == "pure" \
                     else generate_stochastic_strategy_mutants(num_timesteps, Game.strat_len, eps) 

    random_float_index = 0;
    mutant_index       = 0;    
    
    # store current host v. host payoff
    curr_host = host
    pi_xx, _, cc_rate, g1_rate  = Game.get_stats(curr_host, curr_host)

    curr_host_timespan = 0

    # Main Evolution Loop
    for timestep in range(num_timesteps):

        # get mutant strategy, update mutant index
        mutant = tuple(mutants[mutant_index:mutant_index + Game.strat_len])
        mutant_index += Game.strat_len
        
        # get probability of succession invasion
        pi_xy, pi_yx  = Game.get_payoffs(curr_host, mutant)
        pi_yy, _      = Game.get_payoffs(mutant,    mutant)   

        prob_invasion = get_prob_mutant_fixation(N, beta, pi_xx, pi_xy, pi_yx, pi_yy)

        # get random float, update float index
        random_float = random_floats[random_float_index]
        random_float_index += 1

        # update host strategy
        if random_float <= prob_invasion:
            curr_host = mutant
            pi_xx, _, cc_rate, g1_rate  = Game.get_stats(curr_host, curr_host)

            # update host sequence
            host_seq.append(curr_host)
            host_timespans.append(curr_host_timespan)

            # reset for new host
            curr_host_timespan = 0

        curr_host_timespan += 1

        # store data
        if timestep % data_collection_freq == 0:
            cc_timestep_data[data_index] = cc_rate
            g1_timestep_data[data_index] = g1_rate
            data_index += 1


    host_timespans.append(curr_host_timespan)
    return host_seq, host_timespans, cc_timestep_data, g1_timestep_data