from FFT import FFT
from STFT import STFT
from WignerVille import WignerVille
from CWT import CWT
from HHT import HHT
from signal_from_file import get_signal
from signal_generated import generate_signal
from signal_to_file import save_signal
import numpy as np
import matplotlib.pyplot as plt
from spikes import find_spikes
from lowpass_filter import butter_lowpass_filter
from PyEMD.PyEMD import EEMD

from pytftb.tftb.generators import noisecu




S, Fs = get_signal('sig_4.txt')
noise = np.zeros(S.size)

S_new2 = butter_lowpass_filter(S,200,Fs,order=6,plot=True)


#
# noise_std = np.std(S)
# print(noise_std)

#S, noise, Fs = generate_signal()

#FFT(S, Fs)
#
# S, Fs = get_signal('sig_2.txt')
# FFT(S, Fs)
#
# S, Fs = get_signal('sig_3.txt')
# FFT(S, Fs)
#
# S, Fs = get_signal('sig_4.txt')
# FFT(S, Fs)


#find_spikes(S)


T = 1/float(Fs)
t = np.arange(S.size)*T
#STFT(S)
#CWT(S)

#f_modeex = [1000]
#A_modeex = [0.5]
#index_modeex = [0]


imfs = HHT(S, t, plot=False) #f_modeex, A_modeex, index_modeex)

n_imfs = len(imfs)

S_new = S - imfs[0] - imfs[1] - imfs[2] - imfs[3] - imfs[4] - imfs[n_imfs - 1] - imfs[n_imfs - 2]

L = len(S)
plt.subplot(2, 1, 1)
FFT(S_new, Fs)
plt.xlim(0, 400)
plt.ylim(0, 400000)
plt.subplot(2, 1, 2)
FFT(S_new2, Fs)
plt.xlim(0, 400)
plt.ylim(0, 400000)
plt.show()

imfs = HHT(S_new, t, plot=True)

# for i in range(0, len(imfs)):
#     FFT(imfs[i], Fs)
#     plt.xlim(0, 400)
#     plt.show()

from scipy.signal import decimate

S_ds = S_new
for i in range(0,2):
    S_ds = decimate(S_ds,5, ftype='fir')


plt.subplot(2, 1, 1)
plt.plot(S_ds)
plt.subplot(2,1,2)
plt.plot(S_new)
plt.show()


plt.subplot(2, 1, 1)
FFT(S_new, Fs)
plt.xlim(0, 200)
plt.ylim(0, 400000)
plt.subplot(2, 1, 2)
FFT(S_ds, 400)
plt.xlim(0, 200)
plt.ylim(0, 400000)
plt.show()

Fs = 400
S = S_ds
T = 1/float(Fs)
T = np.arange(S.size)*T


eemd = EEMD()
eIMFs = eemd.eemd(S)

imfNo  = eIMFs.shape[0]

# Plot results in a grid
c = np.floor(np.sqrt(imfNo+1))
r = np.ceil( (imfNo+1)/c)


plt.ioff()
plt.subplot(r,c,1)
plt.plot(T, S, 'r')
#plt.xlim((tMin, tMax))
plt.title("Original signal")

for num in range(imfNo):
    plt.subplot(r,c,num+2)
    plt.plot(T, eIMFs[num],'g')
    #plt.xlim((tMin, tMax))
    plt.title("Imf "+str(num+1))

plt.show()





#save_signal(S_filtered, 'ID0_lastexp_lastsecond_filtered.txt')