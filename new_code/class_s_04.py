import numpy as np

from class_game import Game

class S_4_Game(Game):

    strat_len = 4
    ALLD = (0,0,0,0)

    def __init__(self, c, b1):

        self.c = c
        self.b1 = b1
        self.set_payoffs()

    # player1, player2 payoffs for outcomes CC, CD, DC, and DD.
    def set_payoffs(self):
        self.p1_payoffs = np.asarray([b1-c, -c, b1, 0]);
        self.p2_payoffs = np.asarray([b1-c, b1, -c, 0]);


    def generate_transition_matrix(self, s1, s2):
        (pcc, pcd, pdc, pdd) = self.to_strategy(s1)
        (qcc, qcd, qdc, qdd) = self.to_strategy(s2)

        return np.asarray([
            [pcc*qcc, pcc*(1-qcc), (1-pcc)*qcc, (1-pcc)*(1-qcc)],
            [pcd*qdc, pcd*(1-qdc), (1-pcd)*qdc, (1-pcd)*(1-qdc)],
            [pdc*qcd, pdc*(1-qcd), (1-pdc)*qcd, (1-pdc)*(1-qcd)],
            [pdd*qdd, pdd*(1-qdd), (1-pdd)*qdd, (1-pdd)*(1-qdd)]
        ]);