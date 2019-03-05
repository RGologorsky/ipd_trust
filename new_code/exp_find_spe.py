import numpy as np
from helper_functions import get_index, bin_array

### IMPORTANT ###
### CHECK G1 OR G2 DEFAULT DEV STATES, LINE 162 ####
#################

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


# returns set of states reachable by a single deviations from player 2
# player1 = 1C: can deviate to 1CC, 1CD, 2CC, 2CD (coop = 1 -> states 0,1,4,5)
# player1 = 1D: can deviate to 1DC, 1DD, 2DC, 2DD (coop = 0 -> states 2,3,6,7)
# player1 = 2C: can deviate to 2CC, 2CD (coop = 1 -> states 4,5)
# player1 = 2D: can deviate to 2DC, 2DD (coop = 0 -> states 6,7)

def g1_default_possible_dev_states(prior_state, strat):

	# S8 vs. S12 vs. S16 
	if len(strat) == 8:
		player1_transition = strat[4 + prior_state % 4]
		player1_g1_action  = strat[prior_state % 4]
		player1_g2_action  = strat[prior_state % 4]

	elif len(strat) == 12:
		player1_transition = strat[8 + prior_state % 4]
		player1_g1_action  = strat[prior_state % 4]
		player1_g2_action  = strat[4 + prior_state % 4]

	else:
		player1_transition = strat[8 + prior_state]
		player1_g1_action  = strat[prior_state % 4]
		player1_g2_action  = strat[4 + prior_state % 4]


	# always possible to vote and force Game 1.
	single_dev_states = {0,1} if player1_g1_action == 1 else {2,3}

	# add Game 2 state deviations if Game 2 is possible
	if player1_transition == 1:
		return single_dev_states

	# it is possible to reach Game 2
	if player1_g2_action == 1:
		single_dev_states.update({4,5})

	else:
		single_dev_states.update({6,7})

	return single_dev_states

def g2_default_possible_dev_states(prior_state, strat):

	# S8 vs. S12 vs. S16 
	if len(strat) == 8:
		player1_transition = strat[4 + prior_state % 4]
		player1_g1_action  = strat[prior_state % 4]
		player1_g2_action  = strat[prior_state % 4]

	elif len(strat) == 12:
		player1_transition = strat[8 + prior_state % 4]
		player1_g1_action  = strat[prior_state % 4]
		player1_g2_action  = strat[4 + prior_state % 4]

	else:
		player1_transition = strat[8 + prior_state]
		player1_g1_action  = strat[prior_state % 4]
		player1_g2_action  = strat[4 + prior_state % 4]


	# always possible to vote and force Game 2.
	single_dev_states = {4,5} if player1_g2_action == 1 else {6,7}

	# add Game 1 state deviations if Game 1 is possible
	if player1_transition == 0:
		return single_dev_states

	# it is possible to reach Game 1
	if player1_g1_action == 1:
		single_dev_states.update({0,1})

	else:
		single_dev_states.update({2,3})

	return single_dev_states

### IMPORTANT ###
### CHECK G1 OR G2 DEFAULT DEV STATES ####
#################

# checks whether (strategy, strategy) is an SPE
def is_spe(strat, game, delta):
	Q_dict      = get_Q_dictionary(strat, game) 
	payoff_dict = get_p2_payoff_dictionary(strat, game)

	# check all possible single deviations
	for prior_state in range(game.num_states):

		baseline_start_state = Q_dict[prior_state]
		baseline_payoff = get_avg_round_payoff(baseline_start_state, delta, Q_dict, payoff_dict)

		all_possible_devs = default_possible_dev_states(prior_state, strat)

		# remove baseline next state from consideration 
		all_possible_devs.discard(baseline_start_state)

		dev_payoffs = [get_avg_round_payoff(start_state, delta, Q_dict, payoff_dict) 
						for start_state in all_possible_devs]

		max_dev_payoff = max(dev_payoffs)
		# print("max dev payoff", max_dev_payoff)

		if (max_dev_payoff > baseline_payoff):
			return False

	return True

# checks whether the strategy fully cooperates (1CC always) when it plays against itself
# starting from *any* start state
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