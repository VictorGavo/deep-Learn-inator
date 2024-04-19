# transcriber.py: Handles the conversion of audio from videos and podcasts to text.
# - If input is a YouTube video or video file:
#   - Extract audio using moviepy
#   - Transcribe audio to text using speech_recognition
# - If input is a podcast (audio file):
#   - Transcribe directly using speech_recognition
# - Return transcribed text

import moviepy.editor as mp
from SpeechRecognition import Recognizer, AudioFile
import os
from config import FILE_PATHS

# Initialize the speech recognizer
recognizer = Recognizer()

def extract_audio_from_video(video_path):
    # Extract audio from video file and save as an audio file
    video = mp.VideoFileClip(video_path)
    audio_path = os.path.splitext(video_path)[0] + '.wav'
    video.audio.write_audiofile(audio_path)
    return audio_path

def transcribe_audio(audio_path):
    # Transcribe the audio file to text using speech recognition
    with AudioFile(audio_path) as source:
        audio = recognizer.record(source)
        try:
            # Attempt to transcribe the audio to text
            text = recognizer.recognize_google(audio)
            return text
        except Exception as e:
            print(f"Error transcribing audio: {str(e)}")
            return None

def transcribe(video_or_audio_path, file_type='video'):
    # Determine the type of file and process accordingly
    if file_type == 'video':
        # Extract audio from video then transcribe
        audio_path = extract_audio_from_video(video_or_audio_path)
        return transcribe_audio(audio_path)
    elif file_type == 'audio':
        # Directly transcribe audio file
        return transcribe_audio(video_or_audio_path)
    else:
        raise ValueError("Unsupported file type. Please use 'video' or 'audio'.")
