import numpy as np




def get_stationary_dist(Q, s1, s2, tolerance=1e-15):

        #Q is stochastic, guranteed to have left eigenvector v w/ eigenvalue 1
        # v satisfies Q'v = v, i.e. (Q' - I)v = 0, v = null(A) w/ A = Q' - v.

        A = Q.T-np.eye(len(Q))
        u, s, vh = np.linalg.svd(A)
        null_space = np.compress(s <= tolerance, vh, axis=0)

        try:
            v = null_space[0]
            v = np.absolute(v/np.sum(v))

            assert np.allclose(v, np.matmul(v, Q))

        except Exception as e:
            print("Get stationary distribution failed. s1 = {:}, s2 = {:}.".format(s1, s2)) 
            print("Q \n {:}".format(Q))
            raise(e)
        return v

# calculate average payoffs, probability of mutual cooperative state and game 1 state
def get_stats(Q, s1, s2, game_transition_dynamics):

    if game_transition_dynamics == "Unilateral_Dictator":
        v = self.get_unilateral_stationary_dist(s1, s2)
    else:
        v = self.get_stationary_dist(s1, s2)

    s1_payoff = np.dot(v, self.p1_payoffs)
    s2_payoff = np.dot(v, self.p2_payoffs)

    # player 1 cooperates in states 1CC and 1CD, 2CC and 2CD
    # player 2 cooperates in states 1CC and 1DC, 2CC and 2DC

    #s1_single_c_rate = v[0] + v[1] + v[4] + v[5]
    #s2_single_c_rate = v[0] + v[2] + v[4] + v[6]
    
    g1_cc_rate = v[0] #+ v[4] if self.num_states == 8 else v[0]
    g2_cc_rate = v[4] if self.num_states > 4 else 0

    g1_game_rate = sum(v[0:4]) # 1CC, 1CD, 1DC, 1DD

    # player avg coop rate - v1CC+(v1CD+v1DC)/2+v2CC+(v2CD+v2DC)/2

    two_player_c_rate = 2*v[0] + v[1] + v[2]
    if self.num_states > 4:
        two_player_c_rate += 2*v[4] + v[5] + v[6]

    player_c_rate = two_player_c_rate/2.0

    return (s1_payoff, s2_payoff, g1_cc_rate, g2_cc_rate, g1_game_rate, player_c_rate)

