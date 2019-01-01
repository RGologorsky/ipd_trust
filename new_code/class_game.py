import numpy as np

class Game:

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
            print("null space failed")
            print("s1 = {:}, s2 = {:}".format(s1, s2)) 
            print("Q \n {:}".format(Q))
            print(list(Q))
            raise(e)
        return v


    def get_payoffs(self, s1, s2):
        v = self.get_stationary_dist(s1, s2)

        s1_payoff = np.dot(v, self.p1_payoffs)
        s2_payoff = np.dot(v, self.p2_payoffs)

        return (s1_payoff, s2_payoff)

    # each specifc game class must implement these two methods
    def generate_transition_matrix(self, s1, s2):
        pass

    def set_payoffs(self):
        pass