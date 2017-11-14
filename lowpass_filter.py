import numpy as np
from scipy.signal import butter, lfilter, freqz
import matplotlib.pyplot as plt


def butter_lowpass(cutoff, Fs, order=5):
    nyq = 0.5 * Fs
    normal_cutoff = cutoff / nyq
    b, a = butter(order, normal_cutoff, btype='low', analog=False)
    return b, a

def butter_lowpass_filter(data, cutoff, Fs, order=5, plot=False):
    b, a = butter_lowpass(cutoff, Fs, order=order)
    y = lfilter(b, a, data)

    if plot:
        # Plot the frequency response.
        w, h = freqz(b, a, worN=8000)
        f = Fs * w / (2 * np.pi)
        plt.subplot(2, 1, 1)
        plt.plot(f, np.abs(h), 'b')
        plt.plot(cutoff, 0.5 * np.sqrt(2), 'ko')
        plt.axvline(cutoff, color='k')
        plt.xlim(0, 0.5 * Fs)
        plt.title("Lowpass Filter Frequency Response")
        plt.xlabel('Frequency [Hz]')

        plt.subplot(2, 1, 2)
        plt.plot(y, 'b')
        plt.grid()
        plt.show()

    return y

