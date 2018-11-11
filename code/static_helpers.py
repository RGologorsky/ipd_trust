import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import numpy as np

# Probability

def sigmoid(x):
    return 1.0/(1.0 + np.exp(x))

def get_imitation_prob(beta, pi_r, pi_l):
    return sigmoid(-1.0 * beta * (pi_r - pi_l));

# returns index, chosen with weighted probability from a list
def choose_one_from_list(wts, random_weight):
    for index, wt in enumerate(wts):
        random_weight -= wt;
        if random_weight <= 0:
            return index

    print("Error! choose one from list failed")
    raise(Exception)
    
# Matrix Ops/Static Methods

import numpy as np

def safe_get_index(elt, lst):
    try:
        return lst.index(elt)
    except ValueError:
        return -1

def add_row(vec, matrix):
    try:
        return np.r_[matrix,[vec]]
    except Exception as e:
        print("Adding row error. Row {:}.\n Matrix:\n {:} ".format(vec, matrix))
        raise(e)

def add_col(vec, matrix):
    try:
        return np.c_[matrix, vec]
    except Exception as e:
        print("Adding col error. Col {:}.\n Matrix:\n {:} ".format(vec, matrix))
        raise(e)

def del_row(index, matrix):
    return np.r_[matrix[:index,], matrix[index+1:,]]

def del_col(index, matrix):
    return np.c_[matrix[:,:index], matrix[:,index+1:]]

# Plotting 

def plot(xs, ys, title, xlabel, ylabel):
    fig = plt.figure(1)
    fig.clf()

    ax1 = plt.subplot(2,2,1);
    ax1.plot(xs, ys); 
    ax1.set_title(title);
    ax1.set_xlabel(xlabel);
    ax1.set_ylabel(ylabel);
    plt.show()

