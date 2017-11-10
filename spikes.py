import numpy as np
import matplotlib.pyplot as plt

def find_spikes(S):
    pos_thresh = np.zeros(S.size)
    neg_thresh = np.zeros(S.size)
    thresh = np.std(S) * 5
    #thresh = 68800000

    for i in range(0, S.size):
        pos_thresh[i] = thresh
        neg_thresh[i] = -thresh

    plt.plot(S)
    plt.plot(pos_thresh)
    plt.plot(neg_thresh)
    plt.show()