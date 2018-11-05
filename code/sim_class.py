import numpy as np

class Sim:

    # class methods
    from plotting import plot_timestep_data
    # from game import mc_estimate
    from helpers import coin_toss, get_random_float, invent_strategy, \
                        choose_strategy, choose_strategy_pair, gain_adherent, \
                        get_avg_strategy_payoff, add_strategy, \
                        lose_adherent, record_timestep_data

    from printing import print_num_s_active, print_freq_total, print_status, \
                         print_results

    from simulation import simulate_timesteps

    # initialize strategy population to have everyone playing s_initial (=ALL-D)
    def init_strategy_population(self,  s_initial=0):

        # currently active strategies and their frequencies
        self.s_active = [s_initial]
        self.s_freqs  = [self.N]

        new_s_payoff, _, new_s_cc_rate, _, new_s_game1_rate = \
            self.game.get_stats(s_initial, s_initial)

        # matrix of current strategy payoffs against each other
        self.s_payoffs     = new_s_payoff     * np.ones((1,1))
        self.s_cc_rates    = new_s_cc_rate    * np.ones((1,1))
        self.s_game1_rates = new_s_game1_rate * np.ones((1,1))

        self.hist = ""


    def __init__(self, T, game, do_plots=False):

        # Settings
        self.do_plots = do_plots

        # Game: encapsulates b,c values, rules, strategy space.
        self.game = game
        self.max_num_strategies = game.max_num_strategies

        # Evolution Parameters
        self.T    = T; # timesteps
        self.N    = 100;   # population size
        self.beta = 2;     # selection pressure
        self.mu   = 0.01;  # mutation probability
        
        # cumulative strategy counts
        self.s_counts = np.zeros(self.max_num_strategies) 

        # time data vectors store strategy population data at each time step
        self.avg_cc_data     = np.zeros(self.T);
        self.avg_payoff_data = np.zeros(self.T); 
        self.avg_game1_data  = np.zeros(self.T); 

        self.hist = ""


        # Randomness

        """  
            (1) choose to invent or learn this round
            (2) if invent, 
                - choose strategy that lost adherent 
                - invent  a strategy from 1 ... max_num_strategies
            (3) if learn, choose learner and rolemodel
        """

        """ random float
            - each timestep, coin toss for mu: T
            - if invent (mu), once to choose old strategy: T * mu
            - if imitate (1-mu), coin toss for imitation prob: T * (1 - mu)
            - if imitate, twice to choose learner/rolemodel: 2* T * (1-mu) 

            Total: 2T + 2 (1-mu)T = (4-2*mu) T
        """

        self.random_floats       = np.random.random(size=int(self.T *(4-1*self.mu)))
        self.invented_strategies = np.random.randint(self.max_num_strategies, \
                                                     size=int(2*self.mu*self.T))

        self.random_floats_index = 0;
        self.invent_index        = 0;



