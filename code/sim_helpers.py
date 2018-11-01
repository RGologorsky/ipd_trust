# Helper Functions
import init_game
import constants
import numpy as np

# Static methods
def sigmoid(x):
    return 1.0/(1.0 + np.exp(x))

def get_imitation_prob(pi_r, pi_l):
    return sigmoid(-beta * (pi_r - pi_l));

def safe_get_index(elt, list):
    try:
        return s_active.index(new_strategy)
    except ValueError:
        return -1

def add_row(vec, matrix):
    return np.r_[matrix,[vec]]

def add_col(vec, matrix):
    return np.c_[matrix, vec]

def del_row(vec, matrix):
    pass

# Class methods
def coin_toss(self, p):
    result = (self.random_floats[self.random_floats_index] <= self.mu)
    self.random_floats_index += 1
    return result

def invent_strategy(self):
    new_strategy = self.random_strategies[self.invent_index];
    self.invent_index += 1
    return new_strategy

def get_strategy(self, random_weight):
    for index, freq in enumerate(self.s_freqs):
        random_weight -= float(freq)/self.N;
        if random_weight <= 0:
            return index

def choose_strategy(self):
    random_weight = self.random_strategies[self.choose_index]
    self.choose_index += 1
    return self.get_strategy_index(random_weight)

def choose_strategy_pair(self):
    s_weights = self.s_freqs * 1.0/self.N
    return np.random.choice(self.s_active,size=2,replace=False, p=s_weights)

def gain_adherent(self, strategy_index):
    self.s_freqs[strategy_index] += 1

def get_avg_strategy_payoff(self, strategy_index):
    all_payoff  = np.dot(self.s_payoffs[strategy_index], self.s_freqs)
    self_payoff = self.s_payoffs[strategy_index,strategy_index];

    avg_payoff = (all_payoff - self_payoff) * 1.0/(N-1);
    return avg_payoff

# updates strategy list, current pop, payoffs, #strategies, etc.
def add_strategy(new_strategy):

    s_active_index = safe_get_index(new_strategy)

    # no need to update s_payoffs etc if invented strategy already in s_active
    if s_active_index != -1:
        s_freqs[new_strategy_index] += 1
        return

    # if strategy is truly new, add it to s_active & update curr_payoffs
    self.s_active.append(new_strategy_index)
    self.s_freqs.append(1)
        
    # expand_curr_payoffs, etc.
    [payoffs, cc_rate, game1_rate] = \
        [mc_estimate(new_strategy, strat) for strat in s_active]

    self.s_payoffs  



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




# old_strategy lost adherent
        curr_pop(old_strategy_index,2) = curr_pop(old_strategy_index,2) - 1; 
        
        if curr_pop(old_strategy_index,2) == 0:
            # old_strategy went extinct in current population, delete
            delete_strategy(old_strategy_index)
        

# strategy's avg payoff against N - 1 other individuals in current pop
# does not count individual w/ strategy playing against himself 
def get_avg_strategy_payoff(strategy_index):
    all_payoff = curr_payoffs(strategy_index,:) * curr_pop(:,2);
    avg_payoff = (all_payoff - curr_payoffs(strategy_index,strategy_index))/(N-1);

# updates strategy list, current pop, payoffs, #strategies, etc.
def add_strategy(new_strategy)
    [already_listed,strategy_index] = ...
            ismember(new_strategy,strategies_list(1:total_num_strategies));
        
    already_in_pop = false;
        
    if already_listed # check if curr pop has the random strategy 
        [already_in_pop, pop_index] = ...
            ismember(strategy_index,curr_pop(1:curr_num_strategies, 1));

        if already_in_pop
            curr_pop(pop_index,2) = curr_pop(pop_index,2) + 1;
        else
            # update current pop #strategies(also used as index)
            curr_num_strategies = curr_num_strategies + 1;
            curr_pop(curr_num_strategies,:) = [strategy_index 1];
        end

    else # strategy not listed, so not in current pop either.

        # total num strategies also used as an index 
        total_num_strategies = total_num_strategies + 1;
        curr_num_strategies  = curr_num_strategies  + 1;

        strategies_list(total_num_strategies)     = new_strategy;
        cum_strategy_counts(total_num_strategies) = 0;

        curr_pop(curr_num_strategies,:) = [total_num_strategies 1];
    end

    if ~already_in_pop
        # calculate payoffs for newly added strategy
        expand_curr_payoffs()
    end
end

def expand_curr_payoffs():
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
   
            

# deletes a strategy (updates current pop, #strategies, payoffs, etc)
def delete_strategy(strategy_index)
    curr_pop(strategy_index,:) = []; # delete associated row
    shrink_curr_payoffs(strategy_index)
    # curr_num_strategies also serves as index
    curr_num_strategies = curr_num_strategies - 1; 

def shrink_curr_payoffs(index)
    curr_payoffs(index,:) = []; # delete associated row
    curr_payoffs(:,index) = []; # delete associated column
    
    curr_coops(index,:) = []; # delete associated row
    curr_coops(:,index) = []; # delete associated column
    
    curr_game1(index,:) = []; # delete associated row
    curr_game1(:,index) = []; # delete associated column 


def record_timestep_data(timestep)
    # update strategy cumulative totals
    
    indices_in_play = curr_pop(:,1);
    # assignin('base', 'curr_pop', curr_pop)
    # assignin('base', 'cum_strategy_counts', cum_strategy_counts)
    
    cum_strategy_counts(indices_in_play) = ...
        cum_strategy_counts(indices_in_play) + curr_pop(:,2);
    
    # each game contributes 2 values to the overall pool of results; 
    # (N choose 2) games.
    num_contribs = N * (N - 1);
            
    # for each strategy, avg the sum of the contributions of N-1 games
    # (discard 1 game of playing yourself)
    
    # total strategy payoff/coop/game1 in matchup w/other N-1 opponents
    strategy_payoffs = curr_payoffs * curr_pop(:,2) - diag(curr_payoffs); 
    strategy_coops   = curr_coops   * curr_pop(:,2) - diag(curr_coops);
    strategy_game1s  = curr_game1   * curr_pop(:,2) - diag(curr_game1);
    
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


function plot_timestep_data()
   
    figure(1);
    clf;
    
    subplot(2,2,1);
    plot(time_vec, avg_coop_data); 
    title('Evolution of Avg. Cooperation Frequency');
    xlabel('Timestep');
    ylabel('Avg. Fraction of Cooperation');

    subplot(2,2,2); 
    
    plot(time_vec, avg_payoff_data);
    title('Evolution of Overall Avg. Payoff');
    xlabel('Timestep');
    ylabel('Avg. Payoff');
    
    subplot(2,2,3); 
    plot(time_vec, avg_game1_data);  
    title('Evolution of Avg. Game1 Frequency');
    xlabel('Timestep');
    ylabel('Avg. Fraction of Time in Game1');
    
    params_desc = sprintf('Parameters: \n b1 = #1.2f, \n beta = #.2f,\n T = 10^{#d}, \n eps = #.2f, \n mu = #.2f', ...
        b1, beta, log10(T), eps, mu);
    
    values_desc = sprintf('Mean Values: \n payoff = #.3f, \n coop = #.3f, \n game1 = #.3f \n Elapsed Time = #d min', ...
        final_avg_payoff, final_avg_coop, final_avg_game1, round(elapsed_time/60, 0));
    
    strategies_desc = sprintf('Most Abundant Strategies/Freq: \n #d/#.3f \n #d/#.3f \n #d/#.3f', ...
        top_3_strategies(1), top_3_abundances(1), ...
        top_3_strategies(2), top_3_abundances(2), ...
        top_3_strategies(3), top_3_abundances(3));

    annotation('textbox', [0.49 0.01 0.16 0.48], 'String', ...
        {params_desc}, ...
        'FontSize',14,...
        'Color',[0.84 0.16 0]);
    
    annotation('textbox', [0.65 0.01 0.18 0.48], 'String', ...
        {values_desc}, ...
        'FontSize',14,...
        'Color',[0.84 0.16 0]);
    
    annotation('textbox', [0.83 0.01 0.15 0.48], 'String', ...
        {strategies_desc}, ...
        'FontSize',14,...
        'Color',[0.84 0.16 0]);
end
