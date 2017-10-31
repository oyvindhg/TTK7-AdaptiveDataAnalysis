from scipy.signal import hamming
import numpy as np
import matplotlib.pyplot as plt
from pytftb.tftb.processing.linear import ShortTimeFourierTransform

# Short-Time Fourier Transform
def STFT(S):

    Nx = len(S)
    nsc = int(np.round(Nx/4))
    # nov = int(np.floor(nsc / 2))
    window = hamming(nsc)

    stft = ShortTimeFourierTransform(S, fwindow=window)
    stft.run()
    stft.plot(show_tf=True, cmap='Blues')