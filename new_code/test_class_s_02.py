import numpy as np

from class_one_games import *
from stochastic_dynamics import *

from helper_functions import *


game = S_2_Game(c=1.0, b1=10.0)

# testing payoffs in states CC, CD, DC, and DD
assert(game.p1_payoffs.tolist() == [9, -1, 10, 0])
assert(game.p2_payoffs.tolist() == [9, 10, -1, 0])

# testing transition matrix
eps = 0.005
ALLD = (eps, eps)
TFT = (1-eps, eps)

TFT_vs_ALLD = [
	[(1-eps)*eps, (1-eps)*(1-eps), eps*eps, eps*(1-eps)],
	[eps*eps, eps*(1-eps), (1-eps)*eps, (1-eps)*(1-eps)],
	[(1-eps)*eps, (1-eps)*(1-eps), eps*eps, eps*(1-eps)],
	[eps*eps, eps*(1-eps), (1-eps)*eps, (1-eps)*(1-eps)],
]


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

print("Passed my tests!")