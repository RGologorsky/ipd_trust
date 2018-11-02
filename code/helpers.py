# Helper Functions
import numpy as np
from game import mc_estimate

# Static methods
def sigmoid(x):
    return 1.0/(1.0 + np.exp(x))

def get_imitation_prob(beta, pi_r, pi_l):
    return sigmoid(-1.0 * beta * (pi_r - pi_l));

def safe_get_index(elt, lst):
    try:
        return lst.index(elt)
    except ValueError:
        return -1

def add_row(vec, matrix):
    try:
        return np.r_[matrix,[vec]]
    except Exception as e:
        print "Adding row error. Row {:}.\n Matrix:\n {:} ".format(vec, matrix)
        raise(e)

def add_col(vec, matrix):
    try:
        return np.c_[matrix, vec]
    except Exception as e:
        print "Adding col error. Col {:}.\n Matrix:\n {:} ".format(vec, matrix)
        raise(e)

def del_row(index, matrix):
    return np.r_[matrix[:index,], matrix[index+1:,]]

def del_col(index, matrix):
    return np.c_[matrix[:,:index], matrix[:,index+1:]]

# Class methods
def get_random_float(self):
    random_float = self.random_floats[self.random_floats_index]
    self.random_floats_index += 1
    return random_float

def coin_toss(self, p):
    return (self.get_random_float() <= self.mu)

def invent_strategy(self):
    new_strategy = self.invented_strategies[self.invent_index];
    self.invent_index += 1
    return new_strategy

# choose random strategy
def choose_strategy(self):
    random_weight = self.get_random_float()
    for index, freq in enumerate(self.s_freqs):
        random_weight -= float(freq)/self.N;
        if random_weight <= 0:
            return index

# choose random pair (no replacement) of strategy indices
def choose_strategy_pair(self):

    # only one strategy in the population
    if len(self.s_active) == 1:
        return -1

    s_weights = [s_freq/float(self.N) for s_freq in self.s_freqs]
    return np.random.choice(len(self.s_active),size=2,replace=False, p=s_weights)

def gain_adherent(self, strategy_index):
    try:
        self.s_freqs[strategy_index] += 1
    except Exception as e:
        print "strategy_index = {:}".format(strategy_index)
        self.print_status()

        raise(e)

def get_avg_strategy_payoff(self, strategy_index):
    # self.print_status()

    all_payoff  = np.dot(self.s_payoffs[strategy_index], self.s_freqs)
    self_payoff = self.s_payoffs[strategy_index,strategy_index];

    avg_payoff = (all_payoff - self_payoff) * 1.0/(self.N-1);
    return avg_payoff

# updates strategy list, current pop, payoffs, #strategies, etc.
def add_strategy(self, new_strategy):

    s_active_index = safe_get_index(new_strategy, self.s_active)

    # no need to update s_payoffs etc if invented strategy already in s_active
    if s_active_index != -1:
        self.s_freqs[s_active_index] += 1
        return
        
    # get new strategy's stats against currently active strategies
    [new_s_payoffs, strat_payoffs, new_s_cc_rates, new_s_game1_rates] = \
        zip(*[self.game.mc_estimate(new_strategy, strat) for strat in self.s_active])

    s_self_payoff, _, s_self_cc_rate, s_self_game1_rate = \
        self.game.mc_estimate(new_strategy, new_strategy)
    
    # update list of active strategies
    self.s_active.append(new_strategy)
    self.s_freqs.append(1)

    # add this strategy's stats to the matrix containing active strategy stats
    self.s_payoffs     = add_row(new_s_payoffs, self.s_payoffs)
    self.s_cc_rates    = add_row(new_s_cc_rates, self.s_cc_rates)
    self.s_game1_rates = add_row(new_s_game1_rates, self.s_game1_rates)

    col1 = list(strat_payoffs)
    col2 = list(new_s_cc_rates)
    col3 = list(new_s_game1_rates)
    
    col1.append(s_self_payoff)
    col2.append(s_self_cc_rate)
    col3.append(s_self_game1_rate)


    self.s_payoffs     = add_col(col1, self.s_payoffs)
    self.s_cc_rates    = add_col(col2, self.s_cc_rates)
    self.s_game1_rates = add_col(col3, self.s_game1_rates)  
    

def lose_adherent(self, strategy_index):

    self.s_freqs[strategy_index] -= 1

    if self.s_freqs[strategy_index] == 0:
        del self.s_freqs[strategy_index]
        del self.s_active[strategy_index]

        # shrink current payoff matrix 
        self.s_payoffs     = del_row(strategy_index, self.s_payoffs)
        self.s_cc_rates    = del_row(strategy_index, self.s_cc_rates)
        self.s_game1_rates = del_row(strategy_index, self.s_game1_rates)

        self.s_payoffs     = del_col(strategy_index, self.s_payoffs)
        self.s_cc_rates    = del_col(strategy_index, self.s_cc_rates)
        self.s_game1_rates = del_col(strategy_index, self.s_game1_rates)  


def record_timestep_data(self, timestep):
    # update strategy cumulative totals
    
    # self.s_counts[self.s_active] += self.s_freqs
    
    # each game contributes 2 values to the overall pool of results; 
    # (N choose 2) games.
    num_contribs = self.N * (self.N - 1);
            
    # for each strategy, avg the sum of the contributions of N-1 games
    # (discard 1 game of playing yourself)
    
    # total strategy payoff/coop/game1 in matchup w/other N-1 opponents
    # total_s_payoffs     = np.dot(self.s_payoffs,     self.s_freqs) - np.diag(self.s_payoffs) 
    total_s_cc_rates    = np.dot(self.s_cc_rates,    self.s_freqs) - np.diag(self.s_cc_rates)
    # total_s_game1_rates = np.dot(self.s_game1_rates, self.s_freqs) - np.diag(self.s_game1_rates)
    
    # weight by each strategy's freq; sum for overall payoff/coop/game1
    # avg_s_payoffs     = np.sum(np.dot(total_s_payoffs,     self.s_freqs)) * 1.0/num_contribs
    avg_s_cc_rates    = np.sum(np.dot(total_s_cc_rates,    self.s_freqs)) * 1.0/num_contribs
    # avg_s_game1_rates = np.sum(np.dot(total_s_game1_rates, self.s_freqs)) * 1.0/num_contribs
   
    # self.avg_payoff_data[timestep] = avg_s_payoffs;
    self.avg_cc_data[timestep]     = avg_s_cc_rates;
    # self.avg_game1_data[timestep]  = avg_s_game1_rates;
# 
#         avg_single_coop       = time_vec;
#         avg_single_game1_coop = time_vec;
#         avg_single_game2_coop = time_vec;
#         avg_single_game1      = time_vec;
