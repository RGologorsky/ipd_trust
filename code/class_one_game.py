import numpy as np

class One_Game:

    # Calculating Game Transitions, specific payoffs between strategies.

    # 8 states, ranging from 0 to 7, corresponding to 1CC to 2DD.
    # Strategies in [0,1]^16


    def __init__(self, c, b1, b2=None, eps=0.01):
        self.b1 = b1; # benefit coop in Game 1
        self.c  = c;   # cost to coop in both games
        self.eps = eps

        self.strat_len = 4
        self.max_num_strategies = 2**4

        # player1, player2 payoffs for outcomes CC, CD, DC, and DD.
        self.p1_payoffs = np.asarray([b1-c, -c, b1, 0]);
        self.p2_payoffs = np.asarray([b1-c, b1, -c, 0]);

        self.stored_stationary_dists = {}

    def reset_payoffs(self, c, b1, b2=None):
        self.b1 = b1; # benefit coop in Game 1
        self.c  = c;   # cost to coop in both games

        # player1, player2 payoffs for outcomes CC, CD, DC, and DD.
        self.p1_payoffs = np.asarray([b1-c, -c, b1, 0]);
        self.p2_payoffs = np.asarray([b1-c, b1, -c, 0]);


    def reset_b1(self, b1):
        self.reset_payoffs(self.c, b1)


    def generate_transition_matrix(self, s1, s2):
        [pcc, pcd, pdc, pdd] = self.to_strategy(s1)
        [qcc, qcd, qdc, qdd] = self.to_strategy(s2)

        return np.asarray([
            [pcc*qcc, pcc*(1-qcc), (1-pcc)*qcc, (1-pcc)*(1-qcc)],
            [pcd*qdc, pcd*(1-qdc), (1-pcd)*qdc, (1-pcd)*(1-qdc)],
            [pdc*qcd, pdc*(1-qcd), (1-pdc)*qcd, (1-pdc)*(1-qcd)],
            [pdd*qdd, pdd*(1-qdd), (1-pdd)*qdd, (1-pdd)*(1-qdd)]
        ]);


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
        return [int(x)*(1-2*self.eps)+self.eps for x in format(num, '04b')]

    def strat_to_str(self, num):
        arr = self.to_strategy(num)
        return str(arr)

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
            v = [v[0], v[2], v[1], v[3]]

        s1_payoff = np.dot(v, self.p1_payoffs)
        s2_payoff = np.dot(v, self.p2_payoffs)

    
        # player 1 cooperates in states CC and CD
        s1_single_c_rate = v[0] + v[1]
        s2_single_c_rate = v[0] + v[2] # player 2 cooperates in states CC and DC

        frac_game1 = 1.0

        return (s1_payoff, s2_payoff, s1_single_c_rate, s2_single_c_rate, frac_game1)
