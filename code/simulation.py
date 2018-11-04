import numpy as np
import time

from helpers import *
from printing import *

# @profile
def simulate_timesteps(self):

    start_time = time.time()
    
    # Main Evolution Loop
    for timestep in range(self.T):
        # self.print_status()

        # someone with mutates/invents new strategy (must in homogenous population)
        if self.coin_toss(self.mu) or len(self.s_active) == 1:

            new_strategy = self.invent_strategy()
            old_strategy_index = self.choose_strategy()
            
            # keep old strategy number for record
            old_strategy = self.s_active[old_strategy_index]


            # print("mutation: {}->{}".format(new_strategy, self.s_active[old_strategy_index]))

            self.lose_adherent(old_strategy_index)
            self.add_strategy(new_strategy);

            # self.print_freq_total("after coin toss mu")
            
            
        # someone switches strategies
        else: 
            s_learner_index, s_rolemodel_index = self.choose_strategy_pair()

            # avg payoff against N - 1 other individuals in the population
            pi_learner   = self.get_avg_strategy_payoff(s_learner_index);
            pi_rolemodel = self.get_avg_strategy_payoff(s_rolemodel_index);

            imitation_prob = get_imitation_prob(self.beta, pi_rolemodel, pi_learner);

            
            if self.coin_toss(imitation_prob):

                # print("imitation {}->{}. learner = {:.2f}, rolemodel = {:.2f}, Prob = {:.2f}".format(
                #                    self.s_active[s_learner_index], \
                #                    self.s_active[s_rolemodel_index], \
                #                    pi_learner,
                #                    pi_rolemodel,
                #                     imitation_prob))

                # learner switches to rolemodel strategy
                self.gain_adherent(s_rolemodel_index)
                self.lose_adherent(s_learner_index)

                # self.print_freq_total("after coin toss imitiation prob")

        
        self.record_timestep_data(timestep);

    self.elapsed_time = time.time() - start_time
    self.final_avg_cc_rate = np.mean(self.avg_cc_data)
    self.print_results()
    self.plot_timestep_data()

    return self.final_avg_cc_rate




