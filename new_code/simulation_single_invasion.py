import numpy as np
import time

from stochastic_dynamics import *
from helper_functions import *


# returns first succesful mutant strategy and the number of invasion attempts before host succumbed
# @profile
def simulate_invasion(params_dict):
    params_needed = ("N", "eps", "beta", "host", "game", "strategy_type", "max_attempts")
    N, eps, beta, host, Game, strategy_type, max_attempts = get_params(params_needed, params_dict)

    # track how many invasion attempts (up to max attempts)
    num_invasion_attempts = 0

    # set up random variables
    random_floats  = np.random.random(size=max_attempts)
    mutants        = generate_pure_strategy_mutants(max_attempts, Game.strat_len, eps) \
                     if strategy_type == "pure" \
                     else generate_stochastic_strategy_mutants(max_attempts, Game.strat_len, eps) 

    random_float_index = 0;
    mutant_index       = 0;    
    
    # store host v. host payoff
    pi_xx, _     = Game.get_payoffs(host, host)

    # Main Evolution Loop
    while num_invasion_attempts <= max_attempts:

        # get mutant strategy, update mutant index
        mutant = tuple(mutants[mutant_index:mutant_index + Game.strat_len])
        mutant_index += Game.strat_len

        # increment number of invasion attempts
        num_invasion_attempts += 1
        
        # get probability of succession invasion
        pi_xy, pi_yx  = Game.get_payoffs(host,   mutant)
        pi_yy, _      = Game.get_payoffs(mutant, mutant)   

        prob_invasion = get_prob_mutant_fixation(N, beta, pi_xx, pi_xy, pi_yx, pi_yy)

        # get random float, update float index
        random_float = random_floats[random_float_index]
        random_float_index += 1

        if random_float <= prob_invasion:
            #print(strat_to_str(host) + "=>" + strat_to_str(mutant) + ". prob invasion: {:.3f}.".format(prob_invasion))
            return (mutant, num_invasion_attempts)

    raise(ValueError("host " + str(host) + " was not invaded in {:d} attempts.".format(max_attempts)))

# returns a sample distribution over "(first successful mutant, number of invasion attempts)"
def get_invasion_distr(num_trials, params_dict):
    results = [simulate_invasion(params_dict) for _ in range(num_trials)]
    return zip(*results)

# returns a sample distribution over "Prob[random mutant fixates in host population]"
def get_invasion_prob_distr(num_trials, params_dict):
    probs_dist = [0] * num_trials

    params_needed = ("N", "eps", "beta", "host", "game", "strategy_type", "max_attempts")
    N, eps, beta, host, Game, strategy_type, max_attempts = get_params(params_needed, params_dict)

    # set up random variables
    random_floats  = np.random.random(size=max_attempts)
    mutants        = generate_pure_strategy_mutants(max_attempts, Game.strat_len, eps) \
                     if strategy_type == "pure" \
                     else generate_stochastic_strategy_mutants(max_attempts, Game.strat_len, eps) 

    random_float_index = 0;
    mutant_index       = 0;    
    
    # store host v. host payoff
    pi_xx, _     = Game.get_payoffs(host, host)

    # Main Evolution Loop
    for i in range(num_trials):

        # get mutant strategy, update mutant index
        mutant = tuple(mutants[mutant_index:mutant_index + Game.strat_len])
        mutant_index += Game.strat_len
        
        # get probability of succession invasion
        pi_xy, pi_yx  = Game.get_payoffs(host,   mutant)
        pi_yy, _      = Game.get_payoffs(mutant, mutant)   

        prob_invasion = get_prob_mutant_fixation(N, beta, pi_xx, pi_xy, pi_yx, pi_yy)

        probs_dist[i] = prob_invasion

    return probs_dist