import numpy as np

class Two_Game:

    def __init__(self, c, b1, b2, eps=0.01, stored_stationary_dists={}):
        self.b1 = b1; # benefit coop in Game 1
        self.b2 = b2; # benefit coop in Game 2
        self.c  = c;   # cost to coop in both games

        self.eps = eps
        self.f = lambda a, b: a * b

        # player1, player2 payoffs for outcomes CC, CD, DC, and DD.
        self.p1_payoffs = np.asarray([b1-c, -c, b1, 0, b2-c, -c, b2, 0]);
        self.p2_payoffs = np.asarray([b1-c, b1, -c, 0, b2-c, b2, -c, 0]);

        self.stored_stationary_dists = stored_stationary_dists


    def reset_payoffs(self, c, b1, b2):
        self.b1 = b1; # benefit coop in Game 1
        self.b2 = b2; # benefit coop in Game 2
        self.c  = c;   # cost to coop in both games

        # player1, player2 payoffs for outcomes CC, CD, DC, and DD.
        self.p1_payoffs = np.asarray([b1-c, -c, b1, 0, b2-c, -c, b2, 0]);
        self.p2_payoffs = np.asarray([b1-c, b1, -c, 0, b2-c, b2, -c, 0]);

    def reset_b1(self, b1):
        self.reset_payoffs(self.c, b1, self.b2)

    def generate_transition_matrix(self, s1, s2):
        pass


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


    def to_strategy(self, num):
        strat_len = "0" + str(self.strat_len) + "b"
        return [int(x)*(1-2*self.eps)+self.eps for x in format(num, strat_len)]


    def strat_to_str(self, num):
        arr = self.to_strategy(num)
        return str(arr[0:4])   + "," + \
                str(arr[4:8])  + ". Transition: " + \
                str(arr[8:])

    def get_stats(self, s1, s2):
        
        # v = stationary proportion in states

        s_min = min(s1, s2)
        s_max = max(s1, s2)

        key = (s_min, s_max)

        if key in self.stored_stationary_dists:
            v = self.stored_stationary_dists[key]

        else:
            v = self.get_stationary_dist(s_min, s_max)
            self.stored_stationary_dists[key] = v

        # reverse CD and DC in order to be consistent with s1 vs. s2
        if key == (s2, s1):
            v = [v[0], v[2], v[1], v[3], v[4], v[6], v[5], v[7]]

        s1_payoff = np.dot(v, self.p1_payoffs)
        s2_payoff = np.dot(v, self.p2_payoffs)

        # player 1 cooperates in states 1CC and 1CD, 2CC and 2CD
        # player 2 cooperates in states 1CC and 1DC, 2CC and 2DC

        s1_single_c_rate = v[0] + v[1] + v[4] + v[5]
        s2_single_c_rate = v[0] + v[2] + v[4] + v[6]
        frac_game1 = sum(v[0:4]) # 1CC, 1CD, 1DC, 1DD

        return (s1_payoff, s2_payoff, s1_single_c_rate, s2_single_c_rate, frac_game1)
