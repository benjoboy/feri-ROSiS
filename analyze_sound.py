import wave
import numpy as np
import matplotlib.pyplot as plt


wav_obj = wave.open('./pad.wav', 'rb')
sample_freq = wav_obj.getframerate()



n_samples = wav_obj.getnframes()

t_audio = n_samples/sample_freq

n_channels = wav_obj.getnchannels()


signal_wave = wav_obj.readframes(n_samples)
signal_array = np.frombuffer(signal_wave, dtype=np.int16)

# l_channel = signal_array[0::2]


times = np.linspace(0, n_samples/sample_freq, num=n_samples)

plt.figure(figsize=(15, 5))
plt.plot(times, signal_array)
plt.title('Left Channel')
plt.ylabel('Signal Value')
plt.xlabel('Time (s)')
plt.xlim(0, t_audio)
plt.show()



