# Speech and Noise Signal-to-Noise Ratio (SNR) Adjuster

The **Speech and Noise SNR Adjuster** is a Python script that generates audio files with different Signal-to-Noise Ratio (SNR) levels by combining speech and noise audio. It calculates the adjusted noise level based on the desired SNR and mixes it with speech to create audio with the specified SNR.

## Features

- **Adjust SNR:** The script allows you to adjust the SNR between speech and noise by mixing them in different ratios, creating audio files with varying degrees of noise presence.

## Getting Started

To use the Speech and Noise SNR Adjuster, follow these steps:

1. **Installation:** Make sure you have Python installed on your system. Install the required dependencies using the following command:

    ```
    pip install pydub numpy
    ```

2. **Preparing Audio Files:** Replace the file paths in the script (`speech_file` and `noise_file`) with the paths to your speech and noise audio files.

3. **Running the Script:** Run the provided Python script `adjust_snr.py` to generate audio files with different SNR levels.

4. **Adjusting SNR Levels:** Modify the `snr_levels` list in the script to include the desired SNR levels you want to generate.

5. **Output:** The script will create audio files for each SNR level in the specified output directory.

## Usage

1. Replace `speech_file` and `noise_file` with the paths to your actual speech and noise audio files.

2. Run the `adjust_snr.py` script using Python.

3. The script will generate audio files for each SNR level specified in the `snr_levels` list.

## Output

The generated audio files will be named according to their SNR level and saved in the output directory. You can listen to these files to hear the effect of different SNR levels.

## Contributing

If you're interested in contributing to the Speech and Noise SNR Adjuster, feel free to fork this repository, make improvements, and submit pull requests.

## License

This project is licensed under the [MIT License](LICENSE).

## Acknowledgments

The Speech and Noise SNR Adjuster script is a practical tool for generating audio with various SNR levels. The code provided demonstrates the mixing of speech and noise to achieve different SNR levels, which can be useful for various audio processing applications.
