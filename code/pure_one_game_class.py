class Pure_One_Game:

    # Calculating Game Transitions, specific payoffs between strategies.

    # 8 states, ranging from 0 to 7, corresponding to 1CC to 2DD.
    # Strategies in [0,1]^16

    max_num_strategies = 2**4

    states = {
        (1,1): 0, # 1CC
        (1,0): 1, # 1CD
        (0,1): 2, # 1DC
        (0,0): 3, # 1DD
    }

    def __init__(self, b1, b2, c):
        self.b1 = b1; # benefit coop in Game 1
        self.b2 = b2; # benefit coop in Game 2
        self.c  = c;   # cost to coop in both games

         #player1, player2 payoffs for outcomes 1CC, ..., 1DD, 2CC, ..., 2DD
        self.p1_payoffs = [b1-c, -c, b1, 0, b2-c, -c, b2, 0];
        self.p2_payoffs = [b1-c, b1, -c, 0, b2-c, b2, -c, 0];



    def to_strategy(num):
        return [int(x) for x in format(num, '04b')]

    def strat_to_str(num):
        arr = Pure_One_Game.to_strategy(num)
        return str(arr)

    def mc_estimate(self, s1, s2, n = 20, initial_state = 0):
        '''
            Return avg payoffs when s1 plays s2 and CC rate
        '''
        s1_total_payoff = 0.0
        s2_total_payoff = 0.0

        cc_rate     = 0.0

        prev_state = initial_state

        s1 = Pure_One_Game.to_strategy(s1)
        s2 = Pure_One_Game.to_strategy(s2)

        for i in range(n):
            s1_move = s1[prev_state]
            s2_move = s2[prev_state]
            
            curr_state = Pure_One_Game.states[(s1_move, s2_move)]

            s1_total_payoff += self.p1_payoffs[curr_state]
            s2_total_payoff += self.p2_payoffs[curr_state]

            # mutual cooperation = 1CC or 2CC
            if curr_state % 4 == 0:
                cc_rate += 1


        # return s1 avg payoff, s2 avg payoff, avg CC ratex
        return (s1_total_payoff/n, s2_total_payoff/n, cc_rate/n, 1)


    def q_estimate(self, s1, s2, initial_state = 0):
        pass
