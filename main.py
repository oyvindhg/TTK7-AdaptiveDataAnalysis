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
from IMF_removal import EMD_PSD_filter

from pytftb.tftb.generators import noisecu




S, Fs = get_signal('sig_4.txt')
noise = np.zeros(S.size)

plt.plot(S)
plt.ylabel("\u03bcV")
plt.xlabel('t')
plt.title('Original signal')
plt.show()

FFT(S, Fs)
plt.ylabel("\u03bcV")
plt.title('FFT of signal')
plt.show()

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


dt = 1/float(Fs)
t = np.arange(S.size)*dt
#STFT(S)
#CWT(S)

#f_modeex = [1000]
#A_modeex = [0.5]
#index_modeex = [0]


imfs = HHT(S, t, plot=False) #f_modeex, A_modeex, index_modeex)


imfs_remove = EMD_PSD_filter(imfs, 4, 200, 80, Fs)

print(imfs_remove)

S_new = S
for i in imfs_remove:
    S_new = S_new - imfs[i]

L = len(S)
plt.subplot(2, 1, 1)
FFT(S_new, Fs)
plt.xlim(0, 400)
plt.ylim(0, 400000)
plt.ylabel("\u03bcV")
plt.title('FFT of signal after removing IMFs')
plt.subplot(2, 1, 2)
FFT(S_new2, Fs)
plt.xlim(0, 400)
plt.ylim(0, 400000)
plt.ylabel("\u03bcV")
plt.title('FFT of signal after Butterworth low-pass filter')
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
plt.ylabel("\u03bcV")
plt.title('FFT of signal before downsampling')
plt.subplot(2, 1, 2)
FFT(S_ds, 400)
plt.xlim(0, 200)
plt.ylim(0, 400000)
plt.ylabel("\u03bcV")
plt.title('FFT of signal after downsampling')
plt.show()

Fs = 400
S = S_ds
dt = 1/float(Fs)
t = np.arange(S.size)*dt

FFT(S, 400)
plt.xlim(0, 200)
plt.ylim(0, 400000)
plt.ylabel("\u03bcV")
plt.title('FFT')
plt.show()

STFT(S)

eemd = EEMD()
eIMFs = eemd.eemd(S)

imfNo  = eIMFs.shape[0]

# Plot results in a grid
c = np.floor(np.sqrt(imfNo+1))
r = np.ceil( (imfNo+1)/c)


plt.ioff()
plt.subplot(r,c,1)
plt.plot(t, S, 'r')
#plt.xlim((tMin, tMax))
plt.title("Original signal")

for num in range(imfNo):
    plt.subplot(r,c,num+2)
    plt.plot(t, eIMFs[num],'g')
    #plt.xlim((tMin, tMax))
    plt.title("Imf "+str(num+1))

plt.show()





#save_signal(S_filtered, 'ID0_lastexp_lastsecond_filtered.txt')