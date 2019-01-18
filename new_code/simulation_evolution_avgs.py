import numpy as np
import time

from stochastic_dynamics import *
from helper_functions import *

# returns CC and G1 average over evolutionary timeframe
def get_evolution_avgs(num_timesteps, params_dict):

    # get needed parameters
    params_needed = ("N", "eps", "beta", "host", "game", "strategy_type", "max_attempts")
    N, eps, beta, host, Game, strategy_type, max_attempts = get_params(params_needed, params_dict)

    # avg over entire evolution simulation
    cc_avg = 0
    g1_avg = 0

    # set up random variables to simulate evolution
    random_floats  = np.random.random(size=num_timesteps)
    mutants        = generate_pure_strategy_mutants(num_timesteps, Game.strat_len, eps) \
                     if strategy_type == "pure" \
                     else generate_stochastic_strategy_mutants(num_timesteps, Game.strat_len, eps) 

    random_float_index = 0;
    mutant_index       = 0;    
    
    # store current host v. host payoff
    curr_host = host
    pi_xx, _, cc_rate, g1_rate  = Game.get_stats(curr_host, curr_host)

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

        
        # store data
        cc_avg += cc_rate
        g1_avg += g1_rate

    return cc_avg/float(num_timesteps), g1_avg/float(num_timesteps)


# returns CC avgs and G1 avgs for each tested param value
def get_b1_evolution_data(num_timesteps, b1_list, params_dict):
    game = params_dict["game"]

    def get_b1_datapoint(b1):
        game.reset_b1(b1)
        return get_evolution_avgs(num_timesteps, params_dict)

    data = [get_b1_datapoint(b1) for b1 in b1_list]
    return zip(*data)