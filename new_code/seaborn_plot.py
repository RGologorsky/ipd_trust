# import seaborn as sns
# sns.set(style="ticks")
# exercise = sns.load_dataset("exercise")
# g = sns.catplot(x="time", y="pulse", hue="kind", data=exercise)

import matplotlib.pyplot as plt
import seaborn as sns

import pandas as pd

sns.set(style="ticks", palette="pastel")

# Load the example tips dataset
data = pd.read_csv("data/num_timesteps/runs_5_eps_1.00e-03_beta_2.00e+00/date_2019_02_03/data_num_timesteps.csv")


# Draw a nested boxplot to show bills by day and time
ts = "No. Timesteps"
strat = "Strat"

g = sns.boxplot(x=strat, y="1CC rate", 
			hue=ts, data=data)

#handles, labels = ax1.get_legend_handles_labels()

sns.despine(offset=10)
g.set_title('Cooperation Rate Convergence')
g.set_xlabel("Strategy Space")

my_labels = ['1.00e+03', '1.00e+04', '1.00e+05', '2.00e+05', '3.00e+05', '1.00e+06']
#g.legend(handles=handles, loc='upper right', bbox_to_anchor=(1.25, 0.5), ncol=1, labels=my_labels, title="No. Timesteps")
# g._legend(loc='upper right', bbox_to_anchor=(1.25, 0.5), ncol=1)

# g._legend.set_title('No. Timesteps')
# my_labels = ['1.00e+03', '1.00e+04', '1.00e+05', '2.00e+05', '3.00e+05', '1.00e+06']


# #ax.legend(loc='lower right') #, labels = my_labels)

# # Put a legend to the right side
# #ax1.legend(handles=[leg], loc='upper right', bbox_to_anchor=(1.25, 0.5), ncol=1)



# for t, l in zip(g._legend.texts, my_labels):
# 	print("t is ", t, "l is ", l) 
# 	t.set_text(l)

# print("t", g._legend.texts)

plt.tight_layout()
plt.savefig("imgs/1cc_convergence.eps", format='eps', dpi=1000)

plt.show()

