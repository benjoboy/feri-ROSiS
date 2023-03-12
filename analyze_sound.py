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
    #nastavimo število kanalov torej 1 za mono in 2 za stereo
    p = pyaudio.PyAudio()
    wf.setnchannels(CHANNELS)
    #nastavimo število bitov na vzorec glede na format
    wf.setsampwidth(p.get_sample_size(FORMAT))
    #nastavimo frekvenco vzorčenja
    wf.setframerate(RATE)

    stream = p.open(format=FORMAT, channels=CHANNELS, rate=RATE, input=True)

    print('Recording...')
    for _ in range(0, RATE // CHUNK * RECORD_SECONDS):
        #zapisemo v datoteko
        wf.writeframes(stream.read(CHUNK))
    print('Done')

    stream.close()
    p.terminate()

#odpremo datoteko ki smo jo ravno posneli
wav_obj = wave.open('./output.wav', 'rb')

st_vzorcev = wav_obj.getnframes()

#stevilo sekund
t_audio = st_vzorcev/RATE

#preberemo signale
signal_wave = wav_obj.readframes(st_vzorcev)
signal = np.frombuffer(signal_wave, dtype=np.int16)

#casovna os
times = np.linspace(0, st_vzorcev/RATE, num=st_vzorcev)


#izris signala
plt.figure(figsize=(15, 5))
plt.plot(times, signal)
plt.title('Izgovorjava "Olu"')
plt.ylabel('Signal')
plt.xlabel('Time (s)')
plt.xlim(0, t_audio)
plt.show()



