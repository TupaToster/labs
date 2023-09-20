import sounddevice as sd
import matplotlib.pyplot as plt
import numpy as np
from scipy.fft import fft, fftfreq

time_0 = 0.5
fs = 44100
T = 1.0 / fs
N_0 = int (fs * time_0)

time = 0
N = 0
sound = np.array ([])

try:
    for i in range (100):
        y = sd.rec (N_0, samplerate=fs, channels=2)
        plt.figure (figsize = (16, 9), dpi = 100)
        N += N_0
        time += time_0
        x = np.linspace (0.0, N * T, N, endpoint=False)
        xf = fftfreq (N, T)[:N//2]
        plt.xlim (0, 1000)
        plt.grid()
        sd.wait ()
        y = np.array ([i[0] for i in y], dtype=float)
        sound = np.append (sound, y)
        yf = fft (sound)
        plt.plot(xf, time / N * np.abs(yf[0:N//2]))
        plt.xlabel (fr'$\nu$, herz')
        plt.savefig ('lol.png')
        plt.close ()
    exit (0)
finally:
    y = sd.rec (N_0, samplerate=fs, channels=2)
    plt.figure (figsize = (16, 9), dpi = 100)
    N += N_0
    time += time_0
    x = np.linspace (0.0, N * T, N, endpoint=False)
    xf = fftfreq (N, T)[:N//2]
    plt.xlim (0, 1000)
    plt.grid()
    sd.wait ()
    y = np.array ([i[0] for i in y], dtype=float)
    sound = np.append (sound, y)
    yf = fft (sound)
    plt.plot(xf, time / N * np.abs(yf[0:N//2]))
    plt.xlabel (fr'$\nu$, herz')
    plt.show ()