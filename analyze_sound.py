import wave
import numpy as np
import matplotlib.pyplot as plt
import pyaudio

CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 1 
RATE = 44100
RECORD_SECONDS = 3

with wave.open('output.wav', 'wb') as wf:
    p = pyaudio.PyAudio()
    wf.setnchannels(CHANNELS)
    wf.setsampwidth(p.get_sample_size(FORMAT))
    wf.setframerate(RATE)

    stream = p.open(format=FORMAT, channels=CHANNELS, rate=RATE, input=True)

    print('Recording...')
    for _ in range(0, RATE // CHUNK * RECORD_SECONDS):
        wf.writeframes(stream.read(CHUNK))
    print('Done')

    stream.close()
    p.terminate()


wav_obj = wave.open('./output.wav', 'rb')
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
plt.title('Izgovorjava "Olu"')
plt.ylabel('Signal')
plt.xlabel('Time (s)')
plt.xlim(0, t_audio)
plt.show()



