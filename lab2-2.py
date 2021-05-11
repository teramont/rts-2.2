import numpy as np
import matplotlib.pyplot as plt

HARMONICS_COUNT = 6
MAX_FREQUENCY = 1700
DISCRETE_TIMES_COUNT = 1024

def rand_sig(harmonics_count, max_freq, discr_times_count):
	sig = np.zeros(discr_times_count)
	freq_start = max_freq / harmonics_count
	for harmonic_index in range(harmonics_count):
		amplitude = np.random.uniform(0.0, 1000.0)
		phase = np.random.uniform(-np.pi / 2, np.pi / 2)
		freq = freq_start * (harmonic_index + 1)
		for time in range(discr_times_count):
			sig[time] += amplitude * np.sin(freq * time + phase)
	return sig

def fast_fourier_transform(sig):
	if len(sig) <= 1: return sig
	res = np.zeros(len(sig))
	x_even = fast_fourier_transform(sig[::2])
	x_odd = fast_fourier_transform(sig[1::2])
	for p in range(int(len(sig) / 2)):
		angle = 2 * np.pi * p / len(sig)
		turn_coef = complex(np.cos(angle), -np.sin(angle))
		res[p] = x_even[p] + turn_coef * x_odd[p]
		res[p + int(len(sig) / 2)] = x_even[p] - turn_coef * x_odd[p]
	return res


sig = rand_sig(HARMONICS_COUNT, MAX_FREQUENCY, DISCRETE_TIMES_COUNT)

FFT = fast_fourier_transform(sig)

plt.plot(range(DISCRETE_TIMES_COUNT), FFT)
plt.xlabel("p value")
plt.ylabel("FFT value")
plt.show()