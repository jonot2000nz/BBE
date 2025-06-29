
import os
from moviepy.editor import AudioFileClip, ImageClip, concatenate_videoclips

def build_video(script_text, output_dir='output'):
    clips = []
    lines = script_text.strip().split('\n')
    for i, line in enumerate(lines):
        audio_path = f"{output_dir}/line_{i:02}.mp3"
        if not os.path.exists(audio_path):
            continue
        audio_clip = AudioFileClip(audio_path)
        image_path = "fallback.jpg"  # Placeholder image assumed to be present
        img_clip = ImageClip(image_path).set_duration(audio_clip.duration).set_audio(audio_clip)
        img_clip = img_clip.resize(height=720).set_position('center')
        clips.append(img_clip)
    if clips:
        final = concatenate_videoclips(clips)
        final.write_videofile(f"{output_dir}/final_video.mp4", fps=24)
