import numpy as np

from class_game import Game

class OneGame(Game):

    # CC, CD, DC, DD
    num_states = 4

    def __init__(self, c, b1):
        self.c = c
        self.b1 = b1
        self.set_payoffs()

    def set_payoffs(self):
        b1 = self.b1
        c = self.c

        self.p1_payoffs = np.asarray([b1-c, -c, b1, 0]);
        self.p2_payoffs = np.asarray([b1-c, b1, -c, 0]);


class S_2_Game(OneGame):

    strat_len = 2

    def generate_transition_matrix(self, s1, s2):

        (pc, pd) = s1
        (qc, qd) = s2

        return np.asarray([
            [pc*qc, pc*(1-qc), (1-pc)*qc, (1-pc)*(1-qc)],
            [pd*qc, pd*(1-qc), (1-pd)*qc, (1-pd)*(1-qc)],
            [pc*qd, pc*(1-qd), (1-pc)*qd, (1-pc)*(1-qd)],
            [pd*qd, pd*(1-qd), (1-pd)*qd, (1-pd)*(1-qd)]
        ]);

class S_4_Game(OneGame):

    strat_len = 4

    def generate_transition_matrix(self, s1, s2):
        (pcc, pcd, pdc, pdd) = s1
        (qcc, qcd, qdc, qdd) = s2

        return np.asarray([
            [pcc*qcc, pcc*(1-qcc), (1-pcc)*qcc, (1-pcc)*(1-qcc)],
            [pcd*qdc, pcd*(1-qdc), (1-pcd)*qdc, (1-pcd)*(1-qdc)],
            [pdc*qcd, pdc*(1-qcd), (1-pdc)*qcd, (1-pdc)*(1-qcd)],
            [pdd*qdd, pdd*(1-qdd), (1-pdd)*qdd, (1-pdd)*(1-qdd)]
        ]);
