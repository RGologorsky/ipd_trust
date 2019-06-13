import numpy as np

from class_game import Game

class OneGame(Game):

    # CC, CD, DC, DD
    num_states = 4
    eye = np.eye(4)

    # maps a number to corresponding state
    num_to_state = {
        0: (1,0,0,0),
        1: (0,1,0,0),
        2: (0,0,1,0),
        3: (0,0,0,1),
    }

    # maps a state to a corresponding number
    state_to_num = {val: key for key, val in num_to_state.items()}


    def __init__(self, b1, c1):
        self.b1 = b1
        self.c1 = c1
        self.alpha1 = b1/c1

        self.set_payoffs()

        self.game_transition_dynamics = "NA"
        self.f = None

    def set_game_transition_dynamics(self, game_transition_dynamics):
        pass

    def set_payoffs(self):
        b1 = self.b1
        c1 = self.c1

        self.p1_payoffs = np.asarray([b1-c1, -c1, b1, 0]);
        self.p2_payoffs = np.asarray([b1-c1, b1, -c1, 0]);

class S_2_Game(OneGame):

    strat_len = 2

    @staticmethod
    def generate_transition_matrix(s1, s2, f=None):

        (pc, pd) = s1
        (qc, qd) = s2

        return np.asarray((
            (pc*qc, pc*(1-qc), (1-pc)*qc, (1-pc)*(1-qc)),
            (pd*qc, pd*(1-qc), (1-pd)*qc, (1-pd)*(1-qc)),
            (pc*qd, pc*(1-qd), (1-pc)*qd, (1-pc)*(1-qd)),
            (pd*qd, pd*(1-qd), (1-pd)*qd, (1-pd)*(1-qd))
        ));

class S_4_Game(OneGame):

    strat_len = 4

    @staticmethod
    def generate_transition_matrix(s1, s2, f=None):
        (pcc, pcd, pdc, pdd) = s1
        (qcc, qcd, qdc, qdd) = s2

        return np.asarray((
            (pcc*qcc, pcc*(1-qcc), (1-pcc)*qcc, (1-pcc)*(1-qcc)),
            (pcd*qdc, pcd*(1-qdc), (1-pcd)*qdc, (1-pcd)*(1-qdc)),
            (pdc*qcd, pdc*(1-qcd), (1-pdc)*qcd, (1-pdc)*(1-qcd)),
            (pdd*qdd, pdd*(1-qdd), (1-pdd)*qdd, (1-pdd)*(1-qdd))
        ));
