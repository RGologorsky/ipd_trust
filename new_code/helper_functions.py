import numpy as np
import json

def numpy_isclose(a, b, rtol=1.e-5, atol=1.e-8):
    """ A equivalent to numpy's isclose method for individual floating-point values
    
    This is considerably faster than numpy's version over 1D arrays
    """
    return abs(a - b) <= (atol + rtol * abs(b))


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

    string_description =  "sample mean = {:.4f}\nsample sd   = {:.4f}".format(mean, sample_sd)

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

def add_line_plot(ax, xs, ys, xlabel, ylabel, title, text="", point_size=10):
    ax.plot(xs, ys, marker='o', color='b')
    ax.set_title(title)
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel) 

    add_titlebox(ax, text)

def add_scatter_plot(ax, xs, ys, xlabel, ylabel, title, text="", point_size=10):
    ax.scatter(xs, ys, s = point_size)
    ax.set_title(title)
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)

    add_titlebox(ax, text)

# Misc. helpers
def get_params(param_names, params_dict):
    return (params_dict[name] for name in param_names)

# returns -1 if elt not in lst
def get_index(elt, lst):
    try:
        return lst.index(elt)
    except ValueError:
        return -1


def bin_array(num, m):
    """Convert a positive integer num into an m-bit bit vector"""
    return np.array(list(np.binary_repr(num).zfill(m))).astype(np.int8)

str_to_state_dict = {
    "1CC": 0,
    "1CD": 1,
    "1DC": 2,
    "1DD": 3,
    "2CC": 4,
    "2CD": 5,
    "2DC": 6,
    "2DD": 7,
    # "CC": 0,
    # "CD": 1,
    # "DC": 2,
    # "DD": 3
}

state_to_str_dict = {val: key for key,val in str_to_state_dict.items()}

# lst of "1CC", "1DC" to corresponding state identifiers
def str_list_to_states(lst):
    return [str_to_state_dict[string] for string in lst]

def states_to_str_lst(lst):
    return [state_to_str_dict[state] for state in lst]

# def get_sampled_timesteps(num_timesteps, data_collection_freq):
#     return np.arange(num_timesteps, step=)


def save_dict(dictionary, filename):
    with open(filename + ".json", 'w') as f:
        json.dump(dictionary, f)

def read_dict(filename):
    with open(filename + ".json") as f:
        return json.load(f)