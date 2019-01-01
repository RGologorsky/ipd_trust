import numpy as np
from class_two import Two_Game

class S_16_Game(Two_Game):

    strat_len = 16
    ALLD = (0,0,0,0, 0,0,0,0, 1,1,1,1, 1,1,1,1)

    # environment state transition probability given each player's state preference
    f = lambda a, b: a * b

    def __init__(self, c, b1, b2):
        self.c = c
        self.b1 = b1
        self.b2  = b2

        self.set_payoffs()

    def set_payoffs(self):
        self.p1_payoffs = np.asarray([b1-c, -c, b1, 0, b2-c, -c, b2, 0]);
        self.p2_payoffs = np.asarray([b1-c, b1, -c, 0, b2-c, b2, -c, 0]);

    def generate_transition_matrix(self, s1, s2):
        (p1cc, p1cd, p1dc, p1dd, p2cc, p2cd, p2dc, p2dd, \
         x1cc, x1cd, x1dc, x1dd, x2cc, x2cd, x2dc, x2dd) = s1

        (q1cc, q1cd, q1dc, q1dd, q2cc, q2cd, q2dc, q2dd, \
         y1cc, y1cd, y1dc, y1dd, y2cc, y2cd, y2dc, y2dd) = s2

        return np.asarray([
            [
                self.f(x1cc, y1cc)*p1cc*q1cc, \
                self.f(x1cc, y1cc)*p1cc*(1 - q1cc), \
                self.f(x1cc, y1cc)*(1 - p1cc)*q1cc, \
                self.f(x1cc, y1cc)*(1 - p1cc)*(1 - q1cc), \
                (1 - self.f(x1cc, y1cc))*p2cc* q2cc, \
                (1 - self.f(x1cc, y1cc))*p2cc* (1 - q2cc), \
                (1 - self.f(x1cc, y1cc))* (1 - p2cc)*q2cc, \
                (1 - self.f(x1cc, y1cc))* (1 - p2cc)* (1 - q2cc) \
            ],

            [
                self.f(x1cd, y1dc)*p1cd*q1dc, \
                self.f(x1cd, y1dc)*p1cd*(1 - q1dc), \
                self.f(x1cd, y1dc)*(1 - p1cd)*q1dc, \
                self.f(x1cd, y1dc)*(1 - p1cd)*(1 - q1dc), \
                (1 - self.f(x1cd, y1dc))*p2cd*q2dc, \
                (1 - self.f(x1cd, y1dc))*p2cd*(1 - q2dc), \
                (1 - self.f(x1cd, y1dc))*(1 - p2cd)*q2dc, \
                (1 - self.f(x1cd, y1dc))*(1 - p2cd)*(1 - q2dc), \
            ],

            [
                self.f(x1dc, y1cd)*p1dc*q1cd, \
                self.f(x1dc, y1cd)*p1dc*(1 - q1cd), \
                self.f(x1dc, y1cd)* (1 - p1dc)*q1cd, \
                self.f(x1dc, y1cd)*(1 - p1dc)*(1 - q1cd), \
                (1 - self.f(x1dc, y1cd))*p2dc*q2cd, \
                (1 - self.f(x1dc, y1cd))*p2dc*(1 - q2cd), \
                (1 - self.f(x1dc, y1cd))*(1 - p2dc)* q2cd, \
                (1 - self.f(x1dc, y1cd))*(1 - p2dc)*(1 - q2cd), \
            ],

            [
                self.f(x1dd, y1dd)*p1dd*q1dd, \
                self.f(x1dd, y1dd)*p1dd*(1 - q1dd), \
                self.f(x1dd, y1dd)*(1 - p1dd)*q1dd, \
                self.f(x1dd, y1dd)*(1 - p1dd)*(1 - q1dd), \
                (1 - self.f(x1dd, y1dd))*p2dd*q2dd, \
                (1 - self.f(x1dd, y1dd))*p2dd*(1 - q2dd), \
                (1 - self.f(x1dd, y1dd))*(1 - p2dd)*q2dd, \
                (1 - self.f(x1dd, y1dd))*(1 - p2dd)*(1 - q2dd), \
            ],

            [
                self.f(x2cc, y2cc)*p1cc*q1cc, \
                self.f(x2cc, y2cc)*p1cc*(1 - q1cc), \
                self.f(x2cc, y2cc)*(1 - p1cc)*q1cc, \
                self.f(x2cc, y2cc)*(1 - p1cc)*(1 - q1cc), \
                (1 - self.f(x2cc, y2cc))*p2cc* q2cc, \
                (1 - self.f(x2cc, y2cc))*p2cc* (1 - q2cc), \
                (1 - self.f(x2cc, y2cc))* (1 - p2cc)*q2cc, \
                (1 - self.f(x2cc, y2cc))* (1 - p2cc)* (1 - q2cc), \
            ],

            [
                self.f(x2cd, y2dc)*p1cd*q1dc, \
                self.f(x2cd, y2dc)*p1cd*(1 - q1dc), \
                self.f(x2cd, y2dc)*(1 - p1cd)*q1dc, \
                self.f(x2cd, y2dc)*(1 - p1cd)*(1 - q1dc), \
                (1 - self.f(x2cd, y2dc))*p2cd*q2dc, \
                (1 - self.f(x2cd, y2dc))*p2cd*(1 - q2dc), \
                (1 - self.f(x2cd, y2dc))*(1 - p2cd)*q2dc, \
                (1 - self.f(x2cd, y2dc))*(1 - p2cd)*(1 - q2dc), \
            ],

            [
                self.f(x2dc, y2cd)*p1dc*q1cd, \
                self.f(x2dc, y2cd)*p1dc*(1 - q1cd), \
                self.f(x2dc, y2cd)* (1 - p1dc)*q1cd, \
                self.f(x2dc, y2cd)*(1 - p1dc)*(1 - q1cd), \
                (1 - self.f(x2dc, y2cd))*p2dc*q2cd, \
                (1 - self.f(x2dc, y2cd))*p2dc*(1 - q2cd), \
                (1 - self.f(x2dc, y2cd))*(1 - p2dc)* q2cd, \
                (1 - self.f(x2dc, y2cd))*(1 - p2dc)*(1 - q2cd), \
            ],

            [
                self.f(x2dd, y2dd)*p1dd*q1dd, \
                self.f(x2dd, y2dd)*p1dd*(1 - q1dd), \
                self.f(x2dd, y2dd)*(1 - p1dd)*q1dd, \
                self.f(x2dd, y2dd)*(1 - p1dd)*(1 - q1dd), \
                (1 - self.f(x2dd, y2dd))*p2dd*q2dd, \
                (1 - self.f(x2dd, y2dd))*p2dd*(1 - q2dd), \
                (1 - self.f(x2dd, y2dd))*(1 - p2dd)*q2dd, \
                (1 - self.f(x2dd, y2dd))*(1 - p2dd)*(1 - q2dd), \
            ]
        ])
