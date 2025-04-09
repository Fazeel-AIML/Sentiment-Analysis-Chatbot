import streamlit as st
from transformers import pipeline
import random

# --- Load Model ---
emotion_pipeline = pipeline(
    "text-classification",
    model="j-hartmann/emotion-english-distilroberta-base",
    return_all_scores=False
)

def detect_emotion(text):
    result = emotion_pipeline(text)
    return result[0]['label']

# --- Generate Response Based on Emotion ---
def generate_response(text):
    emotion = detect_emotion(text)

    responses = {
        "joy": [
            "😀 That's awesome! Tell me more!",
            "🎉 Love hearing that! You sound happy!",
            "😄 Your joy is contagious! Keep it up!",
            "🌞 Great to hear! What else is going well?"
        ],
        "sadness": [
            "😭 I'm really sorry to hear that. I'm here for you.",
            "💙 That sounds tough. Want to talk more about it?",
            "😔 It's okay to feel down sometimes. I'm listening.",
            "🤗 You're not alone. Share if it helps."
        ],
        "anger": [
            "🤬 That sounds really frustrating. What happened?",
            "💢 I can sense you're upset. Let’s talk about it.",
            "😤 Take a deep breath. I'm here to listen.",
            "⚡ Vent it out! I'm all ears."
        ],
        "disgust": [
            "🤢 That doesn’t sound good. What made you feel that way?",
            "😖 Yikes, that’s awful. Want to share more?",
            "🙁 That situation must’ve been unpleasant.",
            "😷 I understand your reaction. Tell me more."
        ],
        "fear": [
            "😨 That sounds scary. Do you want to talk about it?",
            "😰 I'm here for you. What happened?",
            "😟 It’s okay to be afraid. You’re safe here.",
            "🫂 Let’s face this fear together."
        ],
        "surprise": [
            "😲 Whoa, that’s unexpected! What happened?",
            "😮 That caught you off guard, huh?",
            "😳 Wow! Tell me more!",
            "✨ That sounds surprising!"
        ],
        "neutral": [
            "😐 I'm here to chat. What’s on your mind?",
            "💬 Feel free to share anything.",
            "🤖 I’m always ready for a good convo.",
            "👋 How can I assist you today?"
        ]
    }

    return random.choice(responses.get(emotion, responses["neutral"])), emotion

# --- Streamlit Config ---
st.set_page_config(page_title="Aya Emotion Detection Chatbot", page_icon="💬")
st.markdown("""
    <style>
        .chat-bubble {
            padding: 12px 18px;
            border-radius: 18px;
            margin: 10px 0;
            display: inline-block;
            max-width: 75%;
            box-shadow: 0 4px 10px rgba(0, 0, 0, 0.15);
        }
        .user {
            background-color: #DCF8C6;
            color: #000;
            text-align: right;
            border-top-right-radius: 0;
            float: right;
            clear: both;
        }
        .bot {
            background-color: #F1F0F0;
            color: #000;
            text-align: left;
            border-top-left-radius: 0;
            float: left;
            clear: both;
        }
        .clear {
            clear: both;
        }
    </style>
""", unsafe_allow_html=True)

# --- Title ---
st.markdown("<h2 style='text-align: center;'>💬 Aya Emotion Detection Chatbot</h2>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center;'>Chat with Aya, and she’ll sense your emotions 🤖🧠</p>", unsafe_allow_html=True)

# --- Chat State ---
if 'chat_history' not in st.session_state:
    st.session_state.chat_history = []

# --- User Input ---
user_input = st.text_input("You:", placeholder="Type your message here...")

if user_input:
    response, emotion = generate_response(user_input)
    emoji_map = {
        "anger": "🤬",
        "disgust": "🤢",
        "fear": "😨",
        "joy": "😀",
        "neutral": "😐",
        "sadness": "😭",
        "surprise": "😲"
    }

    # Save both messages to chat history
    st.session_state.chat_history.append(("user", user_input))
    st.session_state.chat_history.append(("bot", f"{emoji_map.get(emotion, '💬')} ({emotion}) {response}"))

# --- Display Chat (Recent on Top) ---
for sender, msg in reversed(st.session_state.chat_history):
    bubble_class = "user" if sender == "user" else "bot"
    st.markdown(f"<div class='chat-bubble {bubble_class}'>{msg}</div><div class='clear'></div>", unsafe_allow_html=True)
