# CC vs. b
import numpy as np

def test_c_vs_b1(sim, T=10**6, b1_start=1, b1_end=3, num_test_pts=12):

    b1_list = np.linspace(b1_start, b1_end, num_test_pts)
    cc_list = np.zeros(num_test_pts)



    for index, b1 in enumerate(b1_list):

        sim.game.reset_b1(b1=b1)
        
        cc_list[index] = sim.simulate_timesteps()
        sim.reset_simulation()

    print("b1_list ", b1_list)
    print("cc_list", cc_list)

    return (b1_list, cc_list)
