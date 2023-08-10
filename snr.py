from pydub import AudioSegment
import numpy as np

# Function to adjust SNR
def adjust_snr(signal, noise, target_snr):
    signal_power = np.sum(signal**2)
    noise_power = np.sum(noise**2)
    noise_factor = np.sqrt(signal_power / (noise_power * (10 ** (target_snr / 10))))
    adjusted_noise = noise * noise_factor
    return adjusted_noise

# Load speech and noise audio files (Replace file paths with actual files)
speech_file = "path/to/speech.wav"
noise_file = "path/to/noise.wav"

# Load audio files
speech = AudioSegment.from_wav(speech_file)
noise = AudioSegment.from_wav(noise_file)

# Calibrate both speech and noise to -26 dBov
speech = speech - 26
noise = noise - 26

# Define SNR levels
snr_levels = [0, 6, 12, 18]

for snr in snr_levels:
    # Adjust noise to the desired SNR level
    adjusted_noise = adjust_snr(speech, noise, snr)
    
    # Combine speech and noise to create the desired SNR level
    mixed_audio = speech.overlay(adjusted_noise)

    # Save the mixed audio to a new file (Replace output_file_path with the desired path)
    output_file_path = f"path/to/output_audio_snr_{snr}dB.wav"
    mixed_audio.export(output_file_path, format="wav")

print("Audio data generation with different SNR levels completed.")
