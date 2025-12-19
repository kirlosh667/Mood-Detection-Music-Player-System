import os
from deepface import DeepFace

def detect_emotion(image_path):
    """Detect emotion from the captured image using DeepFace"""
    try:
        if not image_path or not os.path.exists(image_path):
            print("Error: Image file not found.")
            return "neutral"

        print("🎭 Analyzing your emotion... Please wait...")
        result = DeepFace.analyze(img_path=image_path, actions=['emotion'], enforce_detection=True)
        
        emotion = result[0]['dominant_emotion']
        print(f"🧠 Detected Mood: {emotion.upper()}")
        return emotion.lower()
    except Exception as e:
        print(f"❌ Error detecting emotion: {e}")
        return "neutral"
