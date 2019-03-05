import numpy as np
import time

from class_two_games import S_8_Game, S_12_Game, S_16_Game

import pathlib # create directory as needed

from helper_functions import save_dict, read_dict, get_index, bin_array


# Parameters
c=1.00
b2=1.20

transitions = [
    #"EqualSay_G1_Default",
    #"Random_Dictator",
    #"Player1_Dictator",
    "EqualSay_G2_Default",
    #"EqualSay_G1_Default",
    #"Player1_Dictator",
    #"Random_Dictator",
]

transition = transitions[0]

# 1.0 - 10**(-2) = 0.99 -> exponent = num decimal places
eps = 10**(-3)
S8_game  = S_8_Game(c=c,   b1=1.8, b2=b2, game_transition_dynamics=transition)
S12_game = S_12_Game(c=c,  b1=1.8, b2=b2, game_transition_dynamics=transition)
S16_game = S_16_Game(c=c,  b1=1.8, b2=b2, game_transition_dynamics=transition)

games = [S8_game, S12_game, S16_game]

folder_timestamp = time.strftime("date_%Y_%m_%d_%H_%M_%S")
params_str = "c_{:.2f}_b2_{:.2f}_eps_{:.10f}".format(c, b2, eps)

b1_list = np.arange(1.0, 3.2, 0.14)


def find_all_coop_ess(game, eps):
    num_strats = 2**game.strat_len
    ess_lst = []

    for i in range(num_strats):
        s1 = bin_array(i, game.strat_len)
        s1 = [eps + (1-2*eps)*p for p in s1] # add noise

        # check if cooperates against itself
        v = game.get_stationary_dist(game.get_f(), s1, s1)

        if v[0] > 0.99:
            a = np.dot(v, game.p1_payoffs)

            # check if cannot be invaded by other mutants
            s1_is_ESS_against_all = True

            for j in range(num_strats):
                s2 = bin_array(j, game.strat_len)
                s2 = [eps + (1-2*eps)*p for p in s2] # add noise

                # get q's cooperation rate
                v = game.get_stationary_dist(game.get_f(), s1, s2)
                b = np.dot(v, game.p1_payoffs)
                c = np.dot(v, game.p2_payoffs)

                # payoff q vs. q
                v = game.get_stationary_dist(game.get_f(), s2, s2)
                d = np.dot(v, game.p1_payoffs)

                s1_is_ESS = (a  > c) or (a == c and b > d)

                if not s1_is_ESS:
                    s1_is_ESS_against_all = False
                    break

            if s1_is_ESS_against_all:
                ess_lst.append(s1)
    return ess_lst

#run_dict(b1_list)

def run(b1_list):
    parent_folder = "data/full_coop_ess/transitions/{:s}/{:s}/{:s}/"\
                        .format(transition, params_str, folder_timestamp)

    print("Parent folder: ", parent_folder)

    # print parameters
    print("Parameters: eps = {:.10f}, c={:.2f}, b2 = {:.2f}".format(eps, c, b2))

    for game in games:

        print("game = {:s}".format(str(game)))
    
        folder = parent_folder + "{:s}/".format(str(game))

        # create directory
        pathlib.Path(folder).mkdir(parents=True, exist_ok=True) 

        for b1 in b1_list:

            print("b1 = {:.2f}".format(b1))

            # reset b1 value
            game.reset_b1(b1)

            # time it
            start_time = time.time()
            full_coop_ess_lst = find_all_coop_ess(game, eps)
            elapsed_time = time.time() - start_time

            print("Elapsed Time: {:.2f} min. {:s}, find all coop ESS ({:d})."
                    .format(elapsed_time/60.0, str(game), len(full_coop_ess_lst)))

            # filename = folder + "b1_{:.2f}_num_strat_{:d}.csv".format(b1, len(full_coop_spe_lst))
            filename = folder + "b1_{:.2f}.csv".format(b1)

            with open(filename,'ab') as f:
                np.savetxt(f, full_coop_ess_lst, fmt="%d", delimiter=",")

run(b1_list)