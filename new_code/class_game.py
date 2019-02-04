import numpy as np

class Game:

    def __str__(self):
        return "S_{:02d}".format(self.strat_len)

    def reset_b1(self, b1):
        self.b1 = b1
        self.set_payoffs()

    def get_stationary_dist(self, s1, s2, eps=1e-15):
        Q = self.generate_transition_matrix(s1, s2)

        #Q is stochastic, guranteed to have left eigenvector v w/ eigenvalue 1
        # v satisfies Q'v = v, i.e. (Q' - I)v = 0, v = null(A) w/ A = Q' - v.

        A = Q.T-np.eye(len(Q))
        u, s, vh = np.linalg.svd(A)
        null_space = np.compress(s <= eps, vh, axis=0)

        try:
            v = null_space[0]
            v = np.absolute(v/np.sum(v))

            assert np.allclose(v, np.matmul(v, Q))

        except Exception as e:
            print("Get stationary distribution failed. s1 = {:}, s2 = {:}.".format(s1, s2)) 
            print("Q \n {:}".format(Q))
            raise(e)
        return v


    # calculates average payoffs
    def get_payoffs(self, s1, s2):
        v = self.get_stationary_dist(s1, s2)

        s1_payoff = np.dot(v, self.p1_payoffs)
        s2_payoff = np.dot(v, self.p2_payoffs)

        return (s1_payoff, s2_payoff)

    # calculate average payoffs, probability of mutual cooperative state and game 1 state
    def get_stats(self, s1, s2):
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

        return (s1_payoff, s2_payoff, g1_cc_rate, g2_cc_rate, g1_game_rate)

    # each specifc game class must implement these two methods
    def generate_transition_matrix(self, s1, s2):
        pass

    def set_payoffs(self):
        pass
