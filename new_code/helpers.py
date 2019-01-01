
# strategy to string
def strat_to_str(strat):
	return ','.join(["{:.3f}".format(num) for num in strat])

# Plotting Helpers
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

def plot(xs, ys, title, xlabel, ylabel):
    fig = plt.figure(1)
    fig.clf()

    ax1 = plt.subplot(2,2,1);
    ax1.plot(xs, ys); 
    ax1.set_title(title);
    ax1.set_xlabel(xlabel);
    ax1.set_ylabel(ylabel);
    plt.show()
    

# Params Helpers
def get_params(param_names, params_dict):
    return (params_dict[name] for name in param_names)
