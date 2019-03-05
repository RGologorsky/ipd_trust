import numpy as np
from random import random

from class_game import Game

class TwoGame(Game):

    # 1CC, ..., 1DD, 2CC, ... 2DD
    num_states = 8
    eye = np.eye(8)

    # maps a number to corresponding state
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

    # maps a state to a corresponding number
    state_to_num = {val: key for key, val in num_to_state.items()}

    # Which game is next? f takes in each player's Prob[prefer Game 1] and outputs Prob[next is Game 1]
    def __init__(self, c, b1, b2, game_transition_dynamics):
        self.c = c
        self.b1 = b1
        self.b2  = b2

        self.set_payoffs()
        self.set_game_transition_dynamics(game_transition_dynamics)


    def set_payoffs(self):
        b1 = self.b1
        b2 = self.b2
        c = self.c

        self.p1_payoffs = np.asarray([b1-c, -c, b1, 0, b2-c, -c, b2, 0]);
        self.p2_payoffs = np.asarray([b1-c, b1, -c, 0, b2-c, b2, -c, 0]);


    def set_game_transition_dynamics(self, game_transition_dynamics):

        self.game_transition_dynamics = game_transition_dynamics

    def get_f(self):

        game_transition_dynamics = self.game_transition_dynamics

        if game_transition_dynamics == "EqualSay_G2_Default":
            # Prob[G1] = Prob[player 1 AND player 2 want G1]
            def f(a,b): return a*b

        elif game_transition_dynamics == "EqualSay_G1_Default":
            # Prob[G1] = 1 - Prob[player 1 AND player 2 want G2]
            # = Prob[player 1 OR player 2 want G1] = a + b - a*b
            def f(a,b): return a + b - a*b # return 1 - (1-a)*(1-b)

        elif game_transition_dynamics == "Unilateral_Dictator":
            # Prob[G1] =  Prob[player 1 wants G1] = a, or
            # Prob[G1] = Prob[plaeyr 2 wants G2] = b.
            def f_player1_dictator (a,b): return a 
            def f_player2_dictator (a,b): return b

            f = (f_player1_dictator, f_player2_dictator)

            
        elif game_transition_dynamics == "Player2_Dictator":
            # Prob[G1] =  Prob[player 1 wants G1]
            def f(a,b): return b

        elif game_transition_dynamics == "Random_Dictator":
            # Prob[G1] =  Prob[player 1 dictator and he wants G1] + Prob[player 2 dictator and he wants G1]
            def f(a,b):
                return 0.5*a + 0.5*b

        elif game_transition_dynamics == "Random":
            # Prob[G1] =  0.50
            def f(a,b):
                return 0.5

        else:
            raise ValueError("Unknown Game1 <-> Game2 transition dynamics.")

        return f



class S_8_Game(TwoGame):

    strat_len = 8

    @staticmethod
    def generate_transition_matrix(f, s1, s2):

        (pcc, pcd, pdc, pdd,  xcc, xcd, xdc, xdd) = s1
        (qcc, qcd, qdc, qdd,  ycc, ycd, ydc, ydd) = s2

        f1 = f(xcc, ycc)
        f2 = f(xcd, ydc)
        f3 = f(xdc, ycd)
        f4 = f(xdd, ydd)
        
        b1 = (
                f1*pcc*qcc,
                f1*pcc*(1 - qcc),
                f1*(1 - pcc)*qcc,
                f1*(1 - pcc)*(1 - qcc),
                (1 - f1)*pcc*qcc,
                (1 - f1)*pcc*(1 - qcc),
                (1 - f1)*(1 - pcc)*qcc,
                (1 - f1)*(1 - pcc)*(1 - qcc),
            )
        b2 = (
                f2*pcd*qdc,
                f2*pcd*(1 - qdc),
                f2*(1 - pcd)*qdc,
                f2*(1 - pcd)*(1 - qdc),
                (1 - f2)*pcd*qdc,
                (1 - f2)*pcd*(1 - qdc),
                (1 - f2)*(1 - pcd)*qdc,
                (1 - f2)*(1 - pcd)*(1 - qdc),
            )
        b3 = (
                f3*pdc*qcd,
                f3*pdc*(1 - qcd),
                f3* (1 - pdc)*qcd,
                f3*(1 - pdc)*(1 - qcd),
                (1 - f3)*pdc*qcd,
                (1 - f3)*pdc*(1 - qcd),
                (1 - f3)*(1 - pdc)* qcd,
                (1 - f3)*(1 - pdc)*(1 - qcd),
            )
        b4 = (
                f4*pdd*qdd,
                f4*pdd*(1 - qdd),
                f4*(1 - pdd)*qdd,
                f4*(1 - pdd)*(1 - qdd),
                (1 - f4)*pdd*qdd,
                (1 - f4)*pdd*(1 - qdd),
                (1 - f4)*(1 - pdd)*qdd,
                (1 - f4)*(1 - pdd)*(1 - qdd),
            )

        return np.asarray((b1, b2, b3, b4, b1, b2, b3, b4))

        # return np.asarray([
        #     [
        #         f(xcc, ycc)*pcc*qcc, \
        #         f(xcc, ycc)*pcc*(1 - qcc), \
        #         f(xcc, ycc)*(1 - pcc)*qcc, \
        #         f(xcc, ycc)*(1 - pcc)*(1 - qcc), \
        #         (1 - f(xcc, ycc))*pcc* qcc, \
        #         (1 - f(xcc, ycc))*pcc* (1 - qcc), \
        #         (1 - f(xcc, ycc))* (1 - pcc)*qcc, \
        #         (1 - f(xcc, ycc))* (1 - pcc)* (1 - qcc) \
        #     ],

        #     [
        #         f(xcd, ydc)*pcd*qdc, \
        #         f(xcd, ydc)*pcd*(1 - qdc), \
        #         f(xcd, ydc)*(1 - pcd)*qdc, \
        #         f(xcd, ydc)*(1 - pcd)*(1 - qdc), \
        #         (1 - f(xcd, ydc))*pcd*qdc, \
        #         (1 - f(xcd, ydc))*pcd*(1 - qdc), \
        #         (1 - f(xcd, ydc))*(1 - pcd)*qdc, \
        #         (1 - f(xcd, ydc))*(1 - pcd)*(1 - qdc), \
        #     ],

        #     [
        #         f(xdc, ycd)*pdc*qcd, \
        #         f(xdc, ycd)*pdc*(1 - qcd), \
        #         f(xdc, ycd)* (1 - pdc)*qcd, \
        #         f(xdc, ycd)*(1 - pdc)*(1 - qcd), \
        #         (1 - f(xdc, ycd))*pdc*qcd, \
        #         (1 - f(xdc, ycd))*pdc*(1 - qcd), \
        #         (1 - f(xdc, ycd))*(1 - pdc)* qcd, \
        #         (1 - f(xdc, ycd))*(1 - pdc)*(1 - qcd), \
        #     ],

        #     [
        #         f(xdd, ydd)*pdd*qdd, \
        #         f(xdd, ydd)*pdd*(1 - qdd), \
        #         f(xdd, ydd)*(1 - pdd)*qdd, \
        #         f(xdd, ydd)*(1 - pdd)*(1 - qdd), \
        #         (1 - f(xdd, ydd))*pdd*qdd, \
        #         (1 - f(xdd, ydd))*pdd*(1 - qdd), \
        #         (1 - f(xdd, ydd))*(1 - pdd)*qdd, \
        #         (1 - f(xdd, ydd))*(1 - pdd)*(1 - qdd), \
        #     ],

        #     [
        #         f(xcc, ycc)*pcc*qcc, \
        #         f(xcc, ycc)*pcc*(1 - qcc), \
        #         f(xcc, ycc)*(1 - pcc)*qcc, \
        #         f(xcc, ycc)*(1 - pcc)*(1 - qcc), \
        #         (1 - f(xcc, ycc))*pcc* qcc, \
        #         (1 - f(xcc, ycc))*pcc* (1 - qcc), \
        #         (1 - f(xcc, ycc))* (1 - pcc)*qcc, \
        #         (1 - f(xcc, ycc))* (1 - pcc)* (1 - qcc), \
        #     ],

        #     [
        #         f(xcd, ydc)*pcd*qdc, \
        #         f(xcd, ydc)*pcd*(1 - qdc), \
        #         f(xcd, ydc)*(1 - pcd)*qdc, \
        #         f(xcd, ydc)*(1 - pcd)*(1 - qdc), \
        #         (1 - f(xcd, ydc))*pcd*qdc, \
        #         (1 - f(xcd, ydc))*pcd*(1 - qdc), \
        #         (1 - f(xcd, ydc))*(1 - pcd)*qdc, \
        #         (1 - f(xcd, ydc))*(1 - pcd)*(1 - qdc), \
        #     ],

        #     [
        #         f(xdc, ycd)*pdc*qcd, \
        #         f(xdc, ycd)*pdc*(1 - qcd), \
        #         f(xdc, ycd)* (1 - pdc)*qcd, \
        #         f(xdc, ycd)*(1 - pdc)*(1 - qcd), \
        #         (1 - f(xdc, ycd))*pdc*qcd, \
        #         (1 - f(xdc, ycd))*pdc*(1 - qcd), \
        #         (1 - f(xdc, ycd))*(1 - pdc)* qcd, \
        #         (1 - f(xdc, ycd))*(1 - pdc)*(1 - qcd), \
        #     ],

        #     [
        #         f(xdd, ydd)*pdd*qdd, \
        #         f(xdd, ydd)*pdd*(1 - qdd), \
        #         f(xdd, ydd)*(1 - pdd)*qdd, \
        #         f(xdd, ydd)*(1 - pdd)*(1 - qdd), \
        #         (1 - f(xdd, ydd))*pdd*qdd, \
        #         (1 - f(xdd, ydd))*pdd*(1 - qdd), \
        #         (1 - f(xdd, ydd))*(1 - pdd)*qdd, \
        #         (1 - f(xdd, ydd))*(1 - pdd)*(1 - qdd), \
        #     ]
        # ]);


class S_12_Game(TwoGame):

    strat_len = 12

    @staticmethod
    def generate_transition_matrix(f, s1, s2):
        (p1cc, p1cd, p1dc, p1dd, p2cc, p2cd, p2dc, p2dd, xcc, xcd, xdc, xdd) = s1
        (q1cc, q1cd, q1dc, q1dd, q2cc, q2cd, q2dc, q2dd, ycc, ycd, ydc, ydd) = s2

        f1 = f(xcc, ycc)
        f2 = f(xcd, ydc)
        f3 = f(xdc, ycd)
        f4 = f(xdd, ydd)
        
        b1 = (
                f1*p1cc*q1cc,
                f1*p1cc*(1 - q1cc),
                f1*(1 - p1cc)*q1cc,
                f1*(1 - p1cc)*(1 - q1cc),
                (1 - f1)*p2cc*q2cc,
                (1 - f1)*p2cc*(1 - q2cc),
                (1 - f1)*(1 - p2cc)*q2cc,
                (1 - f1)*(1 - p2cc)*(1 - q2cc),
            )
        b2 = (
                f2*p1cd*q1dc,
                f2*p1cd*(1 - q1dc),
                f2*(1 - p1cd)*q1dc,
                f2*(1 - p1cd)*(1 - q1dc),
                (1 - f2)*p2cd*q2dc,
                (1 - f2)*p2cd*(1 - q2dc),
                (1 - f2)*(1 - p2cd)*q2dc,
                (1 - f2)*(1 - p2cd)*(1 - q2dc),
            )

        b3 = (
                f3*p1dc*q1cd,
                f3*p1dc*(1 - q1cd),
                f3* (1 - p1dc)*q1cd,
                f3*(1 - p1dc)*(1 - q1cd),
                (1 - f3)*p2dc*q2cd,
                (1 - f3)*p2dc*(1 - q2cd),
                (1 - f3)*(1 - p2dc)* q2cd,
                (1 - f3)*(1 - p2dc)*(1 - q2cd),
            )
        b4 = (
                f4*p1dd*q1dd,
                f4*p1dd*(1 - q1dd),
                f4*(1 - p1dd)*q1dd,
                f4*(1 - p1dd)*(1 - q1dd),
                (1 - f4)*p2dd*q2dd,
                (1 - f4)*p2dd*(1 - q2dd),
                (1 - f4)*(1 - p2dd)*q2dd,
                (1 - f4)*(1 - p2dd)*(1 - q2dd),
            )

        return np.asarray((b1, b2, b3, b4, b1, b2, b3, b4))

        # return np.asarray([
        #     [
        #         f(xcc, ycc)*p1cc*q1cc, \
        #         f(xcc, ycc)*p1cc*(1 - q1cc), \
        #         f(xcc, ycc)*(1 - p1cc)*q1cc, \
        #         f(xcc, ycc)*(1 - p1cc)*(1 - q1cc), \
        #         (1 - f(xcc, ycc))*p2cc* q2cc, \
        #         (1 - f(xcc, ycc))*p2cc* (1 - q2cc), \
        #         (1 - f(xcc, ycc))* (1 - p2cc)*q2cc, \
        #         (1 - f(xcc, ycc))* (1 - p2cc)* (1 - q2cc) \
        #     ],

        #     [
        #         f(xcd, ydc)*p1cd*q1dc, \
        #         f(xcd, ydc)*p1cd*(1 - q1dc), \
        #         f(xcd, ydc)*(1 - p1cd)*q1dc, \
        #         f(xcd, ydc)*(1 - p1cd)*(1 - q1dc), \
        #         (1 - f(xcd, ydc))*p2cd*q2dc, \
        #         (1 - f(xcd, ydc))*p2cd*(1 - q2dc), \
        #         (1 - f(xcd, ydc))*(1 - p2cd)*q2dc, \
        #         (1 - f(xcd, ydc))*(1 - p2cd)*(1 - q2dc), \
        #     ],

        #     [
        #         f(xdc, ycd)*p1dc*q1cd, \
        #         f(xdc, ycd)*p1dc*(1 - q1cd), \
        #         f(xdc, ycd)* (1 - p1dc)*q1cd, \
        #         f(xdc, ycd)*(1 - p1dc)*(1 - q1cd), \
        #         (1 - f(xdc, ycd))*p2dc*q2cd, \
        #         (1 - f(xdc, ycd))*p2dc*(1 - q2cd), \
        #         (1 - f(xdc, ycd))*(1 - p2dc)* q2cd, \
        #         (1 - f(xdc, ycd))*(1 - p2dc)*(1 - q2cd), \
        #     ],

        #     [
        #         f(xdd, ydd)*p1dd*q1dd, \
        #         f(xdd, ydd)*p1dd*(1 - q1dd), \
        #         f(xdd, ydd)*(1 - p1dd)*q1dd, \
        #         f(xdd, ydd)*(1 - p1dd)*(1 - q1dd), \
        #         (1 - f(xdd, ydd))*p2dd*q2dd, \
        #         (1 - f(xdd, ydd))*p2dd*(1 - q2dd), \
        #         (1 - f(xdd, ydd))*(1 - p2dd)*q2dd, \
        #         (1 - f(xdd, ydd))*(1 - p2dd)*(1 - q2dd), \
        #     ],

        #     [
        #         f(xcc, ycc)*p1cc*q1cc, \
        #         f(xcc, ycc)*p1cc*(1 - q1cc), \
        #         f(xcc, ycc)*(1 - p1cc)*q1cc, \
        #         f(xcc, ycc)*(1 - p1cc)*(1 - q1cc), \
        #         (1 - f(xcc, ycc))*p2cc* q2cc, \
        #         (1 - f(xcc, ycc))*p2cc* (1 - q2cc), \
        #         (1 - f(xcc, ycc))* (1 - p2cc)*q2cc, \
        #         (1 - f(xcc, ycc))* (1 - p2cc)* (1 - q2cc), \
        #     ],

        #     [
        #         f(xcd, ydc)*p1cd*q1dc, \
        #         f(xcd, ydc)*p1cd*(1 - q1dc), \
        #         f(xcd, ydc)*(1 - p1cd)*q1dc, \
        #         f(xcd, ydc)*(1 - p1cd)*(1 - q1dc), \
        #         (1 - f(xcd, ydc))*p2cd*q2dc, \
        #         (1 - f(xcd, ydc))*p2cd*(1 - q2dc), \
        #         (1 - f(xcd, ydc))*(1 - p2cd)*q2dc, \
        #         (1 - f(xcd, ydc))*(1 - p2cd)*(1 - q2dc), \
        #     ],

        #     [
        #         f(xdc, ycd)*p1dc*q1cd, \
        #         f(xdc, ycd)*p1dc*(1 - q1cd), \
        #         f(xdc, ycd)* (1 - p1dc)*q1cd, \
        #         f(xdc, ycd)*(1 - p1dc)*(1 - q1cd), \
        #         (1 - f(xdc, ycd))*p2dc*q2cd, \
        #         (1 - f(xdc, ycd))*p2dc*(1 - q2cd), \
        #         (1 - f(xdc, ycd))*(1 - p2dc)* q2cd, \
        #         (1 - f(xdc, ycd))*(1 - p2dc)*(1 - q2cd), \
        #     ],

        #     [
        #         f(xdd, ydd)*p1dd*q1dd, \
        #         f(xdd, ydd)*p1dd*(1 - q1dd), \
        #         f(xdd, ydd)*(1 - p1dd)*q1dd, \
        #         f(xdd, ydd)*(1 - p1dd)*(1 - q1dd), \
        #         (1 - f(xdd, ydd))*p2dd*q2dd, \
        #         (1 - f(xdd, ydd))*p2dd*(1 - q2dd), \
        #         (1 - f(xdd, ydd))*(1 - p2dd)*q2dd, \
        #         (1 - f(xdd, ydd))*(1 - p2dd)*(1 - q2dd), \
        #     ]
        # ])

class S_16_Game(TwoGame):

    strat_len = 16

    @staticmethod
    def generate_transition_matrix(f, s1, s2):
        (p1cc, p1cd, p1dc, p1dd, p2cc, p2cd, p2dc, p2dd, \
         x1cc, x1cd, x1dc, x1dd, x2cc, x2cd, x2dc, x2dd) = s1

        (q1cc, q1cd, q1dc, q1dd, q2cc, q2cd, q2dc, q2dd, \
         y1cc, y1cd, y1dc, y1dd, y2cc, y2cd, y2dc, y2dd) = s2

        f1 = f(x1cc, y1cc)
        f2 = f(x1cd, y1dc)
        f3 = f(x1dc, y1cd)
        f4 = f(x1dd, y1dd)
        f5 = f(x2cc, y2cc)
        f6 = f(x2cd, y2dc)
        f7 = f(x2dc, y2cd)
        f8 = f(x2dd, y2dd)
        
        b1 = (
                f1*p1cc*q1cc,
                f1*p1cc*(1 - q1cc),
                f1*(1 - p1cc)*q1cc,
                f1*(1 - p1cc)*(1 - q1cc),
                (1 - f1)*p2cc*q2cc,
                (1 - f1)*p2cc*(1 - q2cc),
                (1 - f1)*(1 - p2cc)*q2cc,
                (1 - f1)*(1 - p2cc)*(1 - q2cc),
            )
        b2 = (
                f2*p1cd*q1dc,
                f2*p1cd*(1 - q1dc),
                f2*(1 - p1cd)*q1dc,
                f2*(1 - p1cd)*(1 - q1dc),
                (1 - f2)*p2cd*q2dc,
                (1 - f2)*p2cd*(1 - q2dc),
                (1 - f2)*(1 - p2cd)*q2dc,
                (1 - f2)*(1 - p2cd)*(1 - q2dc),
            )
        b3 = (
                f3*p1dc*q1cd,
                f3*p1dc*(1 - q1cd),
                f3* (1 - p1dc)*q1cd,
                f3*(1 - p1dc)*(1 - q1cd),
                (1 - f3)*p2dc*q2cd,
                (1 - f3)*p2dc*(1 - q2cd),
                (1 - f3)*(1 - p2dc)* q2cd,
                (1 - f3)*(1 - p2dc)*(1 - q2cd),
            )
        b4 = (
                f4*p1dd*q1dd,
                f4*p1dd*(1 - q1dd),
                f4*(1 - p1dd)*q1dd,
                f4*(1 - p1dd)*(1 - q1dd),
                (1 - f4)*p2dd*q2dd,
                (1 - f4)*p2dd*(1 - q2dd),
                (1 - f4)*(1 - p2dd)*q2dd,
                (1 - f4)*(1 - p2dd)*(1 - q2dd),
            )

        b5 = (
                f5*p1cc*q1cc,
                f5*p1cc*(1 - q1cc),
                f5*(1 - p1cc)*q1cc,
                f5*(1 - p1cc)*(1 - q1cc),
                (1 - f5)*p2cc*q2cc,
                (1 - f5)*p2cc*(1 - q2cc),
                (1 - f5)*(1 - p2cc)*q2cc,
                (1 - f5)*(1 - p2cc)*(1 - q2cc),
            )
        b6 = (
                f6*p1cd*q1dc,
                f6*p1cd*(1 - q1dc),
                f6*(1 - p1cd)*q1dc,
                f6*(1 - p1cd)*(1 - q1dc),
                (1 - f6)*p2cd*q2dc,
                (1 - f6)*p2cd*(1 - q2dc),
                (1 - f6)*(1 - p2cd)*q2dc,
                (1 - f6)*(1 - p2cd)*(1 - q2dc),
            )
        b7 = (
                f7*p1dc*q1cd,
                f7*p1dc*(1 - q1cd),
                f7* (1 - p1dc)*q1cd,
                f7*(1 - p1dc)*(1 - q1cd),
                (1 - f7)*p2dc*q2cd,
                (1 - f7)*p2dc*(1 - q2cd),
                (1 - f7)*(1 - p2dc)* q2cd,
                (1 - f7)*(1 - p2dc)*(1 - q2cd),
            )
        b8 = (
                f8*p1dd*q1dd,
                f8*p1dd*(1 - q1dd),
                f8*(1 - p1dd)*q1dd,
                f8*(1 - p1dd)*(1 - q1dd),
                (1 - f8)*p2dd*q2dd,
                (1 - f8)*p2dd*(1 - q2dd),
                (1 - f8)*(1 - p2dd)*q2dd,
                (1 - f8)*(1 - p2dd)*(1 - q2dd),
            )

        return np.asarray((b1, b2, b3, b4, b5, b6, b7, b8))

        # return np.asarray([
        #     [
        #         f(x1cc, y1cc)*p1cc*q1cc, \
        #         f(x1cc, y1cc)*p1cc*(1 - q1cc), \
        #         f(x1cc, y1cc)*(1 - p1cc)*q1cc, \
        #         f(x1cc, y1cc)*(1 - p1cc)*(1 - q1cc), \
        #         (1 - f(x1cc, y1cc))*p2cc* q2cc, \
        #         (1 - f(x1cc, y1cc))*p2cc* (1 - q2cc), \
        #         (1 - f(x1cc, y1cc))* (1 - p2cc)*q2cc, \
        #         (1 - f(x1cc, y1cc))* (1 - p2cc)* (1 - q2cc) \
        #     ],

        #     [
        #         f(x1cd, y1dc)*p1cd*q1dc, \
        #         f(x1cd, y1dc)*p1cd*(1 - q1dc), \
        #         f(x1cd, y1dc)*(1 - p1cd)*q1dc, \
        #         f(x1cd, y1dc)*(1 - p1cd)*(1 - q1dc), \
        #         (1 - f(x1cd, y1dc))*p2cd*q2dc, \
        #         (1 - f(x1cd, y1dc))*p2cd*(1 - q2dc), \
        #         (1 - f(x1cd, y1dc))*(1 - p2cd)*q2dc, \
        #         (1 - f(x1cd, y1dc))*(1 - p2cd)*(1 - q2dc), \
        #     ],

        #     [
        #         f(x1dc, y1cd)*p1dc*q1cd, \
        #         f(x1dc, y1cd)*p1dc*(1 - q1cd), \
        #         f(x1dc, y1cd)* (1 - p1dc)*q1cd, \
        #         f(x1dc, y1cd)*(1 - p1dc)*(1 - q1cd), \
        #         (1 - f(x1dc, y1cd))*p2dc*q2cd, \
        #         (1 - f(x1dc, y1cd))*p2dc*(1 - q2cd), \
        #         (1 - f(x1dc, y1cd))*(1 - p2dc)* q2cd, \
        #         (1 - f(x1dc, y1cd))*(1 - p2dc)*(1 - q2cd), \
        #     ],

        #     [
        #         f(x1dd, y1dd)*p1dd*q1dd, \
        #         f(x1dd, y1dd)*p1dd*(1 - q1dd), \
        #         f(x1dd, y1dd)*(1 - p1dd)*q1dd, \
        #         f(x1dd, y1dd)*(1 - p1dd)*(1 - q1dd), \
        #         (1 - f(x1dd, y1dd))*p2dd*q2dd, \
        #         (1 - f(x1dd, y1dd))*p2dd*(1 - q2dd), \
        #         (1 - f(x1dd, y1dd))*(1 - p2dd)*q2dd, \
        #         (1 - f(x1dd, y1dd))*(1 - p2dd)*(1 - q2dd), \
        #     ],

        #     [
        #         f(x2cc, y2cc)*p1cc*q1cc, \
        #         f(x2cc, y2cc)*p1cc*(1 - q1cc), \
        #         f(x2cc, y2cc)*(1 - p1cc)*q1cc, \
        #         f(x2cc, y2cc)*(1 - p1cc)*(1 - q1cc), \
        #         (1 - f(x2cc, y2cc))*p2cc* q2cc, \
        #         (1 - f(x2cc, y2cc))*p2cc* (1 - q2cc), \
        #         (1 - f(x2cc, y2cc))* (1 - p2cc)*q2cc, \
        #         (1 - f(x2cc, y2cc))* (1 - p2cc)* (1 - q2cc), \
        #     ],

        #     [
        #         f(x2cd, y2dc)*p1cd*q1dc, \
        #         f(x2cd, y2dc)*p1cd*(1 - q1dc), \
        #         f(x2cd, y2dc)*(1 - p1cd)*q1dc, \
        #         f(x2cd, y2dc)*(1 - p1cd)*(1 - q1dc), \
        #         (1 - f(x2cd, y2dc))*p2cd*q2dc, \
        #         (1 - f(x2cd, y2dc))*p2cd*(1 - q2dc), \
        #         (1 - f(x2cd, y2dc))*(1 - p2cd)*q2dc, \
        #         (1 - f(x2cd, y2dc))*(1 - p2cd)*(1 - q2dc), \
        #     ],

        #     [
        #         f(x2dc, y2cd)*p1dc*q1cd, \
        #         f(x2dc, y2cd)*p1dc*(1 - q1cd), \
        #         f(x2dc, y2cd)* (1 - p1dc)*q1cd, \
        #         f(x2dc, y2cd)*(1 - p1dc)*(1 - q1cd), \
        #         (1 - f(x2dc, y2cd))*p2dc*q2cd, \
        #         (1 - f(x2dc, y2cd))*p2dc*(1 - q2cd), \
        #         (1 - f(x2dc, y2cd))*(1 - p2dc)* q2cd, \
        #         (1 - f(x2dc, y2cd))*(1 - p2dc)*(1 - q2cd), \
        #     ],

        #     [
        #         f(x2dd, y2dd)*p1dd*q1dd, \
        #         f(x2dd, y2dd)*p1dd*(1 - q1dd), \
        #         f(x2dd, y2dd)*(1 - p1dd)*q1dd, \
        #         f(x2dd, y2dd)*(1 - p1dd)*(1 - q1dd), \
        #         (1 - f(x2dd, y2dd))*p2dd*q2dd, \
        #         (1 - f(x2dd, y2dd))*p2dd*(1 - q2dd), \
        #         (1 - f(x2dd, y2dd))*(1 - p2dd)*q2dd, \
        #         (1 - f(x2dd, y2dd))*(1 - p2dd)*(1 - q2dd), \
        #     ]
        # ])
