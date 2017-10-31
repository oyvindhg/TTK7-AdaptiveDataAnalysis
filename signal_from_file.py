import numpy as np

def get_signal(fname):

    Fs = 10000

    with open(fname, 'r') as ins:
        S = ins.read().split('\n')
    for i, elem in enumerate(S):
        S[i] = float(S[i])

    S = np.array(S)

    return S, Fs