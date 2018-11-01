import numpy as np

class Sim:

    def __init__(self):

        # Settings
        self.do_plots = True

        # Game values
        self.b1 = 1.8; # benefit coop in Game 1
        self.b2 = 1.2; # benefit coop in Game 2
        self.c  = 1;   # cost to coop in both games

        # Strategies in [0,1]^16
        self.max_num_strategies = 2**16

        # Evolution Parameters
        self.T    = 10**6; # timesteps
        self.N    = 100;   # population size
        self.beta = 2;     # selection pressure
        self.mu   = 0.01;  # mutation probability
        self.eps  = 0;     # noise

        # Simulation Parameters
        
        # currently active strategies and their frequencies
        self.s_active = np.zeros(1) 
        self.s_freqs  = np.zeros(1) 

        # cumulative strategy counts
        self.s_counts = np.zeros(self.max_num_strategies) 

        # matrix of current strategy payoffs against each other
        self.s_payoffs     = np.zeros(1,1)
        self.s_cc_rates    = np.zeros(1,1)
        self.s_game1_rates = np.zeros(1,1)

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
        self.random_floats       = np.random.random(size=2*self.T)
        self.invented_strategies = np.random.randint(self.max_num_strategies, \
                                                     size=int(2*self.mu*self.T))

        self.random_floats_index = 0;
        self.invent_index        = 0;


    def init_population(self,  s_initial):
        # initialize strategy population to have everyone playing s_initial = ALL-D.
        self.s_active[0] = s_initial;
        self.s_freqs[0]  = self.N
        self.curr_len_s_active = 1

