from class_reactive import Reactive_Game
from class_one import One_Game
from class_s_12 import S_12_Game
from class_s_16 import S_16_Game


from helpers import plot
from simulation import get_invasion_distr

import numpy as np
import matplotlib.pyplot as plt

import time
# choose game
game = Reactive_Game(c=1.0, b1=10)
num_repeats = 500

# Parameters
params_dict = {
	"game": game,
	"N": 100,
	"eps": 0.005,
	"beta": 0.1,
	"host": game.ALLD,
	"max_attempts": 10**4,
}

start_time = time.time()
strategies, num_invasion_attempts = get_invasion_distr(num_repeats, params_dict)
elapsed_time = time.time() - start_time

print("Elapsed Time: {:.2f} min".format(elapsed_time/60.0))

mean, sample_sd = np.mean(num_invasion_attempts), np.std(num_invasion_attempts, ddof=1)
print("Num. Invasion Attempts Distribution: mean = {:.2f}, sample sd = {:2f}".format(mean, sample_sd))

# print("Strategies: ", strategies)
print("Num Invasion Attempts: ", num_invasion_attempts)

# Plot
long_invasion = list(
					strategy 
					for index, strategy in enumerate(strategies) \
					if num_invasion_attempts[index] >= mean + 1.0 * sample_sd
				)

short_invasion = list(
					strategy 
					for index, strategy in enumerate(strategies) \
					if num_invasion_attempts[index] <= mean - 1.0 * sample_sd
				)

normal_invasion = list(
					strategy 
					for index, strategy in enumerate(strategies) \
					if ((num_invasion_attempts[index] > mean - 1.0 * sample_sd) and 
						(num_invasion_attempts[index] < mean + 1.0 * sample_sd))

				)

fig, ax = plt.subplots()

for lst, color in [(long_invasion, "red"), (short_invasion, "lawngreen"), (normal_invasion, "black")]:
	if len(lst) > 0:
		ps, qs     = zip(*lst)
		ax.scatter(ps, qs, s = 10, color=color)

# label each point w/num. invasions
do_label = False
if do_label:
	for i, strategy in enumerate(strategies):
		num_attempts = num_invasion_attempts[i]
		ax.annotate(str(num_attempts), strategy)


ax.set_title('Successful ALL-D Invader Strategies')
ax.set_xlabel('p')
ax.set_ylabel('q')
plt.show()