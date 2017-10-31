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

from pytftb.tftb.generators import noisecu


#S, noise, Fs = generate_signal()

S, Fs = get_signal('ID0_lastexp_lastsecond.txt')
noise = np.zeros(S.size)

T = 1/float(Fs)
t = np.arange(S.size)*T

STFT(S)

#S_filtered = HHT(S, t, noise)

#save_signal(S_filtered, 'ID0_lastexp_lastsecond_filtered.txt')