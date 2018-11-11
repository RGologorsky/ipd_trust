def record_timestep_data(self, timestep):
    # update strategy cumulative totals
    
    self.s_counts[self.s_active] += self.s_freqs
    
    if self.round_result == (-1,-1):
        # print("timestep ", timestep)
        # print("prior avg cc", self.avg_cc_data[timestep - 1])
        # print("all prior", self.avg_cc_data[:timestep])
        self.avg_cc_data[timestep] = self.avg_cc_data[timestep - 1]
        return

    # each game contributes 2 values to the overall pool of results; 
    # (N choose 2) games.
    num_contribs = self.N * (self.N - 1);
            
    # for each strategy, avg the sum of the contributions of N-1 games
    # (discard 1 game of playing yourself)
    
    # total strategy payoff/coop/game1 in matchup w/other N-1 opponents
    # total_s_payoffs     = np.dot(self.s_payoffs,     self.s_freqs) - np.diag(self.s_payoffs) 
    total_s_cc_rates    = np.matmul(self.s_cc_rates,    self.s_freqs) - np.diag(self.s_cc_rates)
    # total_s_game1_rates = np.dot(self.s_game1_rates, self.s_freqs) - np.diag(self.s_game1_rates)
    
    # weight by each strategy's freq; sum for overall payoff/coop/game1
    # avg_s_payoffs     = np.sum(np.dot(total_s_payoffs,     self.s_freqs)) * 1.0/num_contribs
    avg_s_cc_rates    = np.sum(np.dot(total_s_cc_rates,    self.s_freqs))/num_contribs
    # avg_s_game1_rates = np.sum(np.dot(total_s_game1_rates, self.s_freqs)) * 1.0/num_contribs
   
    # self.avg_payoff_data[timestep] = avg_s_payoffs;
    self.avg_cc_data[timestep]     = avg_s_cc_rates;
    # self.avg_game1_data[timestep]  = avg_s_game1_rates;
# 
#         avg_single_coop       = time_vec;
#         avg_single_game1_coop = time_vec;
#         avg_single_game2_coop = time_vec;
#         avg_single_game1      = time_vec;


try:
            #v = null(np.transpose(Q)-np.ones(Q.shape))
            l, v = sp.eigs(Q.T, k=1, which='LM')

        except Exception as e:
            try: 
                l, v = sp.eigs(Q.T, k=1, which='LM')
                # print("fixed")
            
            except Exception as e:
                print("failed twice")
                print("s1 = {:}, s2 = {:}".format(s1, s2)) 
                print("Q \n {:}".format(Q))
                raise(e)
                

# choose random pair (no replacement) of strategy indices
def old_choose_strategy_pair(self):

    # check if only one strategy in the population
    if len(self.s_active) == 1:
        return -1

    # choose first strategy
    rand1 = self.get_random_float()
    s1_index = choose_one_from_list(self.s_freqs, self.N * rand1)

    # choose another strategy without replacement
    freqs_no_replacement = self.s_freqs[:]
    freqs_no_replacement[s1_index] = 0

    rand2 =  self.get_random_float()
    s2_index = choose_one_from_list(freqs_no_replacement, \
                                    (self.N - self.s_freqs[s1_index]) * rand2)

    # choose which strategy is learner/role model
    return (s1_index, s2_index) if rand1 < rand2 else (s2_index, s1_index)


# choose random pair (no replacement) of strategy indices
def slow_choose_strategy_pair(self):

    # only one strategy in the population
    if len(self.s_active) == 1:
        return -1

    s_weights = [s_freq/float(self.N) for s_freq in self.s_freqs]
    return np.random.choice(len(self.s_active),size=2,replace=False, p=s_weights)

