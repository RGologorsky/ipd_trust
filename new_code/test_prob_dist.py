from class_s_02 import S_2_Game
from class_s_04 import S_4_Game
from class_s_12 import S_12_Game
from class_s_16 import S_16_Game


from helpers import *
from simulation import get_invasion_distr
from distr import *

import numpy as np
import matplotlib.pyplot as plt

import time

# choose game
game = S_2_Game(c=1.0, b1=10)
ALLD = (0.005 for _ in range(game.strat_len))
num_trials = 10**2

# Parameters
params_dict = {
	"game": game,
	"N": 100,
	"eps": 0.005,
	"beta": 10,
	"host": ALLD,
	"strategy_type": "pure", # could be "stochastic"
	"max_attempts": 10**4,
}

start_time = time.time()
distr = get_invasion_prob_distr(num_trials, params_dict)
mean, sample_sd = np.mean(distr), np.std(distr, ddof=1)
elapsed_time = time.time() - start_time

print("Elapsed Time: {:.2f} min".format(elapsed_time/60.0))
print("Distribution: mean = {:.2f}, sample sd = {:2f}".format(mean, sample_sd))

# Plot

fig, ax = plt.subplots()

# the histogram of the data
n, bins, patches = ax.hist(distr)

#ax.plot(bins, y, '--')
ax.set_xlabel('Invader Fixation Probability')
ax.set_ylabel('Probability density')
ax.set_title(r'Prob[Invader Fixation]: $\mu={:.4f}$, $\sigma={:.4f}$'.format(mean, sample_sd))

# Tweak spacing to prevent clipping of ylabel
fig.tight_layout()
plt.show()