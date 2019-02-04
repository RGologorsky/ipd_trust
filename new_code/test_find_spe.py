import numpy as np

from find_spe_functions import *
from helper_functions   import *
from class_two_games    import *


# === testing get_avg_round_payoff ===
start_state = 0
delta = 0.90

a1  = 10.1
a2 = 5.2
y1 = 2.6
y2 = 4.3
y3 = 7.2

# Q_dict[state] = next_state
Q_dict = {
	0: 1, 
	1: 2,
	2: 3,
	3: 4,
	4: 2,
}

payoff_dict = {
	0: a1,
	1: a2, 
	2: y1,
	3: y2,
	4: y3,
}

auto_res = get_avg_round_payoff(start_state, delta, Q_dict, payoff_dict)
manual_total = a1 + delta * a2 + 1.0/(1.0-delta**3) * (delta**2 * y1 + delta**3 * y2 + delta**4 * y3) 
expected_num_rounds = 1.0/(1.0-delta)
manual_res = manual_total / expected_num_rounds

print("Auto = {:7f}, Manual = {:.7f}, Diff = {:.7f}".format(auto_res, manual_res, manual_res-auto_res))
assert(np.isclose(manual_res, auto_res))

c = 1.0
b1 = 1.8
b2 = 1.2
delta = 0.99

s_12_game = S_12_Game(c, b1, b2)
WSLS = [1,0,0,0, 0,0,0,1, 1,0,0,0]

Q_dict      = get_Q_dictionary(WSLS, s_12_game) 
payoff_dict = get_p2_payoff_dictionary(WSLS, s_12_game)

start_state = 1 #1CD

auto_res = get_avg_round_payoff(start_state, delta, Q_dict, payoff_dict)
manual_total = b1 + 0*delta + (b2-c)*delta**2 + (b1-c)*delta**3/(1-delta)
expected_num_rounds = 1.0/(1.0-delta)
manual_res = manual_total / expected_num_rounds

print("Auto = {:7f}, Manual = {:.7f}, Diff = {:.7f}".format(auto_res, manual_res, manual_res-auto_res))
assert(np.isclose(manual_res, auto_res))

# testing strat = [1,0,0,0, 0,0,0,1, 1,0,0,0]
print("\ntesting strat [1,0,0,0, 0,0,0,1, 1,0,0,0]\n")

c = 1.0
b1 = 1.5
b2 = 1.2
delta = 0.99

s_12_game = S_12_Game(c, b1, b2)
WSLS = [1,0,0,0, 0,0,0,1, 1,0,0,0]

Q_dict      = get_Q_dictionary(WSLS, s_12_game) 
payoff_dict = get_p2_payoff_dictionary(WSLS, s_12_game)

start_state = 1 #1CD

auto_res = get_avg_round_payoff(start_state, delta, Q_dict, payoff_dict)
manual_total = b1 + 0*delta + (b2-c)*delta**2 + (b1-c)*delta**3/(1-delta)
expected_num_rounds = 1.0/(1.0-delta)
manual_res = manual_total / expected_num_rounds

print("Auto = {:7f}, Manual = {:.7f}, Diff = {:.7f}".format(auto_res, manual_res, manual_res-auto_res))
assert(np.isclose(manual_res, auto_res))

# testing strat = [1,0,0,0, 0,0,0,1, 1,0,0,1]
print("\ntesting strat [1,0,0,0, 0,0,0,1, 1,0,0,1]\n")
c = 1.0
b1 = 1.3
b2 = 1.2
delta = 0.99

s_12_game = S_12_Game(c, b1, b2)
strat = [1,0,0,0, 0,0,0,1, 1,0,0,1]

Q_dict      = get_Q_dictionary(strat, s_12_game) 
payoff_dict = get_p2_payoff_dictionary(strat, s_12_game)

start_state = 0 #1CC

auto_res = get_avg_round_payoff(start_state, delta, Q_dict, payoff_dict)
manual_res = b1 - c

print("Auto = {:7f}, Manual = {:.7f}, Diff = {:.7f}".format(auto_res, manual_res, manual_res-auto_res))
assert(np.isclose(manual_res, auto_res))

start_state = 1 #1CD

auto_res = get_avg_round_payoff(start_state, delta, Q_dict, payoff_dict)
manual_total = b1
expected_num_rounds = 1.0/(1.0-delta)
manual_res = manual_total / expected_num_rounds

print("Auto = {:7f}, Manual = {:.7f}, Diff = {:.7f}".format(auto_res, manual_res, manual_res-auto_res))
assert(np.isclose(manual_res, auto_res))


print("\nPassed get_avg_round_payoff(start_state, delta, Q_dict, payoff_dict).\n")

# == testing possible_dev_states

WSLS = [1,0,0,0, 0,0,0,1, 1,0,0,0]
cWSLS = [1,0,0,0, 1,0,0,1, 1,0,0,0]
onecc_wsls_dev = possible_dev_states(str_to_state_dict["1CC"], strat=WSLS)
onecc_cwsls_dev = possible_dev_states(str_to_state_dict["1CC"], strat=cWSLS)

print("1CC wsls", states_to_str_lst(onecc_wsls_dev))
print("1CC cWsls", states_to_str_lst(onecc_cwsls_dev))

assert(onecc_wsls_dev == set(str_list_to_states(["1CC", "1CD", "2DC", "2DD"])))
assert(onecc_cwsls_dev == set(str_list_to_states(["1CC", "1CD", "2CC", "2CD"])))

print("\nPassed possible_dev_states.\n")

# testing is_spe_s12(strat, game, delta)
delta = 0.9999
s_12_game = S_12_Game(c=1.0, b1=1.8, b2=1.2)
is_wsls_spe = (is_spe(WSLS, s_12_game, delta))
print("1. high b1: is WSLS SPE? ", is_wsls_spe)
assert(is_wsls_spe)

s_12_game = S_12_Game(c=1.0, b1=1.5, b2=1.2)
is_wsls_spe = (is_spe(WSLS, s_12_game, delta))
print("2. low b1: is WSLS SPE? ", is_wsls_spe)
assert(not is_wsls_spe)

s_12_game = S_12_Game(c=1.0, b1=1.601, b2=1.2)
is_wsls_spe = (is_spe(WSLS, s_12_game, delta))
print("3. exact (b1 slightly above cutoff). is WSLS SPE? ", is_wsls_spe)
assert(is_wsls_spe)

s_12_game = S_12_Game(c=1.0, b1=1.599, b2=1.2)
is_wsls_spe = (is_spe(WSLS, s_12_game, delta))
print("3. exact (b1 slightly below cutoff). is WSLS SPE? ", is_wsls_spe)
assert(not is_wsls_spe)

# s_12_game = S_12_Game(c=1.0, b1=1.3, b2=1.2)
# strat = [1,0,0,0,0,0,0,1,1,0,0,1]
# is_strat_spe = (is_spe(strat, s_12_game, delta))
# assert(is_strat_spe)

# testing odd spe
print("\ntesting strat [1,1,1,1, 1,0,1,1 ,1,1,0,1]\n")

c = 1.0
b1 = 1.8
b2 = 1.2
delta = 0.99

s_12_game = S_12_Game(c, b1, b2)

strat = [1,1,1,1, 1,0,1,1 ,1,1,0,1]
is_strat_spe = (is_spe(strat, s_12_game, delta))
is_strat_full_coop_spe = (is_strat_spe and is_full_coop_strat(strat, s_12_game))

Q_dict      = get_Q_dictionary(strat, s_12_game) 
payoff_dict = get_p2_payoff_dictionary(strat, s_12_game)

start_state = 0 #1CC

auto_res = get_avg_round_payoff(start_state, delta, Q_dict, payoff_dict)
manual_res = b1 - c

print("Auto = {:7f}, Manual = {:.7f}, Diff = {:.7f}".format(auto_res, manual_res, manual_res-auto_res))
assert(np.isclose(manual_res, auto_res))

start_state = 1 #1CD

next_state = Q_dict[start_state]
next_next_state = Q_dict[next_state]
next_next_next_state = Q_dict[next_next_state]

strs = states_to_str_lst([start_state, next_state, next_next_state, next_next_next_state])

print("{:s} -> {:s} -> {:s} -> {:s}".format(strs[0], strs[1], strs[2], strs[3]))

dev_states = possible_dev_states(str_to_state_dict["1CD"], strat=strat)
print("1CD dev states\n", states_to_str_lst(dev_states))

auto_res = get_avg_round_payoff(start_state, delta, Q_dict, payoff_dict)
manual_total = b1 + delta*(delta * b2 - c) * (1.0/(1.0-delta**2))
expected_num_rounds = 1.0/(1.0-delta)
manual_res = manual_total / expected_num_rounds

print("Auto = {:7f}, Manual = {:.7f}, Diff = {:.7f}\n".format(auto_res, manual_res, manual_res-auto_res))
assert(np.isclose(manual_res, auto_res))

assert(not is_strat_spe)
assert(not is_strat_full_coop_spe)


print("\nPassed is_spe_s12(strat, game, delta={:5f}).\n".format(delta))
print("Passed my tests!")
