from pydub import AudioSegment
from scipy.io import wavfile
import numpy as np
from scipy.signal import find_peaks

index = 1;
# Path to the MP3 file
mp3_file_path = "./out/" + str(index) + ".mp3"

# Convert MP3 to WAV using pydub
audio = AudioSegment.from_mp3(mp3_file_path)
wav_file_path = "./out/" + str(index) + ".wav"
audio.export(wav_file_path, format="wav")

# Read the WAV file for analysis
sample_rate, data = wavfile.read(wav_file_path)

# Convert to mono if stereo
if len(data.shape) > 1:
    data = data.mean(axis=1)

# Normalize audio data
data = data / np.max(np.abs(data))

# Detect peaks to estimate paddle hits
# Set parameters: 0.5 height threshold and minimum distance of 0.2 seconds
peaks, _ = find_peaks(data, height=0.5, distance=int(sample_rate * 0.2))

# Count the detected hits
number_of_hits = len(peaks)
print(f"Number of paddle hits: {number_of_hits}")

# create a new file with the number of hits
with open("./out/" + str(index) + ".txt", "w") as f:
    f.write(str(number_of_hits))
