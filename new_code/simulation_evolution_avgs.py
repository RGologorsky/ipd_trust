import numpy as np
import time

from stochastic_dynamics import *
from helper_functions import *

# returns CC and G1 average over evolutionary timeframe
# @profile

def get_evolution_avgs(num_timesteps, params_dict, b1, spe_d):

    spe_list = spe_d[round(b1,2)]
    #print(spe_list)

    # get needed parameters
    params_needed = ("N", "eps", "beta", "host", "game", "strategy_type")
    N, eps, beta, host, Game, strategy_type = get_params(params_needed, params_dict)

    # reset b1
    Game.reset_b1(b1)

    # avg over entire evolution simulation
    g1_cc_avg = 0.0
    g2_cc_avg = 0.0
    g1_game_avg = 0.0
    player_c_avg = 0.0

    spe_list_avg = 0.0

    # set up random variables to simulate evolution
    random_floats  = np.random.random(size=num_timesteps)
    mutants        = generate_pure_strategy_mutants(num_timesteps, Game.strat_len, eps) \
                     if strategy_type == "pure" \
                     else generate_stochastic_strategy_mutants(num_timesteps, Game.strat_len, eps) 

    random_float_index = 0;
    mutant_index       = 0;    
    
    # store current host v. host payoff
    curr_host = host
    pi_xx, _, g1_cc_rate, g2_cc_rate, g1_game_rate, player_c_rate  = Game.get_stats(curr_host, curr_host)

    # determine proportion of time the current host is a coop spe
    curr_host_is_spe = (curr_host in spe_list)

    # Main Evolution Loop
    for timestep in range(num_timesteps):

        # get mutant strategy, update mutant index
        mutant = tuple(mutants[mutant_index:mutant_index + Game.strat_len])
        mutant_index += Game.strat_len
        
        # get probability of succession invasion
        pi_xy, pi_yx  = Game.get_payoffs(curr_host, mutant)
        pi_yy, _      = Game.get_payoffs(mutant,    mutant)   

        # get random float, update float index
        random_float = random_floats[random_float_index]
        random_float_index += 1

        # update host strategy if random_float <= Prob[invasion]
        if does_mutant_fixate(N, beta, pi_xx, pi_xy, pi_yx, pi_yy, random_float):

            # update host strategy
            curr_host = mutant
            pi_xx, _, g1_cc_rate, g2_cc_rate, g1_game_rate, player_c_rate  = Game.get_stats(curr_host, curr_host)

            # add 1 if curr host is in set of spe strategies
            curr_host_is_spe = (curr_host in spe_list) 
        
        # store data
        g1_cc_avg += g1_cc_rate
        g2_cc_avg += g2_cc_rate
        g1_game_avg += g1_game_rate
        player_c_avg += player_c_rate
        spe_list_avg += curr_host_is_spe

        #print(spe_list)
        #print(curr_host)

    return g1_cc_avg/float(num_timesteps), g2_cc_avg/float(num_timesteps), \
           g1_game_avg/float(num_timesteps), player_c_avg/float(num_timesteps), \
           spe_list_avg/float(num_timesteps)


# returns CC avgs and G1 avgs for each tested param value
def get_b1_evolution_data(num_timesteps, b1_list, params_dict, spe_d):
    return zip (*[get_evolution_avgs(num_timesteps, params_dict, b1, spe_d) for b1 in b1_list])