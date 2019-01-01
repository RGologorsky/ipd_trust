
from line_profiler import LineProfiler

from simulation import simulate_timesteps
from helpers import record_timestep_data

lp = LineProfiler()
lp.add_function(record_timestep_data)
lp_wrapper = lp(simulate_timesteps)
lp_wrapper(new_simulation)
lp.print_stats()
