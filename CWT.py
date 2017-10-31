from scipy.signal import cwt, ricker
import numpy as np
import matplotlib.pyplot as plt

# Continous Wavelet Transform
def CWT(S, max_wlwidth = 70):
    widths = np.arange(1, max_wlwidth)
    cwtmatr = cwt(S, ricker, widths) # ricker is mexican hat wavelet
    plt.xlabel("Time [s]")
    plt.ylabel("Width of Wavelet")
    plt.imshow(cwtmatr, aspect='auto', cmap='Blues')

    plt.show()