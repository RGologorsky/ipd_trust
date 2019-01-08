import numpy as np

from class_one_games import *
from stochastic_dynamics import *

from helpers import *


# test  get_prob_imitation(beta, pi_learner, pi_rolemodel)
assert(get_prob_imitation(beta = 10, pi_learner=0, pi_rolemodel=0) == 0.50)
assert(get_prob_imitation(beta = 10, pi_learner=1, pi_rolemodel=1) == 0.50)
assert(get_prob_imitation(beta = 10, pi_learner=10, pi_rolemodel=9) < 0.50)
assert(get_prob_imitation(beta = 10, pi_learner=10, pi_rolemodel=11) > 0.50)

beta1_prob_imitation = get_prob_imitation(beta = 1, pi_learner=10, pi_rolemodel=13)
beta2_prob_imitation = get_prob_imitation(beta = 2, pi_learner=10, pi_rolemodel=13)

assert(beta1_prob_imitation < beta2_prob_imitation)


# test get_prob_invader_decr(j, N, beta, pi_invader, pi_host)
assert(get_prob_invader_decr(j=0, N=10, beta=10, pi_invader=10, pi_host=0) == 0)
assert(get_prob_invader_decr(j=10, N=10, beta=10, pi_invader=10, pi_host=0) == 0)

prob_imitation = get_prob_imitation(beta = 10, pi_learner=6, pi_rolemodel=13)
assert(get_prob_invader_decr(j=7, N=100, beta=10, pi_invader=6, pi_host=13) == 7/100.0 * 93/99.0 * prob_imitation) 

assert(get_prob_invader_decr(j=7, N=100, beta=10, pi_invader=0, pi_host=0) == \
	   get_prob_invader_incr(j=7, N=100, beta=10, pi_invader=0, pi_host=0))


# test get_prob_invader_incr(j, N, beta, pi_invader, pi_host):
assert(get_prob_invader_incr(j=0, N=10, beta=10, pi_invader=10, pi_host=0) == 0)
assert(get_prob_invader_incr(j=10, N=10, beta=10, pi_invader=10, pi_host=0) == 0)

prob_imitation = get_prob_imitation(beta = 10, pi_learner=13, pi_rolemodel=12)
assert(get_prob_invader_incr(j=7, N=100, beta=10, pi_invader=12, pi_host=13) == 93/100.0 * 7/99.0 * prob_imitation) 


# test get_invader_decr_incr_ratio(j, N, beta, pi_xx, pi_xy, pi_yx, pi_yy):
assert(get_invader_decr_incr_ratio(j=5, N=10, beta=10, pi_xx=0, pi_xy=0, pi_yx=0, pi_yy=0) == 1.0)
assert(get_invader_decr_incr_ratio(j=1, N=2, beta=10, pi_xx=0, pi_xy=0, pi_yx=1, pi_yy=0) < 1.0)
assert(get_invader_decr_incr_ratio(j=1, N=3, beta=10, pi_xx=10, pi_xy=0, pi_yx=1, pi_yy=0) > 1.0)

# test get_prob_mutant_fixation(N, beta, pi_xx, pi_xy, pi_yx, pi_yy):
assert(get_prob_mutant_fixation(N=1, beta=10, pi_xx=0, pi_xy=0, pi_yx=0, pi_yy=0) == 1/1.0)
assert(get_prob_mutant_fixation(N=2, beta=10, pi_xx=0, pi_xy=0, pi_yx=0, pi_yy=0) == 1/2.0)
assert(get_prob_mutant_fixation(N=3, beta=10, pi_xx=0, pi_xy=0, pi_yx=0, pi_yy=0) == 1/3.0)
assert(get_prob_mutant_fixation(N=13, beta=10, pi_xx=0, pi_xy=0, pi_yx=0, pi_yy=0) == 1/13.0)
assert(get_prob_mutant_fixation(N=5, beta=10, pi_xx=0, pi_xy=0, pi_yx=0, pi_yy=1) > 1/5.0)

# check both function definitions give same answer
N = 5
beta = 2
pi_xx = 0.72165
pi_xy = 0.54212
pi_yx = 0.51620
pi_yy = 0.67152

old_def = old_get_prob_mutant_fixation(N, beta, pi_xx, pi_xy, pi_yx, pi_yy)
new_def = get_prob_mutant_fixation(N, beta, pi_xx, pi_xy, pi_yx, pi_yy)
print("Old def: {:f}, New def: {:f}. Diff: {:f}".format(old_def, new_def, new_def-old_def))

assert(np.isclose(old_def,new_def))

N = 50
beta = 1.88
pi_xx = 0.31276
pi_xy = 0.15217
pi_yx = 0.41290
pi_yy = 0.20347

old_def = old_get_prob_mutant_fixation(N, beta, pi_xx, pi_xy, pi_yx, pi_yy)
new_def = get_prob_mutant_fixation(N, beta, pi_xx, pi_xy, pi_yx, pi_yy)
print("Old def: {:f}, New def: {:f}. Diff: {:f}".format(old_def, new_def, new_def-old_def))

assert(np.isclose(old_def,new_def))

print("Passed my tests!")

# Checking fixation probs
game = S_2_Game(c=1.0, b1=10.0)

N = 100
beta = 2
eps = 0.0050

host = (eps, eps)
mutant = (0.270,0.290)

pi_xx, _      = game.get_payoffs(mutant, mutant)
pi_xy, pi_yx  = game.get_payoffs(host,   mutant)
pi_yy, _      = game.get_payoffs(mutant, mutant)

fixation_prob = get_prob_mutant_fixation(N, beta, pi_xx, pi_xy, pi_yx, pi_yy)
print("Prob mutant takes over ALLD: {:.4f}".format(fixation_prob))



