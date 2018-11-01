# strategy's avg payoff against N - 1 other individuals in current pop
# does not count individual w/ strategy playing against himself 

def get_avg_strategy_payoff(strategy_index, curr_payoffs, curr_freqs):
    all_payoff  = curr_payoffs[strategy_index,s_active] * curr_freqs;
    self_payoff = curr_payoffs[strategy_index,strategy_index];

    avg_payoff = (all_payoff - self_payoff)/(N-1);
    return avg_payoff

def safe_get_index(elt, list):
    try:
        return s_active.index(new_strategy)
    except ValueError:
        return -1

# updates strategy list, current pop, payoffs, #strategies, etc.
def add_strategy(new_strategy, s_active, s_freqs, \
                 s_payoffs, s_cc_rates, s_game1_rates):

    s_active_index = safe_get_index(new_strategy)

    # no need to update s_payoffs etc if invented strategy already in s_active
    if s_active_index != -1:
        s_freqs[new_strategy_index] += 1
        return

    # if strategy is truly new, add it to s_active & update curr_payoffs
    s_active.append(new_strategy_index)
    s_freqs.append(1)
        
    # expand_curr_payoffs, etc.
    [payoffs, cc_rate, game1_rate] = \
        [get_stats(new_strategy, strat) for strat in s_active]

    np.c_[ curr_payoffs, payoffs ]  



def expand_curr_payoffs(new_strategy):
    new_strategy_index = curr_num_strategies;
    new_strat = strategies_list(curr_pop(new_strategy_index,1));
    
    for j = 1:curr_num_strategies
        
        strat_j = strategies_list(curr_pop(j, 1));
        
        [payoffs, frac_coops, frac_game1] = ...
            lookup_stats(game1, game2, new_strat, strat_j, stationary_dists);

        payoff_i    = payoffs(1);
        payoff_j    = payoffs(2); 
        
        frac_coop_i = frac_coops(1);
        frac_coop_j = frac_coops(2);

        curr_payoffs(new_strategy_index,j) = payoff_i;
        curr_coops(new_strategy_index,j)   = frac_coop_i;
        curr_game1(new_strategy_index,j)   = frac_game1;

        curr_payoffs(j,new_strategy_index) = payoff_j;
        curr_coops(j,new_strategy_index)   = frac_coop_j;
        curr_game1(j,new_strategy_index)   = frac_game1;
    end
end
            

def lose_adherent(strategy_index, s_freqs, s_active, \
                    curr_payoffs, curr_coops, curr_game1):

    s_freqs[strategy_index] -= 1

    if s_freqs[strategy_index] == 0:
        del s_freqs[strategy_index]
        del s_active[strategy_index]

        # shrink current payoff matrix 


        curr_payoffs(index,:) = []; # delete associated row
        curr_payoffs(:,index) = []; # delete associated column
        
        curr_coops(index,:) = []; # delete associated row
        curr_coops(:,index) = []; # delete associated column
        
        curr_game1(index,:) = []; # delete associated row
        curr_game1(:,index) = []; # delete associated column 


def record_timestep_data(timestep)
    # update strategy cumulative totals
    
    cum_strategy_counts[s_active] += s_freqs
    
    # each game contributes 2 values to the overall pool of results; 
    # (N choose 2) games.
    num_contribs = N * (N - 1);
            
    # for each strategy, avg the sum of the contributions of N-1 games
    # (discard 1 game of playing yourself)
    
    # total strategy payoff/coop/game1 in matchup w/other N-1 opponents
    strategy_payoffs = curr_payoffs * s_freqs - np.diag(curr_payoffs); 
    strategy_coops   = curr_coops   * s_freqs - np.diag(curr_coops);
    strategy_game1s  = curr_game1   * s_freqs - np.diag(curr_game1);
    
    # weight by each strategy's freq; sum for overall payoff/coop/game1
    avg_payoff = sum(strategy_payoffs .* curr_pop(:,2)/num_contribs);
    avg_coop   = sum(strategy_coops   .* curr_pop(:,2)/num_contribs);
    avg_game1  = sum(strategy_game1s  .* curr_pop(:,2)/num_contribs);
   
    avg_payoff_data(timestep) = avg_payoff;
    avg_coop_data(timestep)   = avg_coop;
    avg_game1_data(timestep)  = avg_game1;
# 
#         avg_single_coop       = time_vec;
#         avg_single_game1_coop = time_vec;
#         avg_single_game2_coop = time_vec;
#         avg_single_game1      = time_vec;



