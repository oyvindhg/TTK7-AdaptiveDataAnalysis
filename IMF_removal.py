import numpy as np
from scipy import signal

def EMD_PSD_filter(imfs, lower_frequency_treshold, upper_frequency_treshold, energy_treshold, Fs):
    # return indices of imfs that shall be subtracted.
    imfs_to_subtract = []

    # imf shall be subtracted if less than energy_treshold % of its total energy
    # lies within a specified frequency band

    number_of_imfs = len(imfs)

    # define frequency regions of a signal
    # A: f element [0, lower_frequency_treshold]
    # B: f element <lower_frequency_treshold, upper_frequency_treshold]
    # C: f element <upper_frequeny treshold, infinity>

    # subract imf from signal if less than 80 percent of total energy of
    # that imf is inside B
    for i in range(0, number_of_imfs):
        # calculate PSD
        f_fft_scipy, Sxx_fft_scipy = signal.periodogram(imfs[i], fs=Fs, scaling="density")

        A_f_end = np.where(f_fft_scipy <= lower_frequency_treshold)[0][-1]
        C_f_start = np.where(f_fft_scipy > upper_frequency_treshold)[0][0]

        # calculate energies using the PSD
        total_energy = np.sum(Sxx_fft_scipy * Fs)
        A_energy = np.sum(Sxx_fft_scipy[0:A_f_end] * Fs)
        B_energy = np.sum(Sxx_fft_scipy[A_f_end:C_f_start] * Fs)
        C_energy = np.sum(Sxx_fft_scipy[C_f_start:] * Fs)

        B_energy_percentage = 100 * B_energy / total_energy

        print("imf %i total energy in range <%i, %i]: %f" % (
        i + 1, lower_frequency_treshold, upper_frequency_treshold, B_energy_percentage))

        if B_energy_percentage < energy_treshold:
            # subtract the imf
            print("    should subract imf " + str(i + 1) + " because f element <%i,%i] total energy is %f percent \
            of total imf energy" % (lower_frequency_treshold, upper_frequency_treshold, B_energy_percentage))
            imfs_to_subtract += [i]

    return imfs_to_subtract