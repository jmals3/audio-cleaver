# Audio Cleaver

Audio Cleaver is a simple yet effective Python-based program that allows users to trim audio files easily. The user interface provides options for selecting an audio file, specifying the start and end times, and trimming the audio file to the desired range. The output file will be saved in the same directory as the input file, with the trimmed time range appended to the filename.

## Prerequisites

Before you can use Audio Cleaver, please ensure you have the following installed:

1. Python 3.6 or higher (download from [Python's official website](https://www.python.org/downloads/))
2. PyQt5: Install using `pip`:

   ```
   pip install PyQt5
   ```

3. Pydub: Install using `pip`:

   ```
   pip install pydub
   ```

4. TinyTag: Install using `pip`:

   ```
   pip install tinytag
   ```

5. FFmpeg: Audio Cleaver relies on FFmpeg for processing audio files. Please follow the installation instructions for your operating system:

   - Windows: Download the FFmpeg executable from the [official website](https://www.ffmpeg.org/download.html) and extract the downloaded ZIP file. Add the `bin` folder inside the extracted folder to your system's PATH.

   - macOS: Install FFmpeg using Homebrew:

     ```
     brew install ffmpeg
     ```

   - Ubuntu:

     ```
     sudo apt update
     sudo apt install ffmpeg
     ```

## Usage

1. Run the Audio Cleaver Python script:

   ```
   python audio_cleaver.py
   ```

2. Use the "Browse" button to select an audio file.

3. Enter the start and end times in the "Start Time" and "Stop Time" input fields, respectively. Use the `hh:mm:ss` format.

4. Click the "OK" button to trim the audio file. The output file will be saved in the same directory as the input file, with the start and stop times appended to the filename (e.g., `inputfile_0h0m0s_0h3m0s.wav`).

5. Check the output window for the status of the operation. If successful, you'll see the message "Success". If not, an error message will be displayed.

## Troubleshooting

If you encounter issues when using Audio Cleaver, please check the following:

1. Ensure that all required packages and software, including FFmpeg, are installed correctly.

2. Make sure you're using a supported audio file format (e.g., MP3, WAV, OGG, or FLAC).

3. Verify that the start and end times are entered in the correct format (hh:mm:ss) and that the start time is less than the end time.

4. If the program still doesn't work, please consult the error message displayed in the output window for more information.