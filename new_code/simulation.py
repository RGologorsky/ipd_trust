import numpy as np
import time

from stochastic_dynamics import *
from helpers import *


def generate_pure_strategy_mutants(num_mutants, strat_len, eps):

    # generate binary 0/1 pure strategies
    rand_nums = np.random.randint(2, size = num_mutants * strat_len)

    # rescale to eps/1-eps
    return [num * (1-2*eps) + eps for num in rand_nums]

def generate_stochastic_strategy_mutants(num_mutants, strat_len, eps):

    # generate Unif(0,1) stochastic strategies
    rand_nums = np.random.uniform(low=eps, high=1.0-eps, size = num_mutants * strat_len)

    # rescale to Unif(eps, 1-eps)
    return [num * (1-2*eps) + eps for num in rand_nums]

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

def get_invasion_distr(num_trials, params_dict):
    results = [simulate_invasion(params_dict) for _ in range(num_trials)]
    return zip(*results)

