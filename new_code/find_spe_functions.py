import numpy as np
from helper_functions import get_index, bin_array

# only for two-games. Returns dictionary d; For strat vs. strat, d[state_id] = next_state
def get_Q_dictionary(strat, game):
	Q = game.generate_transition_matrix(strat, strat)

	return {state_num: game.state_to_num[tuple(np.matmul(game.num_to_state[state_num], Q))] \
			for state_num in range(game.num_states)}

# returns dictionary d; d[state_id] = player 2's payoff in that state 
def get_p2_payoff_dictionary(strat, game):
	return {num: game.p2_payoffs[num] for num in range(game.num_states)}

# returns the seen states until a cycle is created and the cycle start index
def get_cycle_info(start_state, Q_dict):

	# initialize
	curr_state   = start_state
	seen_states  = []

	cycle_start_index = -1

	# 8 states => cycle within 9 steps
	while cycle_start_index == -1:

		# add state
		seen_states.append(curr_state)

		# move forward one step
		curr_state  = Q_dict[curr_state]

		# update whether cycle are seen
		cycle_start_index = get_index(curr_state, seen_states)

	# found cycle
	cycle_len = len(seen_states) - cycle_start_index
	return (seen_states, cycle_start_index, cycle_len)

# returns whether strat vs. strat ends in full coop given start state
def is_full_coop_an_absorbing_state(start_state, Q_dict):
	(seen_states, cycle_start_index, cycle_len) = get_cycle_info(start_state, Q_dict)
	return (seen_states[cycle_start_index] == 0 and cycle_len == 1)

# returns average payoff per round, w/round 0 = start state.
def get_avg_round_payoff(start_state, delta, Q_dict, payoff_dict):

	expected_num_rounds = 1.0/(1.0 - delta)
	seen_states, cycle_start_index, cycle_len = get_cycle_info(start_state, Q_dict)

	# calculating payoffs
	cycle_discount_factor =  1.0/(1.0 - delta**cycle_len)

	discounted_payoff = 0

	for i, state in enumerate(seen_states):

		if i < cycle_start_index:
			discounted_payoff += payoff_dict[state] * delta**i
		else:
			discounted_payoff += payoff_dict[state] * delta**i * cycle_discount_factor

	# return average payoff per round
	return discounted_payoff/expected_num_rounds


# returns set of states reachable by a single deviations 
# baseline action = 2D -> 2DC and 2DD possible deviations (0 -> 6,7)
# basline action  = 2C -> 2CC and 2CD possible deviations (1 -> 4,5)
# baseline action = 1D -> 1DC and 1DD possible deviations (0 -> 2,3)
# basline action  = 1C -> 1CC and 1CD possible deviations (1 -> 0,1)
def possible_dev_states(prior_state, strat):

	# S12 vs. S16 transition decision based on prior state
	if len(strat) == 12:
		baseline_transition = strat[8 + prior_state % 4]
	else:
		baseline_transition = strat[8 + prior_state]

	# Game 2 states are always reachable
	g2_baseline_action = strat[4 + prior_state % 4]
	single_dev_states = {-2*g2_baseline_action + 6, -2*g2_baseline_action + 7}

	# Game 1 states might also reachable
	if baseline_transition == 1:
		g1_baseline_action = strat[prior_state % 4]
		single_dev_states.update({-2*g1_baseline_action + 2, -2*g1_baseline_action + 3})
		
	return single_dev_states

# checks whether (strategy, strategy) is an SPE
def is_spe(strat, game, delta):
	Q_dict      = get_Q_dictionary(strat, game) 
	payoff_dict = get_p2_payoff_dictionary(strat, game)

	# check all possible single deviations
	for prior_state in range(game.num_states):

		baseline_start_state = Q_dict[prior_state]
		all_possible_devs = possible_dev_states(prior_state, strat)

		# remove baseline next state from consideration 
		all_possible_devs.discard(baseline_start_state)

		baseline_payoff = get_avg_round_payoff(baseline_start_state, delta, Q_dict, payoff_dict)
		dev_payoffs = [get_avg_round_payoff(start_state, delta, Q_dict, payoff_dict) 
						for start_state in all_possible_devs
					]

		max_dev_payoff = max(dev_payoffs)

		if (max_dev_payoff > baseline_payoff):
			return False

	# print("max dev payoff", max_dev_payoff)
	return True

# checks whether the strategy fully cooperates (1CC always) when it plays against itself
# starting frmo any position
def is_full_coop_strat(strat, game):
	Q_dict = get_Q_dictionary(strat, game) 

	for start_state in range(game.num_states):
		if not is_full_coop_an_absorbing_state(start_state, Q_dict):
			return False
	return True

# returns a list of all pure strategies s.t. (strat, strat) is an SPE
def find_all_spe(game, delta):
	num_strats = 2**game.strat_len
	spe_lst = []

	for i in range(num_strats):
		strat = bin_array(i, game.strat_len)

		if is_spe(strat, game, delta):
			spe_lst.append(strat)
	return spe_lst