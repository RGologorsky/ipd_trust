import numpy as np
from helper_functions import get_index, bin_array

import pprint as pp
### IMPORTANT ###
### CHECK G1 OR G2 DEFAULT DEV STATES, LINE 162 ####
#################

# returns dictionary d; d[state_id] = player 2's payoff in that state 
def get_p2_payoff_dict(strat, game):
	return {num: game.p2_payoffs[num] for num in range(game.num_states)}

# only for two-games. Returns dictionary d; For strat vs. strat, d[state_id] = next_state
def get_Q_dict(strat, game):
	Q = game.generate_resolution_rule_matrix(strat, strat, game.f)

	Q_dict = {}
	for state_num in range(game.num_states):
		prob_next_states = np.matmul(game.num_to_state[state_num], Q)
		next_states      = np.nonzero(prob_next_states)[0]

		# list of (next_state, prob_next_state)
		Q_dict[state_num] = list(zip(next_states, prob_next_states[next_states]))
		
	return Q_dict

# value iteration
def get_state_values(strat, game, delta, tol=10**-9):
	payoff_dict = get_p2_payoff_dict(strat, game)
	Q_dict = get_Q_dict(strat, game)

	# print number of iterations
	t = 0

	# init state values to 0 for states 1CC to 2DD (state nums 0 to 7)
	vals = {state_num:0.0 for state_num in range(game.num_states)}

	vals_converged = False

	while not vals_converged:

		#print("T = {:d}".format(t))
		#pp.pprint(vals)

		vals_converged = True
		for state_num in range(game.num_states):

			# updated estimate of state value
			new_estimate = 0.0
			for (next_state, prob_next_state) in Q_dict[state_num]:
				next_state_payoff = delta**t * payoff_dict[next_state]
				new_estimate += prob_next_state * (next_state_payoff + delta**t*vals[next_state])

			t += 1
			#print("state {:d}, new_estimate {:f}".format(state_num, new_estimate))
			# avg payoff per round
			#new_estimate = new_estimate * (1-delta)

			# update value if needed
			if abs(vals[state_num] - new_estimate) > tol:
				vals[state_num] = new_estimate 
				vals_converged = False

	print("T = {:d}".format(t))
	return vals



# returns set of states reachable by a single deviations from player 2
# player1 = 1C: can deviate to 1CC, 1CD, 2CC, 2CD (coop = 1 -> states 0,1,4,5)
# player1 = 1D: can deviate to 1DC, 1DD, 2DC, 2DD (coop = 0 -> states 2,3,6,7)
# player1 = 2C: can deviate to 2CC, 2CD (coop = 1 -> states 4,5)
# player1 = 2D: can deviate to 2DC, 2DD (coop = 0 -> states 6,7)


### IMPORTANT ###
### CHECK G1 OR G2 DEFAULT DEV STATES ####
#################

# checks whether (strategy, strategy) is an SPE
def is_spe(strat, game, delta, resolution_rule):

	state_values = get_state_values(strat, game, delta)

	# check all possible single deviations
	for prior_state in range(game.num_states):

		baseline_payoff = state_values[prior_state]

		# check if exists useful deviation

		p1_action = 

		for dev_action in ("1C", "1D", "2D", "2D"):
			dev_states =  

		if resolution_rule == "EqualSay_G2_Default":
			all_possible_devs = g2_default_possible_dev_states(prior_state, strat)

		elif resolution_rule == "EqualSay_G1_Default":
			all_possible_devs = g1_default_possible_dev_states(prior_state, strat)

		elif resolution_rule == "Random":
			all_possible_devs = random_possible_dev_states(prior_state, strat)

		elif resolution_rule == "NA":
			all_possible_devs = one_game_possible_dev_states(prior_state, strat)

		else:
			raise Exception("Unrecognized resolution_rule Strat")
	

		# check whether any deviation is useful
		for dev_state in all_possible_devs:
			dev_payoff = payoff_dict[dev_state] + delta * state_values[dev_payoff]

		dev_payoffs = [dev_payoff + delta * 
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


def is_full_coop_spe(strat, game, delta, resolution_rule="EqualSay_G2_Default"):
	return is_full_coop_strat(strat, game) and is_spe(strat, game, delta, resolution_rule)

# returns a list of all pure strategies s.t. (strat, strat) is an SPE
def find_all_coop_spe(game, delta, resolution_rule):
	num_strats = 2**game.strat_len
	spe_lst = []

	for i in range(num_strats):
		strat = bin_array(i, game.strat_len)

		if is_full_coop_strat(strat, game) and is_spe(strat, game, delta, resolution_rule):
			spe_lst.append(strat)
	return spe_lst



### VERBOSE FUNCTIONs (good for checking why a strategy is not SPE) ###
# prints & checks whether (strategy, strategy) is an SPE
def pprint_strat(strat):
	res = ""
	for i,digit in enumerate(strat):
		res += str(digit)
		if i == 3 or i == 7 or (i == 11 and len(strat) == 16):
			res += ", "
	print(res)


def verbose_is_spe(strat, game, delta, resolution_rule):
	Q_dict      = get_Q_dictionary(strat, game) 
	payoff_dict = get_p2_payoff_dictionary(strat, game)

	# check all possible single deviations
	for prior_state in range(game.num_states):

		baseline_start_state = Q_dict[prior_state]
		baseline_payoff = get_avg_round_payoff(baseline_start_state, delta, Q_dict, payoff_dict)

		if resolution_rule == "EqualSay_G2_Default":
			all_possible_devs = g2_default_possible_dev_states(prior_state, strat)

		elif resolution_rule == "EqualSay_G1_Default":
			all_possible_devs = g1_default_possible_dev_states(prior_state, strat)

		elif resolution_rule == "NA":
			all_possible_devs = one_game_possible_dev_states(prior_state, strat)

		else:
			raise Exception("Unrecognized resolution_rule Strat")

		# remove baseline next state from consideration 
		all_possible_devs.discard(baseline_start_state)

		dev_payoffs = [get_avg_round_payoff(start_state, delta, Q_dict, payoff_dict) 
						for start_state in all_possible_devs]


		max_dev_payoff = max(dev_payoffs)
		# print("max dev payoff", max_dev_payoff)

		if (max_dev_payoff > baseline_payoff):

			print("all_possible_dev states ")
			print(all_possible_devs)

			print("dev_payoffs")
			print([round(payoff, 9) for payoff in dev_payoffs])

			# dev state
			all_possible_devs = list(all_possible_devs)
			dev_state = all_possible_devs[dev_payoffs.index(max_dev_payoff)]

			# state other than 1CC is a useful dev
			pprint_strat(strat)
			print("prior state: ", prior_state, "useful dev state: ", dev_state)

			print("baseline_payoff {:f}".format(baseline_payoff))
			print("max_payoff {:f}".format(max_dev_payoff))
			print("diff: {:f}".format(max_dev_payoff-baseline_payoff))



			return False

	return True

# checks whether the strategy fully cooperates (1CC always) when it plays against itself
# starting from *any* start state
def verbose_is_full_coop_strat(strat, game):
	Q_dict = get_Q_dictionary(strat, game) 

	for start_state in range(game.num_states):
		if not is_full_coop_an_absorbing_state(start_state, Q_dict):
			print("not full coop because of start state ", start_state)
			return False
	return True

# returns True if: not SPE & useful dev is not 1CC
def verbose_not_1cc_useful_dev(strat, game, delta, resolution_rule):
	Q_dict      = get_Q_dictionary(strat, game) 
	payoff_dict = get_p2_payoff_dictionary(strat, game)

	# check all possible single deviations
	for prior_state in range(game.num_states):

		baseline_start_state = Q_dict[prior_state]
		baseline_payoff = get_avg_round_payoff(baseline_start_state, delta, Q_dict, payoff_dict)

		if resolution_rule == "EqualSay_G2_Default":
			all_possible_devs = g2_default_possible_dev_states(prior_state, strat)

		elif resolution_rule == "EqualSay_G1_Default":
			all_possible_devs = g1_default_possible_dev_states(prior_state, strat)

		elif resolution_rule == "NA":
			all_possible_devs = one_game_possible_dev_states(prior_state, strat)

		else:
			raise Exception("Unrecognized resolution_rule Strat")

		# remove baseline next state from consideration 
		all_possible_devs.discard(baseline_start_state)

		all_possible_devs = list(all_possible_devs)
		dev_payoffs = [get_avg_round_payoff(start_state, delta, Q_dict, payoff_dict) 
						for start_state in all_possible_devs]


		max_dev_payoff = max(dev_payoffs)
		# print("max dev payoff", max_dev_payoff)

		if (max_dev_payoff > baseline_payoff):

			# 1CC is a useful dev
			if prior_state == 0:
				return False

			# dev state
			dev_state = all_possible_devs[dev_payoffs.index(max_dev_payoff)]

			# state other than 1CC is a useful dev
			pprint_strat(strat)
			print("useful dev from prior state: ", prior_state, "dev state: ", dev_state)
			return True
	
	# no useful devs
	return False


def verbose_find_not_1cc_useful_dev(game, delta, resolution_rule):
	num_strats = 2**game.strat_len
	not_spe_lst = []

	for i in range(num_strats):
		strat = bin_array(i, game.strat_len)

		if is_full_coop_strat(strat, game) and verbose_not_1cc_useful_dev(strat, game, delta, resolution_rule):
			not_spe_lst.append(strat)
	return not_spe_lst