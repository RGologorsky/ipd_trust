import numpy as np
import time

from sim_helpers import *

def simulate_timesteps(self):

    start_time = time.time()
    
    # Main Evolution Loop
    for timestep in xrange(T):

        # someone with mutates/invents new strategy
        if self.coin_toss(self.mu):

            new_strategy = self.invent_strategy()
            old_strategy_index = self.choose_strategy()
            
            self.lose_adherent(old_strategy_index)
            self.add_strategy(new_strategy);
            
            
        # someone switches strategies
        else: 
            learner, rolemodel = self.choose_strategy_pair()

            # avg payoff against N - 1 other individuals in the population
            pi_learner   = self.get_avg_strategy_payoff(learner);
            pi_rolemodel = self.get_avg_strategy_payoff(rolemodel);

            imitation_prob = get_imitation_prob(pi_rolemodel, pi_learner);

            
            if self.coin_toss(imitation_prob):
                # learner switches to rolemodel strategy
                self.lose_adherent(learner)
                self.gain_adherent(rolemodel)

        
        self.record_timestep_data(timestep);

    self.elapsed_time = time.time() - start_time;




