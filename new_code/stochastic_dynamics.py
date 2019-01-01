import numpy as np
np.seterr(over='raise')

# Probability Helpers
def get_prob_imitation(beta, pi_learner, pi_rolemodel):
    return 1.0/(1.0 + np.exp(-1.0 * beta * (pi_rolemodel - pi_learner)))

# Probability of number of invaders in pop. decreasing from j to j + 1.
# Prob{invader is chosen as learner and host is chosen as rolemodel and learner imitates rolemodel}
def get_prob_invader_decr(j, N, beta, pi_invader, pi_host):
    return float(j)/N * float(N-j)/(N-1) * get_prob_imitation(beta, pi_invader, pi_host)

def get_prob_invader_incr(j, N, beta, pi_invader, pi_host):
    return float(N-j)/N * float(j)/(N-1) * get_prob_imitation(beta, pi_host, pi_invader)


def get_invader_decr_incr_ratio(j, N, beta, pi_xx, pi_xy, pi_yx, pi_yy):

    # no self-interactions
    pi_invader   = pi_yy * (j-1)/(N-1.0) + pi_yx * (N-j)/(N-1.0)
    pi_host      = pi_xy * j/(N-1.0)     + pi_xx * (N-j-1)/(N-1.0)

    return get_prob_invader_decr(j, N, beta, pi_invader, pi_host)/get_prob_invader_incr(j, N, beta, pi_invader, pi_host)

def get_prob_mutant_fixation(N, beta, pi_xx, pi_xy, pi_yx, pi_yy):
    summation = 1
    curr_product = 1

    for k in range(1, N):
        try:
            new_term = get_invader_decr_incr_ratio(k, N, beta, pi_xx, pi_xy, pi_yx, pi_yy)
            curr_product *= new_term
            summation += curr_product

        except FloatingPointError:
            # print("Overflow in denominator => prob of invasion is nil.")
            return 0


    #print("N = {}, beta = {}, pi_xx = {:.2f}, pi_xy = {:.2f}, pi_yx = {:.2f}, pi_yy = {:.2f}, prob: {:.2f}".format(N, beta, pi_xx, pi_xy, pi_yx, pi_yy, 1.0/summation))
    return 1.0/summation