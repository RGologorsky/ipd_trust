import numpy as np

from class_game import Game

class Reactive_Game(Game):

    # Calculating Game Transitions, specific payoffs between strategies.

    # 8 states, ranging from 0 to 7, corresponding to 1CC to 2DD.
    # Strategies in [0,1]^16


    def __init__(self, c, b1):
        super().__init__(c, b1)

        self.strat_len = 2

        # player1, player2 payoffs for outcomes CC, CD, DC, and DD.
        self.p1_payoffs = np.asarray([b1-c, -c, b1, 0]);
        self.p2_payoffs = np.asarray([b1-c, b1, -c, 0]);


        self.ALLD = (0.005,0.005)


    def generate_transition_matrix(self, s1, s2):

        (pc, pd) = s1
        (qc, qd) = s2

        return np.asarray([
            [pc*qc, pc*(1-qc), (1-pc)*qc, (1-pc)*(1-qc)],
            [pc*qd, pc*(1-qd), (1-pc)*qd, (1-pc)*(1-qd)],
            [pd*qc, pd*(1-qc), (1-pd)*qc, (1-pd)*(1-qc)],
            [pd*qd, pd*(1-qd), (1-pd)*qd, (1-pd)*(1-qd)]
        ]);
