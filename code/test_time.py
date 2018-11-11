from class_one_game import One_Game
from classs_12_game import S_12_Game
from classs_16_game import S_16_Game

from class_sim import Sim

# game = Pure_16_Game(c=1.0, b1=1.9, b2=1.2)
game = One_Game(c=1.0, b1=1.9)
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
