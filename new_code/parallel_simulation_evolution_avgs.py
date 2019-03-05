import numpy as np
import time

from stochastic_dynamics import *
from helper_functions import *

# returns CC and G1 average over evolutionary timeframe
# @profile
#from concurrent import futures

from multiprocessing import Queue
import multiprocessing as mp

def get_evolution_avgs(num_timesteps, params_dict, b1, spe_list):

        #num_timesteps, params_dict, b1, spe_list = arg_tuple
        #print(num_timesteps, params_dict,b1, spe_list)

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

def get_chunk(num_timesteps, params_dict, b1_list, spe_d):
    res = zip (*[get_evolution_avgs(num_timesteps, params_dict, b1, spe_d[round(b1,2)]) for b1 in b1_list])
    return res

# returns CC avgs and G1 avgs for each tested param value
def get_b1_evolution_data(num_timesteps, b1_list, params_dict, spe_d):

    one_third = int(len(b1_list)/3)

    first_third = b1_list[:one_third]
    second_third = b1_list[one_third:2*one_third]
    last_third = b1_list[2*one_third:]

    p1 = mp.Process(target=get_chunk, args=(num_timesteps, params_dict, first_third, spe_d)) 
    p1.start()

    p2 = mp.Process(target=get_chunk, args=(num_timesteps, params_dict, second_third, spe_d)) 
    p2.start()

    p3 = mp.Process(target=get_chunk, args=(num_timesteps, params_dict, last_third, spe_d)) 
    p3.start()
   
    # wait until process 1 is finished 
    p1.join() 
    p2.join() 
    p3.join()
  
    # both processes finished 
    print("Done!") 

    return p1.results + p2.results + p3.results

    # for b1 in b1_list:
    #     print("b1 = {:.2f}, len = {:d}".format(b1, len(spe_d[round(b1,2)])))

    #arg_list = [(num_timesteps, params_dict, b1, spe_d[round(b1,2)]) for b1 in b1_list]

    #ex = futures.ProcessPoolExecutor()
    #results = ex.map(get_evolution_avgs, arg_list) 

    # pool = mp.Pool()
    # results = pool.map(get_evolution_avgs, arg_list, chunksize=8)
    # pool.close()
    # pool.join()      

    # pool = mp.Pool()
    # results = [pool.apply(get_evolution_avgs, args=(arg, )) for arg in arg_list]
    # pool.close()
    # pool.join()      
    # return zip (*results)