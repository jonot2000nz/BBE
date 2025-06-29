
import os
from flask import Flask, request, render_template, send_file
from gcloud_tts import synthesize_text
from video_builder import build_video

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        script = request.form['script']
        with open('script.txt', 'w') as f:
            f.write(script)
        synthesize_text(script)
        build_video(script)
        return send_file('output/final_video.mp4', as_attachment=True)
    return render_template('index.html')

if __name__ == '__main__':
    os.makedirs("output", exist_ok=True)
    app.run(host='0.0.0.0', port=5000)
