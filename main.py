import openai, os

def input_api_key(): 
    key = str(input('Please provide your API key here:'))
    openai.api_key = key
    return openai.api_key

def extract_file_name(path_to_file):
    file_name,extention = os.path.splitext(os.path.basename(path_to_file))
    return file_name

def speech_to_text(path_to_file):
    input_api_key()
    audio_file = open(path_to_file,'rb')
    print('Processing data...')

    transcript = openai.Audio.transcribe('whisper-1',audio_file)
    x = str(transcript['text'])
    file_name = extract_file_name(path_to_file)

    with open(f'{file_name} transcribed2.txt','w') as file:
        file.write(x)
    print('Successfully created!')

speech_to_text('/Users/aldmikon/Desktop/Youtube stuff/music for Youtube/Best of Me.mp3')