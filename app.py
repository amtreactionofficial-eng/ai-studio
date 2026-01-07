import os
from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
from youtube_transcript_api import YouTubeTranscriptApi

app = Flask(__name__)
CORS(app)

def get_youtube_id(url):
    if "v=" in url: return url.split("v=")[1].split("&")[0]
    elif "youtu.be/" in url: return url.split("youtu.be/")[1].split("?")[0]
    return None

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def process_video():
    data = request.json
    url = data.get('url')
    video_id = get_youtube_id(url)
    
    if not video_id:
        return jsonify({"error": "YouTube Link မှားနေပါတယ် ဘရို"}), 400

    try:
        # YouTube ကနေ စာသား (Script) ဆွဲထုတ်ခြင်း
        transcript_list = YouTubeTranscriptApi.get_transcript(video_id)
        full_script = " ".join([t['text'] for t in transcript_list])
        
        return jsonify({
            "title": "YouTube Script ထုတ်ယူမှု အောင်မြင်ပါပြီ",
            "script": full_script
        })
    except Exception as e:
        return jsonify({"error": "ဒီ Video မှာ Script (Captions) ပိတ်ထားလို့ မရနိုင်ပါဘူး ဘရို။"})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
