import numpy as np
import scipy.sparse.linalg as sp

def generate_transition_matrix(s1, s2):
        [pcc, pcd, pdc, pdd] = s1
        [qcc, qcd, qdc, qdd] = s2

        return np.asarray([
            [pcc*qcc, pcc*(1-qcc), (1-pcc)*qcc, (1-pcc)*(1-qcc)],
            [pcd*qdc, pcd*(1-qdc), (1-pcd)*qdc, (1-pcd)*(1-qdc)],
            [pdc*qcd, pdc*(1-qcd), (1-pdc)*qcd, (1-pdc)*(1-qcd)],
            [pdd*qdd, pdd*(1-qdd), (1-pdd)*qdd, (1-pdd)*(1-qdd)]
        ]);


def get_stationary_dist(cls, s1, s2):
    Q = generate_transition_matrix(s1, s2)

    #Q is stochastic, guranteed to have left eigenvector v w/ eigenvalue 1
    # v satisfies Q'v = v, i.e. (Q' - I)v = 0.
    #v = null_space(np.transpose(Q)-np.ones(Q.shape))
    l, v = sp.eigs(Q.T, k=1, which='LM')

    v = v/sum(v)
    return v.T

s1 = [0.01, 0.01, 0.01, 0.01]
s2 = [0.01, 0.01, 0.01, 0.01]

Q = generate_transition_matrix(s1, s2)
v = get_stationary_dist("", s1, s2);
c = np.matmul(v, Q);

print("s1 = {:}, s2 = {:}".format(s1, s2))
print(Q)
print("stationary dist: \n {:}".format(v))
print("check")
print("v*Q - v = {:}".format(c - v))
