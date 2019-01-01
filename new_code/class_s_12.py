import numpy as np

from class_game import Game

class S_12_Game(Game):

    strat_len = 12

    # environment state transition probability given each player's state preference
    f = lambda a, b: a * b

    def __init__(self, c, b1, b2):
        self.c = c
        self.b1 = b1
        self.b2  = b2

        self.set_payoffs()

    def set_payoffs(self):
        b1 = self.b1
        b2 = self.b2
        c = self.c

        self.p1_payoffs = np.asarray([b1-c, -c, b1, 0, b2-c, -c, b2, 0]);
        self.p2_payoffs = np.asarray([b1-c, b1, -c, 0, b2-c, b2, -c, 0]);

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
