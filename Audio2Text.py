# importing libraries 
import speech_recognition as sr 
import os 
from pydub import AudioSegment
from pydub.silence import split_on_silence
import re
# create a speech recognition object
# 50 request per day
r = sr.Recognizer()



# Function to extract the numeric part of the filename
def extract_number(filename):
    match = re.search(r'\d+', filename)
    if match:
        return int(match.group())
    else:
        return None




# a function to recognize speech in the audio file
# so that we don't repeat ourselves in in other functions
def transcribe_audio(path):
    # use the audio file as the audio source
    with sr.AudioFile(path) as source:
        audio_listened = r.record(source)
        # try converting it to text
        text = r.recognize_google(audio_listened , language="fa-IR")
    return text

# a function that splits the audio file into chunks on silence
# and applies speech recognition
def get_large_audio_transcription_on_silence(path):
    """Splitting the large audio file into chunks
    and apply speech recognition on each of these chunks"""
    # open the audio file using pydub
    sound = AudioSegment.from_file(path)
    chunksize=60000
    # # split audio sound where silence is 500 miliseconds or more and get chunks
    # chunks = split_on_silence(sound,
    #     # experiment with this value for your target audio file
    #     min_silence_len = 500,
    #     # adjust this per requirement
    #     silence_thresh = sound.dBFS-14,
    #     # keep the silence for 1 second, adjustable as well
    #     keep_silence=500,
    # )
    def divide_chunks(sound, chunksize):
        # looping till length l
        for i in range(0, len(sound), chunksize):
            yield sound[i:i + chunksize]
            
    chunks = list(divide_chunks(sound, chunksize))
    print(f"{len(chunks)} chunks of {chunksize/1000}s each")
    if len(chunks) >= 50:
        # print("Rate limit is process 100 chunks per day !")
        print("Be careful about rate limit !")
        # exit()
    folder_name = f"audio-chunks-{filename}"
    
    
    # create a directory to store the audio chunks
    # If directory exist we continue from last file
    latest_number = None
    if not os.path.isdir(folder_name):
        os.mkdir(folder_name)
    else:
        files = os.listdir(folder_name)
        numbers = []
        for f in files:
            numbers.append(f.split('.')[0])
        
        latest_number = max(numbers) if numbers else None
            
    
    whole_text = ""
    # process each chunk 
    
    start = latest_number if latest_number else 1
        
    for i, audio_chunk in enumerate(chunks, int(start)):
        # export audio chunk and save it in
        print("Process chunk ",str(i))
        # the `folder_name` directory.
        chunk_filename = os.path.join(folder_name, f"{i}.wav")
        audio_chunk.export(chunk_filename, format="wav")
        # recognize the chunk
        try:
            text = transcribe_audio(chunk_filename)
            # print(f"Recognize voice for {chunk_filename}")
        except  Exception as e:
            print("Error:", str(e))
            print(f"When processing chunk{chunk_filename}")
            return whole_text
        else:
            text = f"{text.capitalize()}. "
            print(chunk_filename, ":", text)
            whole_text += text
    # return the text for all chunks detected
    return whole_text
    
    
filepath = "Bugbounty.mp3"
# Split filename by .
filename = filepath.split('.')[0]
sound = AudioSegment.from_mp3(filepath)
temp = f"{filename}.wav"
sound.export(temp, format="wav")
text = get_large_audio_transcription_on_silence(temp)
print("\nFull text:", text)
result = (f'{filename}.txt')
open(result, 'a+').writelines(text)