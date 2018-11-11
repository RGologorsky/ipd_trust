# printing

import numpy as np

def print_num_s_active(self):
    print("No. S_Active: {:}".format(len(self.s_active)))

def print_freq_total(self, msg):
    total = sum(self.s_freqs)
    if total != self.N:
        print(msg)
        print("Unusual: Total Freq: {:}".format(sum(self.s_freqs)))

def print_status(self, timestep):
    if self.round_result == (-1, -1):
        return

    print("#### Round {:} STATUS ####".format(timestep))

    self.print_num_s_active()
    print("s_active", self.s_active)

    print("s_freqs", self.s_freqs)

    print("s_payoffs")
    print(self.s_payoffs)

    print("s_cc_rates")
    print(self.s_cc_rates)

    print("#### END STATUS ####")

def print_results(self, print_most_abundant=False):
    print("b1 = {:}. T = 10^({:}). Overall Avg. CC rate: {:.4f}. Elapsed time: {:.2f} sec"\
            .format(self.game.b1, int(np.log10(self.T)), self.final_avg_cc_rate, self.elapsed_time))

    # most abundant
    if print_most_abundant:
        ind = np.argpartition(self.s_counts, -4)[-4:]
        ind = ind[np.argsort(-1 * self.s_counts[ind])]
        print("most abundant strategies: strat = {:} s_counts {:}".format(ind, self.s_counts[ind]))
        print("abundance ALL-D: {:}".format(self.s_counts[0]))
