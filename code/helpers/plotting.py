import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import numpy as np

def plot_timestep_data(self):
    if not self.do_plots:
        return

    print("plotting")

    time_vec = range(self.T)
   
    fig = plt.figure(1);
    fig.clf();
    
    ax1 = plt.subplot(2,2,1);
    ax1.plot(time_vec, self.avg_cc_data); 
    ax1.set_title('Evolution of Cooperation over Time');
    ax1.set_xlabel('Timestep');
    ax1.set_ylabel('Avg. Prob[C]');


    @ticker.FuncFormatter
    def major_formatter(x, pos):
        return 0 if x == 0 else "10^({%d})" % int(np.log10(x))

    ax1.xaxis.set_major_formatter(ticker.FormatStrFormatter('%.2e'))
    plt.show()

    # plt.subplot(2,2,2); 
    
    # plt.plot(time_vec, self.avg_payoff_data);
    # title('Evolution of Overall Avg. Payoff');
    # xlabel('Timestep');
    # ylabel('Avg. Payoff');
    
    # subplot(2,2,3); 
    # plot(time_vec, avg_game1_data);  
    # title('Evolution of Avg. Game1 Frequency');
    # xlabel('Timestep');
    # ylabel('Avg. Fraction of Time in Game1');
    
    # params_desc = """Parameters: \n 
    #                     b1 = #1.2f, \n 
    #                     beta = #.2f,\n 
    #                     T = 10^{#d}, \n 
    #                     eps = #.2f, \n m
    #                     u = #.2f""".format(b1, beta, log10(T), eps, mu);
    
    # values_desc = """Mean Values: \n 
    #                     payoff = #.3f, \n 
    #                     coop = #.3f, \n 
    #                     game1 = #.3f \n 
    #                     Elapsed Time = #d min"""\
    #             .format(final_avg_payoff, final_avg_coop, \
    #                     final_avg_game1, round(elapsed_time/60, 0));
    
    # strategies_desc = sprintf('Most Abundant Strategies/Freq: \n #d/#.3f \n #d/#.3f \n #d/#.3f', ...
    #     top_3_strategies(1), top_3_abundances(1), ...
    #     top_3_strategies(2), top_3_abundances(2), ...
    #     top_3_strategies(3), top_3_abundances(3));

    # annotation('textbox', [0.49 0.01 0.16 0.48], 'String', ...
    #     {params_desc}, ...
    #     'FontSize',14,...
    #     'Color',[0.84 0.16 0]);
    
    # annotation('textbox', [0.65 0.01 0.18 0.48], 'String', ...
    #     {values_desc}, ...
    #     'FontSize',14,...
    #     'Color',[0.84 0.16 0]);
    
    # annotation('textbox', [0.83 0.01 0.15 0.48], 'String', ...
    #     {strategies_desc}, ...
    #     'FontSize',14,...
    #     'Color',[0.84 0.16 0]);
