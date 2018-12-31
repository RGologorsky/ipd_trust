import numpy as np
import time

from helpers import *


# @profile
def simulate_invasion(params_dict):
    params_needed = ("N", "eps", "beta", "host", "game", "max_attempts")
    N, eps, beta, host, Game, max_attempts = get_params(params_needed, params_dict)

    # track how many invasion attempts (up to max attempts)
    num_invasion_attempts = 0

    # set up random variables
    random_floats  = np.random.random(size=max_attempts)
    invaders       = np.random.uniform(low=eps, high=1.0-eps, \
                                        size = max_attempts * Game.strat_len)

    random_floats_index = 0;
    invader_index       = 0;    
    
    # store host v. host payoff
    pi_xx, _     = Game.get_payoffs(host, host)

    # Main Evolution Loop
    while True:

        # get invader strategy
        start = invader_index
        invader = tuple(invaders[invader_index:invader_index + Game.strat_len])
        
        # update invader index
        invader_index += Game.strat_len

        # increment number of invasion attempts
        num_invasion_attempts += 1
        

        # get probability of succession invasion
        pi_xy, pi_yx  = Game.get_payoffs(host,    invader)
        pi_yy, _      = Game.get_payoffs(invader, invader)   

        prob_invasion = get_prob_mutant_fixation(N, beta, pi_xx, pi_xy, pi_yx, pi_yy)

        #print("prob invasion: {:.2f}".format(prob_invasion))
        random_float = random_floats[random_floats_index]
        random_floats_index += 1

        if random_float <= prob_invasion:
            return (invader, num_invasion_attempts)
        


def get_invasion_distr(num_invasions, params_dict):
    results = [simulate_invasion(params_dict) for _ in range(num_invasions)]
    return zip(*results)

