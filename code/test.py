from class_one_game import One_Game
from class_s_12_game import S_12_Game
from class_s_16_game import S_16_Game

from class_sim import Sim

from test_c_vs_b1 import test_c_vs_b1
from static_helpers import plot

# game = Pure_16_Game(c=1.0, b1=1.9, b2=1.2)
T = 10**7

game = S_12_Game(c=1.0, b1=1.9,b2=1.0, eps=0.01)
sim  = Sim(T=T, game = game, do_plots = False)
sim.init_strategy_population(s_initial = 0)


b1_list, c_list = test_c_vs_b1(sim, T=T, b1_start=1, b1_end=3, num_test_pts=12)

plot(b1_list, c_list, title = "Prob[C] v. b1 value", xlabel = "b1 value", \
                                                     ylabel = "Prob[C]")

print("b1_list: ", b1_list)
print("c_list: ", c_list)
