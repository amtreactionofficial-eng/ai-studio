from flask import Flask, render_template, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def process_video():
    try:
        data = request.json
        video_url = data.get('url')
        
        if not video_url:
            return jsonify({"error": "Link ထည့်ပေးဖို့ လိုပါတယ်"}), 400

        # AI က အလုပ်လုပ်သလိုမျိုး နမူနာ စာသား ထုတ်ပေးခြင်း
        return jsonify({
            "title": "AI စနစ် ချိတ်ဆက်မှု အောင်မြင်သည်",
            "script": f"ဘရို ထည့်လိုက်တဲ့ Link ကတော့: {video_url} ဖြစ်ပါတယ်။ \n\nဒါကတော့ AI ကနေ ထုတ်ပေးလိုက်တဲ့ နမူနာ စာသား (Script) ဖြစ်ပါတယ်။ အခုဆိုရင် Backend နဲ့ Frontend ချိတ်ဆက်မှု ၁၀၀% အောင်မြင်သွားပါပြီ!"
        })
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
