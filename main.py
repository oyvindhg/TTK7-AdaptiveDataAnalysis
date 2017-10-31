import numpy as np
import matplotlib.pyplot as plt
from pytftb.tftb.generators import noisecu

# -- The signals --
# Amplitude
A = 1

# Frequencies
f1 = 3
f2 = 7
f3 = 12
f4 = 15
f5 = 18


# Sampling
Fs = 1000
T = 1/float(Fs)
L = 3000

t = np.arange(L)*T
t2 = np.arange(1500,2500)*T
t3 = np.arange(1000,2000)*T
t4 = np.arange(0,1000)*T

s1 = A*np.sin(2*np.pi*f1*t)
s2 = np.concatenate([ np.zeros(1500), A*np.sin(2*np.pi*f2*t2), np.zeros(500) ])
s3 = np.concatenate([ np.zeros(1000), A*np.sin(2*np.pi*f3*t3), np.zeros(1000) ])
s4 = np.concatenate([ A*np.sin(2*np.pi*f4*t4), np.zeros(2000) ])
s5 = np.concatenate([ A*np.sin(2*np.pi*f5*t) ])

# Analytic complex uniform white noise.
noise = noisecu(L)

S = s1 + s2 + s3 + s4 + s5 + noise

plt.figure(1)
plt.suptitle("Signals")

plt.subplot(7,1,6)
plt.ylabel("3 Hz")
plt.plot(s1)

plt.subplot(7,1,5)
plt.ylabel("7 Hz")
plt.plot(s2)

plt.subplot(7,1,4)
plt.ylabel("12 Hz")
plt.plot(s3)

plt.subplot(7,1,3)
plt.ylabel("15 Hz")
plt.plot(s4)

plt.subplot(7,1,2)
plt.ylabel("18 Hz")
plt.plot(s5)

plt.subplot(7,1,1)
plt.ylabel("Noise")
plt.plot(noise)

plt.subplot(7,1,7)
plt.ylabel("Sum")
plt.plot(S)

plt.show()