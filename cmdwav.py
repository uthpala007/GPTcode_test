import wave
import numpy as np
import argparse

# Create command line argument parser
parser = argparse.ArgumentParser()

# Add arguments for frequency, amplitude, and duration
parser.add_argument("-f", "--frequency", type=float, required=True, help="Frequency of the tone in hertz")
parser.add_argument("-a", "--amplitude", type=float, required=True, help="Amplitude of the tone as a percentage")
parser.add_argument("-d", "--duration", type=float, required=True, help="Duration of the tone in seconds")

# Parse the command line arguments
args = parser.parse_args()

# Set the sample rate and number of frames
sample_rate = 48000
num_frames = int(sample_rate * args.duration)

# Generate the tone
tone = np.array([np.sin(2*np.pi*args.frequency*x/sample_rate)*(args.amplitude/100) for x in range(num_frames)], dtype=np.float32)

# Create a wave file object
wave_file = wave.open("400Hz.wav", "w")

# Set the wave file parameters
wave_file.setparams((1, 4, sample_rate, num_frames, "NONE", "not compressed"))

# Write the tone data to the wave file
wave_file.writeframes(tone.tostring())

# Close the wave file
wave_file.close()

print("Wav file has been created and saved in the current directory with name")


""" import argparse
import numpy as np
import wave

def generate_tone(frequency, amplitude, duration, sample_rate, vibrato_rate=5, vibrato_depth=0.1):
    num_frames = int(sample_rate * duration)
    time_array = np.linspace(0, duration, num_frames)
    modulation_wave = np.sin(2 * np.pi * vibrato_rate * time_array)
    frequency_modulation = modulation_wave * vibrato_depth
    modulated_frequency = frequency + frequency_modulation
    samples = amplitude * np.sin(2 * np.pi * modulated_frequency * np.arange(num_frames) / sample_rate)

    return samples

def save_to_wav(samples, sample_rate, filename):
    wav_file = wave.open(filename, "w")
    wav_file.setparams((1, 2, sample_rate, 0, "NONE", "not compressed"))
    wav_file.writeframes(samples.tostring())
    wav_file.close()

parser = argparse.ArgumentParser()
parser.add_argument("-f", "--frequency", type=float, help="frequency of the tone in hertz", required=True)
parser.add_argument("-a", "--amplitude", type=float, help="amplitude of the tone as a percentage", required=True)
parser.add_argument("-d", "--duration", type=float, help="duration of the tone in seconds", required=True)
parser.add_argument("-vr", "--vibrato_rate", type=float, help="vibrato rate of the tone in Hz", default=5)
parser.add_argument("-vd", "--vibrato_depth", type=float, help="vibrato depth of the tone in percentage", default=0.1)


args = parser.parse_args()
sample_rate = 44100
samples = generate_tone(args.frequency, args.amplitude, args.duration, sample_rate, args.vibrato_rate, args.vibrato_depth)
save_to_wav(samples, sample_rate, "vibrato_tone.wav")
 """