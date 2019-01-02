# Code Documentation

## Game Mechanics

I implemented 4 game types. Each game type is implemented in its own class:
* **S_02_Class** implements IPD over the 2-dim space of reactive strategies (p,q). 
* **S_04_Class** implements IPD over the 4-dim space of memory-1 strategies (p_cc, p_cd, p_dc, p_dd).
* **S_12_Class** implements IPD over the 12-dim space of reactive two-game strategies (p_1cc, p_1cd, p_1dc, p_1dd, q_1cc, q_1cd, q_1dc, q_1dd, x_cc, x_cd, x_dc, x_dd)
* **S_16_Class** implements IPD over the 16-dim space of memory-1 two-game strategies (p_1cc, p_1cd, p_1dc, p_1dd, q_1cc, q_1cd, q_1dc, q_1dd, x_1cc, x_1cd, x_1dc, x_1dd, x_2cc, x_2cd, x_2dc, x_2dd).

Each specific game class has the following structure:
1. Class variables: 
	- **length of a strategy in this game** (e.g. strat_len = 2 for reactive strategies (p, q) and strat_len = 4 for memory-1 strategies (p_cc, p_cd, p_dc, p_dd).
	- **definition of strategy ALLD** (e.g. ALLD = (0,0) or ALLD = (0,0,0,0)).


2. Instance variables: **the values to use in the payoff matrix**, such as *c=1* and *b=10* or *c=1*,*b1=10*, and *b2=5*. These are set during initialization, and are used to define each player's payoff.
3. Instance Methods.
	* **set_payoffs(self)**. This function uses the payoff matrix values to set player 1 and player 2's payoff values for each game state.
	* **generate_transition_matrix(self, s1, s2)**. This function takes in two strategies and returns the corresponding transition matrix.

 Each specific game inherits from the general **Game class** two methods:
 1. **get_stationary_dist(self, s1, s2, eps=1e-15)**. This function takes in two strategies, s1 and s2, generates the corresponding transition matrix, and returns the resulting stationary distribution (to the specified precision *eps*).
 2. **get_payoffs(self, s1, s2)**. This function takes in two strategies, gets the stationary distribution over game states, and returns the resulting average payoff for each strategy.

## Stochastic Dynamics

The invader fixation probability is calculated in *stochastic_dynamics.py*. This file defines:

1. **get_prob_imitation(beta, pi_learner, pi_rolemodel)**. This calculates the probability that an individual with the learner strategy will switch to the rolemodel's strategy. It is currently implemented using the Fermi function, with selection pressure beta, according to Traulsen et al (2006).

2. **get_prob_invader_decr(j, N, beta, pi_invader, pi_host)**. This calculates **T<sub>j</sub><sup>-</sup>**, the probability that the number of invaders in the population decreases from *j* to *j-1*, where the total population size is *N* and there are no self-interactions.
3. **get_prob_invader_incr(j, N, beta, pi_invader, pi_host)**. This calculates **T<sub>j</sub><sup>+</sup>**, the probability that the number of invaders in the population increases from *j* to *j-1*, where the total population size is *N*.
4. **get_invader_decr_incr_ratio(j, N, beta, pi_xx, pi_xy, pi_yx, pi_yy)**. This calculates the ratio **T<sub>j</sub><sup>-</sup>**/**T<sub>j</sub><sup>+</sup>**  where there are *j* invaders in a population of size *N*, host vs. host average payoff is pi_xx, invader vs. invader average payoff is pi_yy, and selection pressure is *beta*.
5. **get_prob_mutant_fixation(N, beta, pi_xx, pi_xy, pi_yx, pi_yy)**. This calculates the probablity that a single mutant invader will fixate in the population. 

## Simulation

In *simulation.py*, I simulate the occurrence of (rare) mutations until the host strategy is invaded or until the maximum number of mutants is generated.
The file contains the following functions:

1. **generate_pure_strategy_mutants(num_mutants, strat_len, eps)**. This function generates an array of mutants with randomly generated pure strategies (i.e. cooperate/defect probabilities are eps/1-eps).

2. **generate_stochastic_strategy_mutants(num_mutants, strat_len, eps)**. This function generates an array of mutants with randomly generated stochastic strategies (i.e. cooperate/defect probabilities are drawn from Unif(eps,1-eps)).

3. **simulate_invasion(params_dict)**. This function simulates the occurrence of random mutants probabilistically taking over the host strategy. Specifically, we stars with a homogeneous population where everyone is playing the host strategy, and we generate mutants until one of them takes over the host strategy or until the maximum number of mutants is generated. If a mutant successfully invades, the function returns the successful mutant strategy and the number of invasion attempts; otherwise, the function returns False.
    
4. **get_invasion_distr(num_trials, params_dict)**. This function simulates invasion of the host population several times in order to obtain a distribution over the types of mutants that successfully invade and over the number of invasion attempts until success.

