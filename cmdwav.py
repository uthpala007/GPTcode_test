import wave
import numpy as np
import argparse

# Create command line argument parser
parser = argparse.ArgumentParser()

# Add arguments for frequency, amplitude, duration and break
parser.add_argument("-f", "--frequency", type=float, required=True, help="Frequency of the tone in hertz")
parser.add_argument("-a", "--amplitude", type=float, required=True, help="Amplitude of the tone as a percentage")
parser.add_argument("-d", "--duration", type=float, required=True, help="Duration of the tone in seconds")
parser.add_argument("-b", "--breaktime", type=float, default=0.5, help="length of the break time in seconds")

# Parse the command line arguments
args = parser.parse_args()

frequency = args.frequency
amplitude = args.amplitude/100
duration = args.duration
breaktime = args.breaktime

# Set the sample rate and number of frames
sample_rate = 48000
num_frames = int(sample_rate * duration)

# Generate the tone

# Sine wave
# tone = np.array([np.sin(2*np.pi*frequency*x/sample_rate)*(amplitude) for x in range(num_frames)], dtype=np.float32)
# tone = amplitude * np.sin(2 * np.pi * frequency * np.linspace(0, duration, num_frames))

# Square wave
tone = amplitude * np.sign(np.sin(2 * np.pi * frequency * np.arange(num_frames) / sample_rate))
# tone = amplitude * (np.square(2 * np.pi * np.arange(num_frames) * frequency / sample_rate))

# Sawtooth wave
# tone = np.array([amplitude * (2 * (np.arange(num_frames) / sample_rate * frequency) % 2 - 1) for x in range(num_frames)], dtype=np.float32)

# Triangle wave
# tone = amplitude * (2 / np.pi) * np.arcsin(np.sin(2 * np.pi * frequency * np.arange(num_frames) / sample_rate))

# convert samples to 16-bit integers
tone = np.array(tone*32767, dtype=np.int16)

#Add the break to the tone
sine_wave_with_break = np.concatenate([tone, np.zeros(int(sample_rate * args.breaktime))])
for i in range(int(duration/breaktime)):
    sine_wave_with_break = np.concatenate([sine_wave_with_break, tone, np.zeros(int(sample_rate * breaktime))])

# Create a wave file object
# wave_file = wave.open("finger.wav", "w"
wav_file = wave.open("sine_wave_with_break.wav", "w")


# Set the wave file parameters
# wave_file.setparams((1, 4, sample_rate, num_frames, "NONE", "not compressed"))
wav_file.setparams((1, 4, sample_rate, num_frames, "NONE", "not compressed"))


# Write the tone data to the wave file
# wave_file.writeframes(tone.tostring())
wav_file.writeframes(sine_wave_with_break)


# Close the wave file
# wave_file.close()
wav_file.close()

print("Wav file has been created and saved in the current directory with name")