import numpy as np

from class_two_games import *
from stochastic_dynamics import *

from helper_functions import *


game = S_12_Game(c=1.0, b1=1.8, b2=1.2)

# testing payoffs in states 1CC, 1CD, 1DC, 1DD, 2CC, 2CD, 2DC, 2DD
#print(game.p1_payoffs.tolist())
assert(np.allclose(game.p1_payoffs, [0.8, -1, 1.8, 0, 0.2, -1, 1.2, 0]))
assert(np.allclose(game.p2_payoffs, [0.8, 1.8, -1, 0, 0.2, 1.2, -1, 0]))

print("Payoffs passed!")

# testing transition matrix
for eps in [0, 0.005, 0.990]:

	def d(d_eps):
		d_1_eps = 2 - d_eps
		return (eps**d_eps) * ((1-eps) ** d_1_eps)

	def t(d_eps):
		d_1_eps = 2 - d_eps
		return (eps**d_eps) * ((1-eps) ** d_1_eps)

	print("=== Testing eps = {:.4f}".format(eps))
	
	#ALLD = (eps for _ in range(game.strat_len))

	# cooperates if prior = CC or DC, game1 if prior = CC or DC
	TFT = (1-eps, eps, 1-eps, eps,
		   1-eps, eps, 1-eps, eps,
		   1-eps, eps, 1-eps, eps)

	# cooperates if prior = CC or DD, game1 if prior = CC, DC, or DD
	WSLS = (1-eps, eps, eps, 1-eps, 
		    1-eps, eps, eps, 1-eps, 
		    1-eps, eps, 1-eps, 1-eps)

	# TFT_vs_ALLD = [
	# 	[(1-eps)*eps, (1-eps)*(1-eps), eps*eps, eps*(1-eps)],
	# 	[eps*eps, eps*(1-eps), (1-eps)*eps, (1-eps)*(1-eps)],
	# 	[(1-eps)*eps, (1-eps)*(1-eps), eps*eps, eps*(1-eps)],
	# 	[eps*eps, eps*(1-eps), (1-eps)*eps, (1-eps)*(1-eps)],
	# ]

	TFT_vs_WSLS = [
		[t(0)*d(0), t(0)*d(1), t(0)*d(1), t(0)*d(2), (1-t(0))*d(0), (1-t(0))*d(1), (1-t(0))*d(1), (1-t(0))*d(2)],
		[t(1)*d(2), t(1)*d(1), t(1)*d(1), t(1)*d(0), (1-t(1))*d(2), (1-t(1))*d(1), (1-t(1))*d(1), (1-t(1))*d(0)],
		[t(1)*d(1), t(1)*d(2), t(1)*d(0), t(1)*d(1), (1-t(1))*d(1), (1-t(1))*d(2), (1-t(1))*d(0), (1-t(1))*d(1)],
		[t(1)*d(1), t(1)*d(2), t(1)*d(0), t(1)*d(1), (1-t(1))*d(1), (1-t(1))*d(2), (1-t(1))*d(0), (1-t(1))*d(1)],

		[t(0)*d(0), t(0)*d(1), t(0)*d(1), t(0)*d(2), (1-t(0))*d(0), (1-t(0))*d(1), (1-t(0))*d(1), (1-t(0))*d(2)],
		[t(1)*d(2), t(1)*d(1), t(1)*d(1), t(1)*d(0), (1-t(1))*d(2), (1-t(1))*d(1), (1-t(1))*d(1), (1-t(1))*d(0)],
		[t(1)*d(1), t(1)*d(2), t(1)*d(0), t(1)*d(1), (1-t(1))*d(1), (1-t(1))*d(2), (1-t(1))*d(0), (1-t(1))*d(1)],
		[t(1)*d(1), t(1)*d(2), t(1)*d(0), t(1)*d(1), (1-t(1))*d(1), (1-t(1))*d(2), (1-t(1))*d(0), (1-t(1))*d(1)],


	]


	# TFT vs ALLD
	# print("=== TFT vs. ALLD ===")
	# print_matrix("Manual", TFT_vs_ALLD)
	# print_matrix("Autogen", game.generate_transition_matrix(TFT, ALLD).tolist())

	# testing stationary distribution
	# stationary_TFT_vs_ALLD = game.get_stationary_dist(TFT, ALLD).tolist()
	#stationary_ALLD_vs_TFT = game.get_stationary_dist(ALLD, TFT).tolist()

	#print_list("stationary TFT vs ALLD", stationary_TFT_vs_ALLD)
	#print_list("stationary ALLD vs TFT", stationary_ALLD_vs_TFT)

	# assert(is_close(stationary_TFT_vs_ALLD[0], stationary_ALLD_vs_TFT[0]) and
	# 	   is_close(stationary_TFT_vs_ALLD[3], stationary_ALLD_vs_TFT[3]) and
	# 	   is_close(stationary_TFT_vs_ALLD[1], stationary_ALLD_vs_TFT[2]))

	# assert(np.allclose(stationary_TFT_vs_ALLD, np.matmul(stationary_TFT_vs_ALLD, TFT_vs_ALLD)))

	# TFT vs WSLS
	print("=== TFT vs. WSLS ===")
	print_matrix("Manual", TFT_vs_WSLS)
	print_matrix("Autogen", game.generate_transition_matrix(TFT, WSLS).tolist())

	assert(np.allclose(TFT_vs_WSLS, game.generate_transition_matrix(TFT, WSLS)))
	print("Passed transition matrix!")

	# testing stationary distribution
	stationary_TFT_vs_WSLS = game.get_stationary_dist(TFT, WSLS).tolist()
	stationary_WSLS_vs_TFT = game.get_stationary_dist(WSLS, TFT).tolist()

	print_list("stationary TFT vs WSLS", stationary_TFT_vs_WSLS)
	print_list("stationary WSLS vs TFT", stationary_WSLS_vs_TFT)

	assert(is_close(stationary_TFT_vs_WSLS[0], stationary_WSLS_vs_TFT[0]) and
		   is_close(stationary_TFT_vs_WSLS[3], stationary_WSLS_vs_TFT[3]) and
		   is_close(stationary_TFT_vs_WSLS[1], stationary_WSLS_vs_TFT[2]))

	assert(is_close(stationary_TFT_vs_WSLS[0+4], stationary_WSLS_vs_TFT[0+4]) and
		   is_close(stationary_TFT_vs_WSLS[3+4], stationary_WSLS_vs_TFT[3+4]) and
		   is_close(stationary_TFT_vs_WSLS[1+4], stationary_WSLS_vs_TFT[2+4]))

	print(stationary_TFT_vs_WSLS)
	print(np.matmul(stationary_TFT_vs_WSLS, TFT_vs_WSLS))
	assert(np.allclose(stationary_TFT_vs_WSLS, np.matmul(stationary_TFT_vs_WSLS, TFT_vs_WSLS)))

print("Passed my tests!")