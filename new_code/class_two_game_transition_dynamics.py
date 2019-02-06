# Which game is next? 
# f inputs each player's Prob[prefer Game 1] and 
# f outputs Prob[next is Game 1]
class EqualSay_G2_Default:
    @staticmethod
    def f(a,b): 
        return a * b

class EqualSay_G1_Default:
    @staticmethod
    def f(a,b): 
        return 1 - (a * b)

class OneSidedDictator:
    @staticmethod
    def f(a,b): 
        return a

class Random:
    @staticmethod
    def f(a,b, coin_flip):
        if coin_flip:
            return a
        return b 