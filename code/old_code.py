# choose random pair (no replacement) of strategy indices
def old_choose_strategy_pair(self):

    # check if only one strategy in the population
    if len(self.s_active) == 1:
        return -1

    # choose first strategy
    rand1 = self.get_random_float()
    s1_index = choose_one_from_list(self.s_freqs, self.N * rand1)

    # choose another strategy without replacement
    freqs_no_replacement = self.s_freqs[:]
    freqs_no_replacement[s1_index] = 0

    rand2 =  self.get_random_float()
    s2_index = choose_one_from_list(freqs_no_replacement, \
                                    (self.N - self.s_freqs[s1_index]) * rand2)

    # choose which strategy is learner/role model
    return (s1_index, s2_index) if rand1 < rand2 else (s2_index, s1_index)


# choose random pair (no replacement) of strategy indices
def slow_choose_strategy_pair(self):

    # only one strategy in the population
    if len(self.s_active) == 1:
        return -1

    s_weights = [s_freq/float(self.N) for s_freq in self.s_freqs]
    return np.random.choice(len(self.s_active),size=2,replace=False, p=s_weights)
