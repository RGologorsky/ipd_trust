# printing

def print_num_s_active(self):
    print "No. S_Active: {:}".format(len(self.s_active))

def print_freq_total(self, msg):
    total = sum(self.s_freqs)
    if total != self.N:
        print msg
        print "Unusual: Total Freq: {:}".format(sum(self.s_freqs))

def print_status(self):
    print "#### STATUS ####"

    self.print_num_s_active()
    print "s_active", self.s_active

    print "s_freqs", self.s_freqs

    print "s_payoffs"
    print self.s_payoffs

    print "s_cc_rates"
    print self.s_cc_rates

    print "#### END STATUS ####"
