import numpy as np

def save_signal(S, fname):
    np.savetxt(fname, S)