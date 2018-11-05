import numpy as np
import scipy.sparse.linalg as sp

class Pure_One_Game:

    # Calculating Game Transitions, specific payoffs between strategies.

    # 8 states, ranging from 0 to 7, corresponding to 1CC to 2DD.
    # Strategies in [0,1]^16

    max_num_strategies = 2**4

    states = {
        (1,1): 0, # 1CC
        (1,0): 1, # 1CD
        (0,1): 2, # 1DC
        (0,0): 3, # 1DD
    }

    def __init__(self, c, b1, b2=None, eps=0.01):
        self.b1 = b1; # benefit coop in Game 1
        self.c  = c;   # cost to coop in both games
        self.eps = eps

        # player1, player2 payoffs for outcomes CC, CD, DC, and DD.
        self.p1_payoffs = np.asarray([b1-c, -c, b1, 0]);
        self.p2_payoffs = np.asarray([b1-c, b1, -c, 0]);


    def generate_transition_matrix(self, s1, s2):
        [pcc, pcd, pdc, pdd] = self.to_strategy(s1)
        [qcc, qcd, qdc, qdd] = self.to_strategy(s2)

        return np.asarray([
            [pcc*qcc, pcc*(1-qcc), (1-pcc)*qcc, (1-pcc)*(1-qcc)],
            [pcd*qdc, pcd*(1-qdc), (1-pcd)*qdc, (1-pcd)*(1-qdc)],
            [pdc*qcd, pdc*(1-qcd), (1-pdc)*qcd, (1-pdc)*(1-qcd)],
            [pdd*qdd, pdd*(1-qdd), (1-pdd)*qdd, (1-pdd)*(1-qdd)]
        ]);


    def get_stationary_dist(self, s1, s2):
        Q = self.generate_transition_matrix(s1, s2)

        #Q is stochastic, guranteed to have left eigenvector v w/ eigenvalue 1
        # v satisfies Q'v = v, i.e. (Q' - I)v = 0.

    
        #v = null_space(np.transpose(Q)-np.ones(Q.shape))
        try:
            l, v = sp.eigs(Q.T, k=1, which='LM')

            v = v.T[0]
            v = np.absolute(v/np.sum(v))
        
            assert np.allclose(v, np.matmul(v, Q))

            return v

        except Exception as e:
            print("s1 = {:}, s2 = {:}".format(s1, s2)) 
            print("Q \n {:}".format(Q))

            raise(e)

    def to_strategy(self, num):
        return [int(x)*(1-2*self.eps)+self.eps for x in format(num, '04b')]

    def strat_to_str(self, num):
        arr = self.to_strategy(num)
        return str(arr)

    def get_stats(self, s1, s2):
        
        # v = stationary proportion in states
        v = self.get_stationary_dist(s1, s2)

        s1_payoff = np.dot(v, self.p1_payoffs)
        s2_payoff = np.dot(v, self.p2_payoffs)

        # print("s1 payoff ", s1_payoff)
        # print("v ", v)
        # print("p1 payoffs", self.p1_payoffs)
    
        # player 1 cooperates in states CC and CD

        s1_single_c_rate = v[0] + v[1]
        s2_single_c_rate = v[0] + v[2] # player 2 cooperates in states CC and DC
        

        # cc_rate = v[0]

        # print("v", v)
        # print("s1_payoff", s1_payoff)
        # print("s2_payoff", s2_payoff)
        # print("s1_cc_rate", s1_cc_rate)
        # print("s2_cc_rate", s2_cc_rate)

        frac_game1 = 1.0

        if s1_single_c_rate < 0 or s2_single_c_rate < 0:
            print("anomaly")
            print(s1, s2)
            print(v)
            print(s1_single_c_rate, s2_single_c_rate)
            print("done")

        return (s1_payoff, s2_payoff, s1_single_c_rate, s2_single_c_rate, frac_game1)

        
    # def mc_estimate(self, s1, s2, n = 30, initial_state = 0):
    #     '''
    #         Return avg payoffs when s1 plays s2 and CC rate
    #     '''
    #     s1_total_payoff = 0.0
    #     s2_total_payoff = 0.0

    #     cc_rate     = 0.0

    #     prev_state = initial_state

    #     s1 = Pure_One_Game.to_strategy(s1)
    #     s2 = Pure_One_Game.to_strategy(s2)

    #     for i in range(n):
    #         s1_move = s1[prev_state]
    #         s2_move = s2[prev_state]
            
    #         curr_state = Pure_One_Game.states[(s1_move, s2_move)]

    #         s1_total_payoff += self.p1_payoffs[curr_state]
    #         s2_total_payoff += self.p2_payoffs[curr_state]

    #         # mutual cooperation = 1CC or 2CC
    #         if curr_state # 4 == 0:
    #             cc_rate += 1


    #     # return s1 avg payoff, s2 avg payoff, avg CC ratex
    #     return (s1_total_payoff/n, s2_total_payoff/n, cc_rate/n, 1.0)


    # def q_estimate(self, s1, s2, initial_state = 0):
    #     pass
