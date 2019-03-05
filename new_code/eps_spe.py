import numpy as np
from helper_functions import get_index, bin_array

### IMPORTANT ###
### CHECK G1 OR G2 DEFAULT DEV STATES, LINE 162 ####
#################


# returns a list of all pure strategies s.t. (strat, strat) is an SPE
def find_all_ess(game, eps):
	num_strats = 2**game.strat_len
	ess_lst = []

	for i in range(num_strats):
		s1 = bin_array(i, game.strat_len)
		s1 = [eps + (1-2*eps)*p for p in s1] # add noise

		# check if cooperates against itself
		v = game.get_stationary_dist(game.get_f(), p_strat, p_strat)

		if v[0] > 0.99:
			a = np.dot(v, self.p1_payoffs)

			# check if cannot be invaded by other mutants
			s1_is_ESS_against_all = True

			for j in range(num_strats):
				s2 = bin_array(j, game.strat_len)
				s2 = [eps + (1-2*eps)*p for p in s2] # add noise

				# get q's cooperation rate
				v = game.get_stationary_dist(game.get_f(), s1, s2)
				b = np.dot(v, self.p1_payoffs)
        		c = np.dot(v, self.p2_payoffs)
				
        		# payoff q vs. q
        		v = game.get_stationary_dist(game.get_f(), s2, s2)
				d = np.dot(v, self.p1_payoffs)

				s1_is_ESS = (a  > c) or (a == c and b > d)

				if not s1_is_ESS:
					s1_is_ESS_against_all = False
					break

			if s1_is_ESS_against_all:
				ess_lst.append(s1)
	return ess_lst

# def find_all_spe(game, eps):
# 	num_strats = 2**game.strat_len
# 	spe_lst = []

# 	for i in range(num_strats):
# 		p_strat = bin_array(i, game.strat_len)
# 		p_strat = [eps + (1-2*eps)*p for p in strat] # add noise

# 		# check if cooperates against itself
# 		v = game.get_stationary_dist(game.get_f(), p_strat, p_strat)

# 		if v[0] > 0.99:
# 			p_g1_coop_rate = (2*v[0] + v[1] + v[2])/2.0
# 			p_g2_coop_rate = (2*v[4] + v[5] + v[6])/2.0

# 			payoff_p_vs_p = game.b1 * p_g1_coop_rate - game.c * p_g1_coop_rate \
# 							+ game.b2 * p_g2_coop_rate - game.c * p_g2_coop_rate

# 			is_NE = True

# 			# check if cannot be invaded by other mutants
# 			for j in range(num_strats):
# 				q_strat = bin_array(j, game.strat_len)
# 				q_strat = [eps + (1-2*eps)*p for p in strat] # add noise

# 				# get q's cooperation rate
# 				v = game.get_stationary_dist(game.get_f(), p_strat, q_strat)
# 				inv_p_g1_coop_rate = (2*v[0] + v[1])/2.0
# 				inv_p_g2_coop_rate = (2*v[4] + v[5])/2.0

# 				inv_q_g1_coop_rate = (2*v[0] + v[2])/2.0
# 				inv_q_g2_coop_rate = (2*v[4] + v[6])/2.0

# 				inv_payoff_p_vs_q = game.b1 * inv_q_g1_coop_rate - game.c * inv_p_g1_coop_rate \
# 							+ game.b2 * inv_q_g2_coop_rate - game.c * inv_p_g2_coop_rate

# 				inv_payoff_q_vs_p = game.b1 * inv_p_g1_coop_rate - game.c * inv_q_g1_coop_rate \
# 							+ game.b2 * inv_p_g2_coop_rate - game.c * inv_q_g2_coop_rate

# 				# compare payoff p vs. p to payoff p vs. q and q vs. p

# 				payoff_p_vs_q = game.b1 * p_g1_coop_rate - game.c * p_g1_coop_rate \
# 							+ game.b2 * p_g2_coop_rate - game.c * p_g2_coop_rate


# 		if is_full_coop_strat(strat, game) and is_spe(strat, game, delta, transition):
# 			spe_lst.append(strat)
# 	return spe_lst