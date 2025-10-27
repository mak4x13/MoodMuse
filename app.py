import streamlit as st
import random
from datetime import datetime

# --- Mood data ---
MOODS = {
    "Happy": {
        "color": "#FFF9C4",
        "emoji": "😄",
        "quotes": [
            "Happiness is not by chance, but by choice.",
            "Let your smile change the world.",
            "Joy is contagious — pass it on!"
        ],
        "sound": "https://actions.google.com/sounds/v1/ambiences/birds_in_forest.ogg"
    },
    "Sad": {
        "color": "#B3E5FC",
        "emoji": "😢",
        "quotes": [
            "It’s okay to feel what you’re feeling.",
            "Tears are words the heart can’t express.",
            "Storms make trees take deeper roots."
        ],
        "sound": "https://actions.google.com/sounds/v1/water/stream.ogg"
    },
    "Calm": {
        "color": "#C8E6C9",
        "emoji": "🌿",
        "quotes": [
            "Peace begins with a deep breath.",
            "Stillness speaks louder than noise.",
            "You are exactly where you need to be."
        ],
        "sound": "https://actions.google.com/sounds/v1/water/flowing_water.ogg"
    },
    "Creative": {
        "color": "#F3E5F5",
        "emoji": "🎨",
        "quotes": [
            "Creativity is intelligence having fun.",
            "Every artist was first an amateur.",
            "Your imagination can build worlds."
        ],
        "sound": "https://actions.google.com/sounds/v1/cartoon/cartoon_boing.ogg"
    },
    "Stressed": {
        "color": "#FFCDD2",
        "emoji": "😖",
        "quotes": [
            "Breathe. This too shall pass.",
            "Relax — even the sky takes breaks.",
            "Take one step at a time."
        ],
        "sound": "https://actions.google.com/sounds/v1/ambiences/beach.ogg"
    }
}

# --- Streamlit UI ---
st.set_page_config(page_title="MoodMuse", page_icon="🎭", layout="centered")

st.markdown(
    "<h1 style='text-align:center; color:#4A148C;'>🎭 MoodMuse</h1>"
    "<p style='text-align:center;'>Discover a color, quote, and vibe to match your mood ✨</p>",
    unsafe_allow_html=True
)

mood = st.selectbox("Select your mood:", list(MOODS.keys()))
if mood:
    mood_data = MOODS[mood]
    color = mood_data["color"]
    emoji = mood_data["emoji"]
    quote = random.choice(mood_data["quotes"])

    # --- Apply background color ---
    st.markdown(
        f"""
        <style>
        .stApp {{
            background-color: {color};
            transition: background-color 1s ease;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

    st.markdown(f"<h2 style='text-align:center;'>{emoji} {mood} {emoji}</h2>", unsafe_allow_html=True)
    st.markdown(f"<h3 style='text-align:center; color:#4A148C;'>“{quote}”</h3>", unsafe_allow_html=True)
    st.markdown(f"<p style='text-align:center; color:#616161;'>Mood logged at {datetime.now().strftime('%I:%M %p')}</p>", unsafe_allow_html=True)

    # --- Optional: Play sound ---
    st.audio(mood_data["sound"])

st.markdown("---")
st.markdown("<p style='text-align:center; color:gray;'>Made with ❤️ using Streamlit</p>", unsafe_allow_html=True)
