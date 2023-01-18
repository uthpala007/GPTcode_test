import sounddevice as sd
import numpy as np

def play_tone(frequency):
    frequency = int(frequency)
    if frequency:
        duration = 100  # in seconds
        sample_rate = 44100
        t = np.linspace(0, duration, int(sample_rate * duration), endpoint=False)
        tone = np.sin(frequency * 2 * np.pi * t)
        sd.play(tone, sample_rate)

