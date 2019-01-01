import numpy as np

from class_game import Game

class S_2_Game(Game):

    strat_len = 2
    ALLD = (0, 0)

    def __init__(self, c, b1):
        self.c = c
        self.b1 = b1
        self.set_payoffs()

    def set_payoffs(self):
        self.p1_payoffs = np.asarray([b1-c, -c, b1, 0]);
        self.p2_payoffs = np.asarray([b1-c, b1, -c, 0]);

    def generate_transition_matrix(self, s1, s2):

        (pc, pd) = s1
        (qc, qd) = s2

        return np.asarray([
            [pc*qc, pc*(1-qc), (1-pc)*qc, (1-pc)*(1-qc)],
            [pc*qd, pc*(1-qd), (1-pc)*qd, (1-pc)*(1-qd)],
            [pd*qc, pd*(1-qc), (1-pd)*qc, (1-pd)*(1-qc)],
            [pd*qd, pd*(1-qd), (1-pd)*qd, (1-pd)*(1-qd)]
        ]);
