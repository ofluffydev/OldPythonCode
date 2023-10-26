import math
import pyaudio

class Player:
    def __init__(self):
        self.p = pyaudio.PyAudio()
        self.volume = 0.5
        self.fs = 44100

    def play_note(self, freq, duration):
        samples = []
        for i in range(int(duration * self.fs)):
            samples.append(int(32767.0 * self.volume * math.sin(2.0 * math.pi * freq * float(i) / float(self.fs))))
        stream = self.p.open(format=pyaudio.paInt16, channels=1, rate=self.fs, output=True)
        stream.write(bytes(samples))
        stream.close()