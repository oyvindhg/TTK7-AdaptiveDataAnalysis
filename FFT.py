import numpy as np
import matplotlib.pyplot as plt

#Fast Fourier Transform
def FFT(S, Fs):

    T = 1 / float(Fs)
    L = len(S)

    fft = np.fft.fft(S)

    freq = np.fft.fftfreq(L, T)

    plt.grid()
    plt.xlabel("Hz")

    plt.plot(freq[0:round(L/2)], 2*np.absolute(fft/L)[0:round(L/2)])

    #plt.show()