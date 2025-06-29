
from google.cloud import texttospeech
import os

def synthesize_text(script_text, output_dir='output'):
    client = texttospeech.TextToSpeechClient()
    voice = texttospeech.VoiceSelectionParams(
        language_code="en-US",
        name="en-US-Studio-O"
    )
    audio_config = texttospeech.AudioConfig(audio_encoding=texttospeech.AudioEncoding.MP3)

    os.makedirs(output_dir, exist_ok=True)
    lines = script_text.strip().split('\n')
    for i, line in enumerate(lines):
        if not line.strip():
            continue
        synthesis_input = texttospeech.SynthesisInput(text=line)
        response = client.synthesize_speech(
            input=synthesis_input,
            voice=voice,
            audio_config=audio_config
        )
        with open(f"{output_dir}/line_{i:02}.mp3", "wb") as out:
            out.write(response.audio_content)
