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

from pytftb.tftb.generators import noisecu




# S, Fs = get_signal('ID0_lastexp_last2seconds.txt')
# noise = np.zeros(S.size)
#
# noise_std = np.std(S)
# print(noise_std)

S, noise, Fs = generate_signal()


#find_spikes(S)


T = 1/float(Fs)
t = np.arange(S.size)*T
#STFT(S)
#CWT(S)

f_modeex = [1000]
A_modeex = [0.5]
index_modeex = [0]


imfs = HHT(S, t, noise, f_modeex, A_modeex, index_modeex)

for i in range(0, len(imfs)):
    FFT(imfs[i], Fs)

#save_signal(S_filtered, 'ID0_lastexp_lastsecond_filtered.txt')