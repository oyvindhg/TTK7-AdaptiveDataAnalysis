from pyhht.emd import EMD
from pyhht.visualization import plot_imfs
import matplotlib.pyplot as plt
from scipy.signal import hilbert
from scipy import angle, unwrap
import numpy as np

def add_signal_modeex(S, t, f, A):
    S_ex = A*np.sin(2 * np.pi * f * t)
    S = S + S_ex
    return S

def remove_signal_modeex(S, t, f, A):
    S_ex = A*np.sin(2 * np.pi * f * t)
    S = S - S_ex
    return S

# Hilbert-Huang Transform
def HHT(S, t, noise, f_modeex, A_modeex, index):

    #S = add_signal_modeex(S, t, f_modeex[0], A_modeex[0])

    decomposer = EMD(S)

    imfs = decomposer.decompose()

    #S = remove_signal_modeex(S, t, f_modeex[0], A_modeex[0])
    #imfs[index[0]] = remove_signal_modeex(imfs[index[0]], t, f_modeex[0], A_modeex[0])

    plot_imfs(S, imfs, t)

    # S_filtered = S - imfs[0][:] - imfs[1][:] - imfs[2][:] - imfs[3][:]

    # if np.all(noise == 0):
    #     plt.subplot(2, 1, 1)
    #     plt.ylabel("Original")
    #     plt.plot(S)
    #
    #     plt.subplot(2, 1, 2)
    #     plt.ylabel("Filtered by removing IMFs")
    #     plt.plot(S_filtered)
    #     plt.show()
    # else:
    #     plt.subplot(3, 1, 1)
    #     plt.ylabel("Original")
    #     plt.plot(S)
    #
    #     plt.subplot(3, 1, 2)
    #     plt.ylabel("Original without noise")
    #     plt.plot(S - noise)
    #
    #     plt.subplot(3, 1, 3)
    #     plt.ylabel("Filtered by removing IMFs")
    #     plt.plot(S_filtered)
    #     plt.show()



    # hs1 = hilbert(imfs[0])
    # hs2 = hilbert(imfs[1][:])
    # hs3 = hilbert(imfs[2][:])
    # hs4 = hilbert(imfs[3][:])
    # hs5 = hilbert(imfs[4][:])
    # plt.plot(np.real(hs1), np.imag(hs1), 'b')
    # plt.plot(np.real(hs2), np.imag(hs2), 'g')
    # plt.plot(np.real(hs3), np.imag(hs3), 'r')
    # plt.plot(np.real(hs4), np.imag(hs4), 'y')
    # plt.plot(np.real(hs5), np.imag(hs5), 'k')
    #
    # plt.show()
    #
    # omega_s1 = unwrap(angle(hs1))  # unwrapped instantaneous phase
    # omega_s2 = unwrap(angle(hs2))
    # omega_s3 = unwrap(angle(hs3))
    # omega_s4 = unwrap(angle(hs4))
    # omega_s5 = unwrap(angle(hs5))
    # f_inst_s1 = np.diff(omega_s1)  # instantaneous frequency
    # f_inst_s2 = np.diff(omega_s2)
    # f_inst_s3 = np.diff(omega_s3)
    # f_inst_s4 = np.diff(omega_s4)
    # f_inst_s5 = np.diff(omega_s5)
    # plt.plot(t[1:], f_inst_s1, "b")
    # plt.plot(t[1:], f_inst_s2, "g")
    # plt.plot(t[1:], f_inst_s3, "r")
    # plt.plot(t[1:], f_inst_s4, "y")
    # plt.plot(t[1:], f_inst_s5, "k")
    # plt.show()

    return imfs