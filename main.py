import openai, os
from config import api_key_check


def extract_file_name(path_to_file):
    file_name,extention = os.path.splitext(os.path.basename(path_to_file))
    return file_name

def speech_to_text(path_to_file):
    api_key_check()
    audio_file = open(path_to_file,'rb')
    print('Processing data...')

    transcript = openai.Audio.transcribe('whisper-1',audio_file)
    x = str(transcript['text'])
    file_name = extract_file_name(path_to_file)

    with open(f'{file_name} transcribed.txt','w') as file:
        file.write(x)
    print('Successfully created!')

speech_to_text('/Users/aldmikon/Desktop/Youtube stuff/music for Youtube/Best of Me.mp3')