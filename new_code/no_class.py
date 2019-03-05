import numpy as np
from helper_functions import get_params #get_params(params_needed, params_dict)
# Needed Game Functions for Evolutionary Sim

  
def reset_b1(game_d, b1):
    game_d["b1"] = b1
    
    b2,c = get_params(["b2", "c"], game_d)

    # set payoffs
    game_d["p1_payoffs"] = np.asarray([b1-c, -c, b1, 0, b2-c, -c, b2, 0]);
    game_d["p2_payoffs"] = np.asarray([b1-c, b1, -c, 0, b2-c, b2, -c, 0]);


def set_game_transition_dynamics(game_d, game_transition_dynamics):

    if game_transition_dynamics == "EqualSay_G2_Default":
        # Prob[G1] = Prob[player 1 AND player 2 want G1]
        def f(a,b): return a*b
        game_d["f"] = f
        return

    elif game_transition_dynamics == "EqualSay_G1_Default":
        # Prob[G1] = 1 - Prob[player 1 AND player 2 want G2]
        # = Prob[player 1 OR player 2 want G1] = a + b - a*b
        def f(a,b): return a + b - a*b # return 1 - (1-a)*(1-b)
        game_d["f"] = f
        return

    elif game_transition_dynamics == "Unilateral_Dictator":
        # Prob[G1] =  Prob[player 1 wants G1] = a, or
        # Prob[G1] = Prob[plaeyr 2 wants G2] = b.
        def f_player1_dictator (a,b): return a 
        def f_player2_dictator (a,b): return b

        game_d["f"] = (f_player1_dictator, f_player2_dictator)
        return

    elif game_transition_dynamics == "Player2_Dictator":
        # Prob[G1] =  Prob[player 1 wants G1]
        def f(a,b): return b
        
        game_d["f"] = f
        return

    elif game_transition_dynamics == "Random_Dictator":
        # Prob[G1] =  Prob[player 1 dictator and he wants G1] + Prob[player 2 dictator and he wants G1]
        def f(a,b):
            return 0.5*a + 0.5*b
        
        game_d["f"] = f
        return

    elif game_transition_dynamics == "Random":
        # Prob[G1] =  0.50
        def f(a,b):
            return 0.5
        
        game_d["f"] = f
        return

    else:
        raise ValueError("Unknown Game1 <-> Game2 transition dynamics.")


def generate_S_16_Q(game_d, s1, s2):

    f = game_d["f"]

    (p1cc, p1cd, p1dc, p1dd, p2cc, p2cd, p2dc, p2dd, \
     x1cc, x1cd, x1dc, x1dd, x2cc, x2cd, x2dc, x2dd) = s1

    (q1cc, q1cd, q1dc, q1dd, q2cc, q2cd, q2dc, q2dd, \
     y1cc, y1cd, y1dc, y1dd, y2cc, y2cd, y2dc, y2dd) = s2

    return np.asarray([
        [
            f(x1cc, y1cc)*p1cc*q1cc, \
            f(x1cc, y1cc)*p1cc*(1 - q1cc), \
            f(x1cc, y1cc)*(1 - p1cc)*q1cc, \
            f(x1cc, y1cc)*(1 - p1cc)*(1 - q1cc), \
            (1 - f(x1cc, y1cc))*p2cc* q2cc, \
            (1 - f(x1cc, y1cc))*p2cc* (1 - q2cc), \
            (1 - f(x1cc, y1cc))* (1 - p2cc)*q2cc, \
            (1 - f(x1cc, y1cc))* (1 - p2cc)* (1 - q2cc) \
        ],

        [
            f(x1cd, y1dc)*p1cd*q1dc, \
            f(x1cd, y1dc)*p1cd*(1 - q1dc), \
            f(x1cd, y1dc)*(1 - p1cd)*q1dc, \
            f(x1cd, y1dc)*(1 - p1cd)*(1 - q1dc), \
            (1 - f(x1cd, y1dc))*p2cd*q2dc, \
            (1 - f(x1cd, y1dc))*p2cd*(1 - q2dc), \
            (1 - f(x1cd, y1dc))*(1 - p2cd)*q2dc, \
            (1 - f(x1cd, y1dc))*(1 - p2cd)*(1 - q2dc), \
        ],

        [
            f(x1dc, y1cd)*p1dc*q1cd, \
            f(x1dc, y1cd)*p1dc*(1 - q1cd), \
            f(x1dc, y1cd)* (1 - p1dc)*q1cd, \
            f(x1dc, y1cd)*(1 - p1dc)*(1 - q1cd), \
            (1 - f(x1dc, y1cd))*p2dc*q2cd, \
            (1 - f(x1dc, y1cd))*p2dc*(1 - q2cd), \
            (1 - f(x1dc, y1cd))*(1 - p2dc)* q2cd, \
            (1 - f(x1dc, y1cd))*(1 - p2dc)*(1 - q2cd), \
        ],

        [
            f(x1dd, y1dd)*p1dd*q1dd, \
            f(x1dd, y1dd)*p1dd*(1 - q1dd), \
            f(x1dd, y1dd)*(1 - p1dd)*q1dd, \
            f(x1dd, y1dd)*(1 - p1dd)*(1 - q1dd), \
            (1 - f(x1dd, y1dd))*p2dd*q2dd, \
            (1 - f(x1dd, y1dd))*p2dd*(1 - q2dd), \
            (1 - f(x1dd, y1dd))*(1 - p2dd)*q2dd, \
            (1 - f(x1dd, y1dd))*(1 - p2dd)*(1 - q2dd), \
        ],

        [
            f(x2cc, y2cc)*p1cc*q1cc, \
            f(x2cc, y2cc)*p1cc*(1 - q1cc), \
            f(x2cc, y2cc)*(1 - p1cc)*q1cc, \
            f(x2cc, y2cc)*(1 - p1cc)*(1 - q1cc), \
            (1 - f(x2cc, y2cc))*p2cc* q2cc, \
            (1 - f(x2cc, y2cc))*p2cc* (1 - q2cc), \
            (1 - f(x2cc, y2cc))* (1 - p2cc)*q2cc, \
            (1 - f(x2cc, y2cc))* (1 - p2cc)* (1 - q2cc), \
        ],

        [
            f(x2cd, y2dc)*p1cd*q1dc, \
            f(x2cd, y2dc)*p1cd*(1 - q1dc), \
            f(x2cd, y2dc)*(1 - p1cd)*q1dc, \
            f(x2cd, y2dc)*(1 - p1cd)*(1 - q1dc), \
            (1 - f(x2cd, y2dc))*p2cd*q2dc, \
            (1 - f(x2cd, y2dc))*p2cd*(1 - q2dc), \
            (1 - f(x2cd, y2dc))*(1 - p2cd)*q2dc, \
            (1 - f(x2cd, y2dc))*(1 - p2cd)*(1 - q2dc), \
        ],

        [
            f(x2dc, y2cd)*p1dc*q1cd, \
            f(x2dc, y2cd)*p1dc*(1 - q1cd), \
            f(x2dc, y2cd)* (1 - p1dc)*q1cd, \
            f(x2dc, y2cd)*(1 - p1dc)*(1 - q1cd), \
            (1 - f(x2dc, y2cd))*p2dc*q2cd, \
            (1 - f(x2dc, y2cd))*p2dc*(1 - q2cd), \
            (1 - f(x2dc, y2cd))*(1 - p2dc)* q2cd, \
            (1 - f(x2dc, y2cd))*(1 - p2dc)*(1 - q2cd), \
        ],

        [
            f(x2dd, y2dd)*p1dd*q1dd, \
            f(x2dd, y2dd)*p1dd*(1 - q1dd), \
            f(x2dd, y2dd)*(1 - p1dd)*q1dd, \
            f(x2dd, y2dd)*(1 - p1dd)*(1 - q1dd), \
            (1 - f(x2dd, y2dd))*p2dd*q2dd, \
            (1 - f(x2dd, y2dd))*p2dd*(1 - q2dd), \
            (1 - f(x2dd, y2dd))*(1 - p2dd)*q2dd, \
            (1 - f(x2dd, y2dd))*(1 - p2dd)*(1 - q2dd), \
        ]
    ])

def get_stationary_dist(game_d, s1, s2, tolerance=1e-15):
    Q = self.generate_transition_matrix(s1, s2)

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


    def get_unilateral_stationary_dist(self, s1, s2):

        self.f = self.f_player1_dictator
        v1 = self.get_stationary_dist(s1, s2)

        self.f = self.f_player2_dictator
        v2 =  self.get_stationary_dist(s1, s2)

        # reset f, so no confusion arises later
        self.f = self.f_pass

        return (v1 + v2)/2.0


    # calculates average payoffs
    def get_payoffs(self, s1, s2):

        if self.game_transition_dynamics == "Unilateral_Dictator":
            v = self.get_unilateral_stationary_dist(s1, s2)
        else:
            v = self.get_stationary_dist(s1, s2)

        s1_payoff = np.dot(v, self.p1_payoffs)
        s2_payoff = np.dot(v, self.p2_payoffs)

        return (s1_payoff, s2_payoff)

    # calculate average payoffs, probability of mutual cooperative state and game 1 state
    def get_stats(self, s1, s2):

        if self.game_transition_dynamics == "Unilateral_Dictator":
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

    # each specifc game class must implement these two methods
    def generate_transition_matrix(self, s1, s2):
        pass

    def set_payoffs(self):
        pass
