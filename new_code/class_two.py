import numpy as np

from class_game import Game

class Two_Game(Game):

    def __init__(self, c, b1, b2):
        super().__init__(c, b1)

        self.b2 = b2; # benefit coop in Game 2

        self.f = lambda a, b: a * b

        # player1, player2 payoffs for outcomes CC, CD, DC, and DD.
        self.p1_payoffs = np.asarray([b1-c, -c, b1, 0, b2-c, -c, b2, 0]);
        self.p2_payoffs = np.asarray([b1-c, b1, -c, 0, b2-c, b2, -c, 0]);
