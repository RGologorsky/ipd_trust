import numpy as np
from class_two import Two_Game

class S_12_Game(Two_Game):

    # Calculating Game Transitions, specific payoffs between strategies.

    # 8 states, ranging from 0 to 7, corresponding to 1CC to 2DD.
    # Strategies in [0,1]^16

    def __init__(self, c, b1, b2):
        self.strat_len = 12
        self.ALLD = (0,0,0,0, 0,0,0,0, 1,1,1,1)

        super().__init__(c, b1, b2)



    def generate_transition_matrix(self, s1, s2):
        (p1cc, p1cd, p1dc, p1dd, p2cc, p2cd, p2dc, p2dd, xcc, xcd, xdc, xdd) = s1
        (q1cc, q1cd, q1dc, q1dd, q2cc, q2cd, q2dc, q2dd, ycc, ycd, ydc, ydd) = s2

        return np.asarray([
            [
                self.f(xcc, ycc)*p1cc*q1cc, \
                self.f(xcc, ycc)*p1cc*(1 - q1cc), \
                self.f(xcc, ycc)*(1 - p1cc)*q1cc, \
                self.f(xcc, ycc)*(1 - p1cc)*(1 - q1cc), \
                (1 - self.f(xcc, ycc))*p2cc* q2cc, \
                (1 - self.f(xcc, ycc))*p2cc* (1 - q2cc), \
                (1 - self.f(xcc, ycc))* (1 - p2cc)*q2cc, \
                (1 - self.f(xcc, ycc))* (1 - p2cc)* (1 - q2cc) \
            ],

            [
                self.f(xcd, ydc)*p1cd*q1dc, \
                self.f(xcd, ydc)*p1cd*(1 - q1dc), \
                self.f(xcd, ydc)*(1 - p1cd)*q1dc, \
                self.f(xcd, ydc)*(1 - p1cd)*(1 - q1dc), \
                (1 - self.f(xcd, ydc))*p2cd*q2dc, \
                (1 - self.f(xcd, ydc))*p2cd*(1 - q2dc), \
                (1 - self.f(xcd, ydc))*(1 - p2cd)*q2dc, \
                (1 - self.f(xcd, ydc))*(1 - p2cd)*(1 - q2dc), \
            ],

            [
                self.f(xdc, ycd)*p1dc*q1cd, \
                self.f(xdc, ycd)*p1dc*(1 - q1cd), \
                self.f(xdc, ycd)* (1 - p1dc)*q1cd, \
                self.f(xdc, ycd)*(1 - p1dc)*(1 - q1cd), \
                (1 - self.f(xdc, ycd))*p2dc*q2cd, \
                (1 - self.f(xdc, ycd))*p2dc*(1 - q2cd), \
                (1 - self.f(xdc, ycd))*(1 - p2dc)* q2cd, \
                (1 - self.f(xdc, ycd))*(1 - p2dc)*(1 - q2cd), \
            ],

            [
                self.f(xdd, ydd)*p1dd*q1dd, \
                self.f(xdd, ydd)*p1dd*(1 - q1dd), \
                self.f(xdd, ydd)*(1 - p1dd)*q1dd, \
                self.f(xdd, ydd)*(1 - p1dd)*(1 - q1dd), \
                (1 - self.f(xdd, ydd))*p2dd*q2dd, \
                (1 - self.f(xdd, ydd))*p2dd*(1 - q2dd), \
                (1 - self.f(xdd, ydd))*(1 - p2dd)*q2dd, \
                (1 - self.f(xdd, ydd))*(1 - p2dd)*(1 - q2dd), \
            ],

            [
                self.f(xcc, ycc)*p1cc*q1cc, \
                self.f(xcc, ycc)*p1cc*(1 - q1cc), \
                self.f(xcc, ycc)*(1 - p1cc)*q1cc, \
                self.f(xcc, ycc)*(1 - p1cc)*(1 - q1cc), \
                (1 - self.f(xcc, ycc))*p2cc* q2cc, \
                (1 - self.f(xcc, ycc))*p2cc* (1 - q2cc), \
                (1 - self.f(xcc, ycc))* (1 - p2cc)*q2cc, \
                (1 - self.f(xcc, ycc))* (1 - p2cc)* (1 - q2cc), \
            ],

            [
                self.f(xcd, ydc)*p1cd*q1dc, \
                self.f(xcd, ydc)*p1cd*(1 - q1dc), \
                self.f(xcd, ydc)*(1 - p1cd)*q1dc, \
                self.f(xcd, ydc)*(1 - p1cd)*(1 - q1dc), \
                (1 - self.f(xcd, ydc))*p2cd*q2dc, \
                (1 - self.f(xcd, ydc))*p2cd*(1 - q2dc), \
                (1 - self.f(xcd, ydc))*(1 - p2cd)*q2dc, \
                (1 - self.f(xcd, ydc))*(1 - p2cd)*(1 - q2dc), \
            ],

            [
                self.f(xdc, ycd)*p1dc*q1cd, \
                self.f(xdc, ycd)*p1dc*(1 - q1cd), \
                self.f(xdc, ycd)* (1 - p1dc)*q1cd, \
                self.f(xdc, ycd)*(1 - p1dc)*(1 - q1cd), \
                (1 - self.f(xdc, ycd))*p2dc*q2cd, \
                (1 - self.f(xdc, ycd))*p2dc*(1 - q2cd), \
                (1 - self.f(xdc, ycd))*(1 - p2dc)* q2cd, \
                (1 - self.f(xdc, ycd))*(1 - p2dc)*(1 - q2cd), \
            ],

            [
                self.f(xdd, ydd)*p1dd*q1dd, \
                self.f(xdd, ydd)*p1dd*(1 - q1dd), \
                self.f(xdd, ydd)*(1 - p1dd)*q1dd, \
                self.f(xdd, ydd)*(1 - p1dd)*(1 - q1dd), \
                (1 - self.f(xdd, ydd))*p2dd*q2dd, \
                (1 - self.f(xdd, ydd))*p2dd*(1 - q2dd), \
                (1 - self.f(xdd, ydd))*(1 - p2dd)*q2dd, \
                (1 - self.f(xdd, ydd))*(1 - p2dd)*(1 - q2dd), \
            ]
        ])
