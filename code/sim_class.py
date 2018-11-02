import numpy as np

class Sim:

    # class methods
    from plotting import plot_timestep_data
    from game import mc_estimate
    from helpers import *
    from printing import *
    from simulation import simulate_timesteps

    # initialize strategy population to have everyone playing s_initial (=ALL-D)
    def init_strategy_population(self,  s_initial=0):

        # currently active strategies and their frequencies
        self.s_active = [s_initial]
        self.s_freqs  = [self.N]

        new_s_payoffs, _, new_s_cc_rates, new_s_game1_rates = \
            self.mc_estimate(s_initial, s_initial)

        # matrix of current strategy payoffs against each other
        self.s_payoffs     = new_s_payoffs     * np.ones((1,1))
        self.s_cc_rates    = new_s_cc_rates    * np.ones((1,1))
        self.s_game1_rates = new_s_game1_rates * np.ones((1,1))

    def __init__(self, T):

        # Settings
        self.do_plots = True

        # Game values
        self.b1 = 1.8; # benefit coop in Game 1
        self.b2 = 1.2; # benefit coop in Game 2
        self.c  = 1;   # cost to coop in both games

         #player1, player2 payoffs for outcomes 1CC, ..., 1DD, 2CC, ..., 2DD
        b1, b2, c = self.b1, self.b2, self.c
        self.p1_payoffs = [b1-c, -c, b1, 0, b2-c, -c, b2, 0];
        self.p2_payoffs = [b1-c, b1, -c, 0, b2-c, b2, -c, 0];

        # Strategies in [0,1]^16
        self.max_num_strategies = 2**16

        # Evolution Parameters
        self.T    = T; # timesteps
        self.N    = 100;   # population size
        self.beta = 2;     # selection pressure
        self.mu   = 0.01;  # mutation probability
        self.eps  = 0;     # noise

        # cumulative strategy counts
        self.s_counts = np.zeros(self.max_num_strategies) 

        # time data vectors store strategy population data at each time step
        self.avg_cc_data     = np.zeros(self.T);
        self.avg_payoff_data = np.zeros(self.T); 
        self.avg_game1_data  = np.zeros(self.T); 


        # Randomness

        """  
            (1) choose to invent or learn this round
            (2) if invent, 
                - choose strategy that lost adherent 
                - invent  a strategy from 1 ... max_num_strategies
            (3) if learn, choose learner and rolemodel
        """
        self.random_floats       = np.random.random(size=3*self.T)
        self.invented_strategies = np.random.randint(self.max_num_strategies, \
                                                     size=int(2*self.mu*self.T))

        self.random_floats_index = 0;
        self.invent_index        = 0;



