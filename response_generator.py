from emotion_detector import detect_emotion

def generate_response(text):
    emotion = detect_emotion(text)

    if emotion == "joy":
        return "😊 I'm glad to hear that! Tell me more."
    elif emotion == "sadness":
        return "😔 I'm really sorry you're feeling this way. I'm here for you."
    elif emotion == "anger":
        return "😡 That sounds upsetting. I'm listening."
    else:
        return "🤖 I'm here to chat. How can I help you today?"
