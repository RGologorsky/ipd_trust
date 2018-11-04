import numpy as np

from sim_class import Sim

from pure_12_game_class import Pure_12_Game
from pure_16_game_class import Pure_16_Game
from pure_one_game_class import Pure_One_Game

from test_cc_vs_b import test_cc_vs_b
from plotting import plot

# game = Pure_16_Game(c=1.0, b1=1.9, b2=1.2)
game = Pure_One_Game(c=1.0, b1=1.9)
new_simulation = Sim(T=10**5, game = game, do_plots = False)
new_simulation.init_strategy_population(s_initial = 0)

# new_simulation.simulate_timesteps()

from line_profiler import LineProfiler

from simulation import simulate_timesteps
from helpers import record_timestep_data

lp = LineProfiler()
lp.add_function(record_timestep_data)
lp_wrapper = lp(simulate_timesteps)
lp_wrapper(new_simulation)
lp.print_stats()
