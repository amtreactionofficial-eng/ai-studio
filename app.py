import os, re
from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
from youtube_transcript_api import YouTubeTranscriptApi

app = Flask(__name__)
CORS(app)

def get_youtube_id(url):
    # YouTube Shorts ရော Video ရော ID ယူနိုင်အောင် ပြင်ထားတယ်
    id_match = re.search(r'(?:v=|\/)([0-9A-Za-z_-]{11}).*', url)
    return id_match.group(1) if id_match else None

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def process_video():
    try:
        data = request.json
        url = data.get('url')
        video_id = get_youtube_id(url)
        
        if not video_id:
            return jsonify({"error": "YouTube Link မှားနေပါတယ်"}), 400

        # Transcript ဆွဲထုတ်ခြင်း
        transcript_list = YouTubeTranscriptApi.get_transcript(video_id)
        full_script = " ".join([t['text'] for t in transcript_list])
        
        # ဒီနေရာမှာ AI Feature တွေအတွက် နမူနာစာသားတွေပါ ထည့်ပေးလိုက်တယ်
        return jsonify({
            "success": True,
            "title": "YouTube Script ရရှိပါပြီ",
            "script": full_script,
            "myanmar": "အခုဒါကတော့ AI ကနေ မြန်မာလို ဘာသာပြန်ပေးထားတဲ့ စာသားဖြစ်ပါတယ်။ (Google Translate API ချိတ်ဆက်ရန် လိုအပ်ပါသည်)",
            "fb_post": f"🚀 Video Content Summary: \n\n{full_script[:100]}... #AI_Myanmar_Studio"
        })
    except Exception as e:
        return jsonify({"error": "ဒီ Video မှာ စာသားထုတ်လို့မရပါဘူး။ Script ပိတ်ထားတာ ဖြစ်နိုင်ပါတယ်။"}), 500

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=9999)
