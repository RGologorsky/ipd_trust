import numpy as np

from class_game import Game

class TwoGame(Game):

    # 1CC, ..., 1DD, 2CC, ... 2DD
    num_states = 8

    num_to_state = {
        0: (1,0,0,0,0,0,0,0),
        1: (0,1,0,0,0,0,0,0),
        2: (0,0,1,0,0,0,0,0),
        3: (0,0,0,1,0,0,0,0),
        4: (0,0,0,0,1,0,0,0),
        5: (0,0,0,0,0,1,0,0),
        6: (0,0,0,0,0,0,1,0),
        7: (0,0,0,0,0,0,0,1),
    }

    state_to_num = {val: key for key, val in num_to_state.items()}

    # environment state transition probability given each player's state preference
    @staticmethod
    def f(a,b): 
        return a*b

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

class S_8_Game(TwoGame):

    strat_len = 8

    def generate_transition_matrix(self, s1, s2):
        (pcc, pcd, pdc, pdd,  xcc, xcd, xdc, xdd) = s1
        (qcc, qcd, qdc, qdd,  ycc, ycd, ydc, ydd) = s2

        return np.asarray([
            [
                self.f(xcc, ycc)*pcc*qcc, \
                self.f(xcc, ycc)*pcc*(1 - qcc), \
                self.f(xcc, ycc)*(1 - pcc)*qcc, \
                self.f(xcc, ycc)*(1 - pcc)*(1 - qcc), \
                (1 - self.f(xcc, ycc))*pcc* qcc, \
                (1 - self.f(xcc, ycc))*pcc* (1 - qcc), \
                (1 - self.f(xcc, ycc))* (1 - pcc)*qcc, \
                (1 - self.f(xcc, ycc))* (1 - pcc)* (1 - qcc) \
            ],

            [
                self.f(xcd, ydc)*pcd*qdc, \
                self.f(xcd, ydc)*pcd*(1 - qdc), \
                self.f(xcd, ydc)*(1 - pcd)*qdc, \
                self.f(xcd, ydc)*(1 - pcd)*(1 - qdc), \
                (1 - self.f(xcd, ydc))*pcd*qdc, \
                (1 - self.f(xcd, ydc))*pcd*(1 - qdc), \
                (1 - self.f(xcd, ydc))*(1 - pcd)*qdc, \
                (1 - self.f(xcd, ydc))*(1 - pcd)*(1 - qdc), \
            ],

            [
                self.f(xdc, ycd)*pdc*qcd, \
                self.f(xdc, ycd)*pdc*(1 - qcd), \
                self.f(xdc, ycd)* (1 - pdc)*qcd, \
                self.f(xdc, ycd)*(1 - pdc)*(1 - qcd), \
                (1 - self.f(xdc, ycd))*pdc*qcd, \
                (1 - self.f(xdc, ycd))*pdc*(1 - qcd), \
                (1 - self.f(xdc, ycd))*(1 - pdc)* qcd, \
                (1 - self.f(xdc, ycd))*(1 - pdc)*(1 - qcd), \
            ],

            [
                self.f(xdd, ydd)*pdd*qdd, \
                self.f(xdd, ydd)*pdd*(1 - qdd), \
                self.f(xdd, ydd)*(1 - pdd)*qdd, \
                self.f(xdd, ydd)*(1 - pdd)*(1 - qdd), \
                (1 - self.f(xdd, ydd))*pdd*qdd, \
                (1 - self.f(xdd, ydd))*pdd*(1 - qdd), \
                (1 - self.f(xdd, ydd))*(1 - pdd)*qdd, \
                (1 - self.f(xdd, ydd))*(1 - pdd)*(1 - qdd), \
            ],

            [
                self.f(xcc, ycc)*pcc*qcc, \
                self.f(xcc, ycc)*pcc*(1 - qcc), \
                self.f(xcc, ycc)*(1 - pcc)*qcc, \
                self.f(xcc, ycc)*(1 - pcc)*(1 - qcc), \
                (1 - self.f(xcc, ycc))*pcc* qcc, \
                (1 - self.f(xcc, ycc))*pcc* (1 - qcc), \
                (1 - self.f(xcc, ycc))* (1 - pcc)*qcc, \
                (1 - self.f(xcc, ycc))* (1 - pcc)* (1 - qcc), \
            ],

            [
                self.f(xcd, ydc)*pcd*qdc, \
                self.f(xcd, ydc)*pcd*(1 - qdc), \
                self.f(xcd, ydc)*(1 - pcd)*qdc, \
                self.f(xcd, ydc)*(1 - pcd)*(1 - qdc), \
                (1 - self.f(xcd, ydc))*pcd*qdc, \
                (1 - self.f(xcd, ydc))*pcd*(1 - qdc), \
                (1 - self.f(xcd, ydc))*(1 - pcd)*qdc, \
                (1 - self.f(xcd, ydc))*(1 - pcd)*(1 - qdc), \
            ],

            [
                self.f(xdc, ycd)*pdc*qcd, \
                self.f(xdc, ycd)*pdc*(1 - qcd), \
                self.f(xdc, ycd)* (1 - pdc)*qcd, \
                self.f(xdc, ycd)*(1 - pdc)*(1 - qcd), \
                (1 - self.f(xdc, ycd))*pdc*qcd, \
                (1 - self.f(xdc, ycd))*pdc*(1 - qcd), \
                (1 - self.f(xdc, ycd))*(1 - pdc)* qcd, \
                (1 - self.f(xdc, ycd))*(1 - pdc)*(1 - qcd), \
            ],

            [
                self.f(xdd, ydd)*pdd*qdd, \
                self.f(xdd, ydd)*pdd*(1 - qdd), \
                self.f(xdd, ydd)*(1 - pdd)*qdd, \
                self.f(xdd, ydd)*(1 - pdd)*(1 - qdd), \
                (1 - self.f(xdd, ydd))*pdd*qdd, \
                (1 - self.f(xdd, ydd))*pdd*(1 - qdd), \
                (1 - self.f(xdd, ydd))*(1 - pdd)*qdd, \
                (1 - self.f(xdd, ydd))*(1 - pdd)*(1 - qdd), \
            ]
        ]);


class S_12_Game(TwoGame):

    strat_len = 12

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

class S_16_Game(TwoGame):

    strat_len = 16

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