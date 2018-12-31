from class_reactive import Reactive_Game
from class_one import One_Game
from class_s_12 import S_12_Game
from class_s_16 import S_16_Game


from helpers import *

# choose game
game = Reactive_Game(c=1.0, b1=10)

# Parameters
j = 1
N=2
beta=1

# Relative Payoffs
pi_xx = 0 
pi_xy = 10 
pi_yx = -1 
pi_yy = 9

pi_invader   = pi_yy * (j-1)/(N-1.0) + pi_yx * (N-j)/(N-1.0)
pi_host      = pi_xy * j/(N-1.0)     + pi_xx * (N-j-1)/(N-1.0)

print("fitness: invader = {:.2f}, host = {:.2f}: ".format(pi_invader, pi_host))
print("invader -> host    imitation prob: ", get_prob_imitation(beta, pi_invader, pi_host))
print("host    -> invader imitation prob: ", get_prob_imitation(beta, pi_host, pi_invader))
print("invader decr prob: ", get_prob_invader_decr(j, N, beta, pi_invader, pi_host))
print("invader incr prob: ", get_prob_invader_incr(j, N, beta, pi_invader, pi_host))
print("ratio: ", get_invader_decr_incr_ratio(j, N, beta, pi_xx, pi_xy, pi_yx, pi_yy))
print("get prob mutant fixation: ", get_prob_mutant_fixation(N, beta, pi_xx, pi_xy, pi_yx, pi_yy))