# Empathy-Engine


## Project Overview

Empathy Engine is an AI-powered system that transforms plain text into **emotionally expressive speech**. Unlike traditional Text-to-Speech (TTS) systems that produce flat and robotic voices, this project detects the **underlying emotion in text** and dynamically adjusts voice characteristics such as speed and volume to create a more **human-like and engaging audio output**.

The goal of this project is to bridge the gap between **text-based sentiment** and **natural voice interaction**, improving user experience in applications like customer support, virtual assistants, and AI-driven communication systems.

---

##  Features

*  Emotion Detection (Positive, Negative, Neutral)
*  Voice Modulation (Rate & Volume control)
*  Audio Output Generation (.mp3)
*  Simple Web Interface using Flask
*  Real-time processing and playback

---

##  Tech Stack

* **Language:** Python
* **Backend Framework:** Flask
* **NLP Model:** VADER Sentiment Analyzer (NLTK)
* **Text-to-Speech Engine:** pyttsx3
* **Frontend:** HTML

---

##  Setup Instructions

### 1. Clone the Repository

```bash
git clone <your-repo-url>
cd empathy-engine
```

---

### 2. Create Virtual Environment (Recommended)

```bash
python -m venv venv
venv\Scripts\activate   # Windows
```

---

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 4. Run the Application

```bash
python app.py
```

---

### 5. Open in Browser

```text
http://127.0.0.1:5000/
```

---

### 6. Usage

1. Enter any text in the input box
2. Click **"Generate Voice"**
3. The system will:

   * Detect emotion
   * Generate speech
   * Play audio in the browser

---

##  System Architecture

```text
Text Input → Emotion Detection → Voice Parameter Mapping → TTS Engine → Audio Output
```

---

##  Emotion Detection Logic

The system uses VADER sentiment analysis to compute a **compound score** ranging from -1 to +1.

| Score Range | Emotion  |
| ----------- | -------- |
| ≥ 0.3       | Positive |
| ≤ -0.3      | Negative |
| Otherwise   | Neutral  |

Additionally, a **keyword override mechanism** is implemented to handle strong emotional words like:

* "terrible"
* "unacceptable"
* "worst"
* "awful"

This ensures better accuracy in edge cases where sentiment models may fail.

---

##  Emotion → Voice Mapping Logic

The core of the Empathy Engine lies in mapping emotions to vocal characteristics:

| Emotion  | Speech Rate | Volume | Effect                  |
| -------- | ----------- | ------ | ----------------------- |
| Positive | Fast        | High   | Energetic, enthusiastic |
| Negative | Slow        | Low    | Calm, serious           |
| Neutral  | Normal      | Medium | Balanced                |

### Implementation Details

* **Rate (Speed):**

  * Increased for positive emotions
  * Decreased for negative emotions
* **Volume:**

  * Slightly reduced for negative tones
  * Higher for positive tones

### Intensity Scaling

The compound score also influences how strongly these parameters are adjusted:

```python
rate = base_rate + int(intensity * factor)
```

This allows:

* Mild emotions → subtle voice change
* Strong emotions → noticeable voice modulation

---

##  Project Structure

```text
empathy-engine/
│
├── app.py
├── emotion.py
├── tts_engine.py
├── requirements.txt
├── README.md
│
├── templates/
│   └── index.html
│
└── static/
    └── output.mp3
```

---


##  Conclusion

Empathy Engine demonstrates how combining **NLP and speech synthesis** can create more natural and emotionally aware AI systems. It highlights the importance of **emotional intelligence in AI-driven communication**, making interactions more engaging and human-like.

---
