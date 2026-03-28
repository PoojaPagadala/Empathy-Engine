from flask import Flask, render_template, request
from emotion import detect_emotion
from tts_engine import generate_speech
import time
import os

app = Flask(__name__)

# Ensure static folder exists
if not os.path.exists("static"):
    os.makedirs("static")

OUTPUT_PATH = "static/output.mp3"

@app.route("/", methods=["GET", "POST"])
def index():
    emotion = None

    if request.method == "POST":
        text = request.form.get("text")

        # Safety check
        if text and text.strip() != "":
            
            # Detect emotion
            emotion, intensity = detect_emotion(text)
            print("Final Emotion:", emotion)

            # Generate speech
            generate_speech(text, emotion, intensity, OUTPUT_PATH)

    # Pass timestamp to avoid caching issue
    return render_template(
        "index.html",
        emotion=emotion,
        timestamp=time.time()
    )


if __name__ == "__main__":
    app.run(debug=True)