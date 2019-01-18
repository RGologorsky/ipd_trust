import numpy as np

from class_one_games import *
from stochastic_dynamics import *

from helper_functions import *


game = S_4_Game(c=1.0, b1=10.0)

# testing payoffs in states CC, CD, DC, and DD
assert(game.p1_payoffs.tolist() == [9, -1, 10, 0])
assert(game.p2_payoffs.tolist() == [9, 10, -1, 0])

# testing transition matrix
for eps in [0, 0.005, 0.990]:
	print("=== Testing eps = {:.4f}".format(eps))
	
	ALLD = (eps, eps, eps, eps)
	TFT = (1-eps, eps, 1-eps, eps)
	WSLS = (1-eps, eps, eps, 1-eps)

	TFT_vs_ALLD = [
		[(1-eps)*eps, (1-eps)*(1-eps), eps*eps, eps*(1-eps)],
		[eps*eps, eps*(1-eps), (1-eps)*eps, (1-eps)*(1-eps)],
		[(1-eps)*eps, (1-eps)*(1-eps), eps*eps, eps*(1-eps)],
		[eps*eps, eps*(1-eps), (1-eps)*eps, (1-eps)*(1-eps)],
	]

	TFT_vs_WSLS = [
		[(1-eps)*(1-eps), (1-eps)*eps, eps*(1-eps), eps*eps],
		[eps*eps, eps*(1-eps), (1-eps)*eps, (1-eps)*(1-eps)],
		[(1-eps)*eps, (1-eps)*(1-eps), eps*eps, eps*(1-eps)],
		[eps*(1-eps), eps*eps, (1-eps)*(1-eps), (1-eps)*eps],
	]


	# TFT vs ALLD
	print("=== TFT vs. ALLD ===")
	print_matrix("Manual", TFT_vs_ALLD)
	print_matrix("Autogen", game.generate_transition_matrix(TFT, ALLD).tolist())

	# testing stationary distribution
	stationary_TFT_vs_ALLD = game.get_stationary_dist(TFT, ALLD).tolist()
	stationary_ALLD_vs_TFT = game.get_stationary_dist(ALLD, TFT).tolist()

	print_list("stationary TFT vs ALLD", stationary_TFT_vs_ALLD)
	print_list("stationary ALLD vs TFT", stationary_ALLD_vs_TFT)

	assert(is_close(stationary_TFT_vs_ALLD[0], stationary_ALLD_vs_TFT[0]) and
		   is_close(stationary_TFT_vs_ALLD[3], stationary_ALLD_vs_TFT[3]) and
		   is_close(stationary_TFT_vs_ALLD[1], stationary_ALLD_vs_TFT[2]))

	assert(np.allclose(stationary_TFT_vs_ALLD, np.matmul(stationary_TFT_vs_ALLD, TFT_vs_ALLD)))

	# TFT vs WSLS
	print("=== TFT vs. WSLS ===")
	print_matrix("Manual", TFT_vs_WSLS)
	print_matrix("Autogen", game.generate_transition_matrix(TFT, WSLS).tolist())

	# testing stationary distribution
	stationary_TFT_vs_WSLS = game.get_stationary_dist(TFT, WSLS).tolist()
	stationary_WSLS_vs_TFT = game.get_stationary_dist(WSLS, TFT).tolist()

	print_list("stationary TFT vs WSLS", stationary_TFT_vs_WSLS)
	print_list("stationary WSLS vs TFT", stationary_WSLS_vs_TFT)

	assert(is_close(stationary_TFT_vs_WSLS[0], stationary_WSLS_vs_TFT[0]) and
		   is_close(stationary_TFT_vs_WSLS[3], stationary_WSLS_vs_TFT[3]) and
		   is_close(stationary_TFT_vs_WSLS[1], stationary_WSLS_vs_TFT[2]))

	assert(np.allclose(stationary_TFT_vs_WSLS, np.matmul(stationary_TFT_vs_WSLS, TFT_vs_WSLS)))

print("Passed my tests!")