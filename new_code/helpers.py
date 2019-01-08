import numpy as np


# generate binary 0/1 pure strategies, rescale to eps/1-eps
def generate_pure_strategy_mutants(num_mutants, strat_len, eps):
    rand_nums = np.random.randint(2, size = num_mutants * strat_len)
    return [num * (1-2*eps) + eps for num in rand_nums]

# generate Unif(0,1) stochastic strategies, rescale to Unif(eps, 1-eps)
def generate_stochastic_strategy_mutants(num_mutants, strat_len, eps):
    rand_nums = np.random.uniform(low=eps, high=1.0-eps, size = num_mutants * strat_len)
    return [num * (1-2*eps) + eps for num in rand_nums]


# returns sample mean and sample standard deviation
def get_sample_statistics(sample):
    mean      = np.mean(sample)
    sample_sd = np.std(sample, ddof=1)

    string_description =  "sample mean = {:.4f}\nsample sd = {:.4f}".format(mean, sample_sd)

    return mean, sample_sd, string_description

# Debugging helpers
def strat_to_str(strat):
    return ','.join(["{:.3f}".format(num) for num in strat])

def print_matrix(title, matrix):
    print(title)
    print('\n'.join(['\t'.join(["{:.3f}".format(cell) for cell in row]) for row in matrix]))


def print_list(title, lst):
    print(title)
    print('\t'.join(["{:.3f}".format(num) for num in lst]))


def is_close(a, b, precision=10**-8):
    return abs(a-b) < precision

# Plotting Helpers
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

def add_titlebox(ax, text):
    ax.text(.55, .8, text,
        horizontalalignment='center',
        transform=ax.transAxes,
        bbox=dict(facecolor='white', alpha=0.6))
        #,fontsize=12.5)
    return ax

def plot_line(xs, ys, xlabel, ylabel, title, titlebox="", point_size=10):
    fig, ax = plt.subplots()
    ax.plot(xs, ys, marker='o', color='b')
    ax.set_title(title)
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)

    add_titlebox(ax, titlebox)
    plt.show()
    

def plot_scatter(xs, ys, xlabel, ylabel, title, titlebox="", point_size=10):
    fig, ax = plt.subplots()
    ax.scatter(xs, ys, s = point_size)
    ax.set_title(title)
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)

    add_titlebox(ax, titlebox)
    plt.show()


# Misc. helpers
def get_params(param_names, params_dict):
    return (params_dict[name] for name in param_names)

# def get_sampled_timesteps(num_timesteps, data_collection_freq):
#     return np.arange(num_timesteps, step=)