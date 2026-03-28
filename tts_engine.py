import pyttsx3

engine = pyttsx3.init()

def set_voice_properties(emotion, intensity):
    
    # Base rate
    base_rate = 160
    
    if emotion == "positive":
        rate = base_rate + int(intensity * 60)
        volume = 1.0
        
    elif emotion == "negative":
        rate = base_rate + int(intensity * 40)  # intensity is negative
        volume = 0.7
        
    else:
        rate = base_rate
        volume = 0.9

    engine.setProperty('rate', rate)
    engine.setProperty('volume', volume)


def generate_speech(text, emotion, intensity, output_path):
    
    set_voice_properties(emotion, intensity)

    engine.save_to_file(text, output_path)
    engine.runAndWait()