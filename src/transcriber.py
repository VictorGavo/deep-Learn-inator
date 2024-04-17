# transcriber.py: Handles the conversion of audio from videos and podcasts to text.
# - If input is a YouTube video or video file:
#   - Extract audio using moviepy
#   - Transcribe audio to text using speech_recognition
# - If input is a podcast (audio file):
#   - Transcribe directly using speech_recognition
# - Return transcribed text

