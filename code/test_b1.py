import numpy as np

from class_one_game import One_Game
from classs_s_12_game import S_12_Game
from classs_s_16_game import S_16_Game

from class_sim import Sim

from static_helpers import plot

# game = Pure_16_Game(c=1.0, b1=1.9, b2=1.2)
T = 10**5
num_test_pts = 0

# game = S_12_Game(c=1.0, b1=1.9, b2 = 1.0, eps=0.01)
game = One_Game(c=1.0, b1=2.5, eps=0.01)

sim  = Sim(T=T, game = game, do_plots = False)
sim.init_strategy_population(s_initial = 0)

sim.simulate_timesteps()
plot(np.arange(sim.T), sim.avg_cc_data, \
       title = "Prob[C] over Time", xlabel = "Timestep", ylabel = "Prob[C]")

c_list = np.zeros(num_test_pts)

for i in range(num_test_pts):
    c_list[i] = sim.simulate_timesteps()
    sim.reset_simulation()

print("Stats: mean = {:.4f}, std = {:.4f}".format(np.mean(c_list), np.std(c_list)))
print("c_list: ", c_list)
