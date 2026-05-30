import os
from flask import Flask, render_template, request, jsonify
import os
from dotenv import load_dotenv
import google.generativeai as genai

app = Flask(__name__)

load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")
genai.configure(api_key=api_key)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/generate", methods=["POST"])
def generate():
    try:
        data = request.json
        venue = data.get("venue", "")
        tournament = data.get("tournament", "")
        offer = data.get("offer", "")
        timing = data.get("timing", "")

        prompt = f"""
        You are a social media expert for a Box Cricket business.
        Create social media content for the following details:
        
        Venue Name: {venue}
        Tournament Details: {tournament}
        Offer Details: {offer}
        Timing: {timing}
        
        Please generate:
        1. INSTAGRAM CAPTION: An engaging Instagram caption (2-3 lines)
        2. WHATSAPP MESSAGE: A friendly WhatsApp message
        3. HASHTAGS: 10 relevant hashtags
        
        Format your response exactly like this:
        INSTAGRAM CAPTION:
        [caption here]
        
        WHATSAPP MESSAGE:
        [message here]
        
        HASHTAGS:
        [hashtags here]
        """

        model = genai.GenerativeModel("gemini-1.5-flash")
        response = model.generate_content(prompt)
        return jsonify({"result": response.text})

    except Exception as e:
        print("ERROR:", str(e))
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)
    if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))