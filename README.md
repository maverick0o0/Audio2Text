This document includes an overview, installation requirements, usage instructions, functions descriptions, and a sample output section.

# Audio Transcription Tool

This Python script provides a utility for transcribing long audio files into text. It uses the speech_recognition and pydub libraries to process audio files, split them based on silence, and convert the audio chunks to text using Google’s speech recognition API.

## Features
Audio Splitting: Splits large audio files into manageable chunks based on silence.
Speech Recognition: Transcribes audio to text using Google’s speech recognition service.
Resumable Processing: Keeps track of processed chunks to allow resumption of transcription.
Installation

Before running the script, ensure you have Python installed on your system. Then, install the necessary Python libraries using pip:

```bash
pip install speechrecognition pydub
```

Note: pydub requires FFmpeg for audio format operations. Install FFmpeg by following the instructions on the official FFmpeg download page.

Usage
Place your audio file in the same directory as the script or provide the path to the file.
Run the script with Python:
```bash
python audio_transcription.py
```
The script will output the transcription to a text file named after the audio file.
Code Description
Functions
extract_number(filename): Extracts numbers from filenames, useful for sorting or versioning.
transcribe_audio(path): Transcribes a single audio file to text using Google’s speech recognition.
get_large_audio_transcription_on_silence(path): Processes a large audio file by splitting it into chunks, transcribing each chunk, and compiling the results.
Main Execution

The script executes the transcription process for an audio file named Bugbounty.mp3, converting it into a .wav format, and then processing it through the get_large_audio_transcription_on_silence function.

Sample Output

The script will output the transcription to a text file and print the transcription to the console. Here’s a sample of what the console output might look like:

```plaintext
Processing chunk 1
audio-chunks-Bugbounty/1.wav : Hello world. 
Processing chunk 2
audio-chunks-Bugbounty/2.wav : This is a test. 
Full text: Hello world. This is a test. ...
```

Limitations
The script is rate-limited by Google’s speech recognition API to 100 requests per day.
It currently supports only Farsi (fa-IR) for the speech recognition language.

This document provides a comprehensive guide to using and understanding the Python script for audio transcription. Adjust the content as necessary to better fit the actual functionality and limitations of your script.
