import streamlit as st
import random
from datetime import datetime, timedelta, timezone

# --- Mood data ---
MOODS = {
    "Happy": {
        "color": "#FFF8E1",
        "emoji": "😄",
        "quotes": [
            "Happiness is not by chance, but by choice.",
            "Let your smile change the world.",
            "Joy is contagious — pass it on!"
        ],
        "sound": "https://cdn.pixabay.com/download/audio/2021/08/08/audio_37bce610c2.mp3?filename=birds-forest-ambience-6101.mp3"
    },
    "Sad": {
        "color": "#BBDEFB",
        "emoji": "😢",
        "quotes": [
            "It’s okay to feel what you’re feeling.",
            "Tears are words the heart can’t express.",
            "Storms make trees take deeper roots."
        ],
        "sound": "https://cdn.pixabay.com/download/audio/2021/09/01/audio_21f4f272f8.mp3?filename=rain-ambient-110624.mp3"
    },
    "Calm": {
        "color": "#E8F5E9",
        "emoji": "🌿",
        "quotes": [
            "Peace begins with a deep breath.",
            "Stillness speaks louder than noise.",
            "You are exactly where you need to be."
        ],
        "sound": "https://cdn.pixabay.com/download/audio/2021/09/02/audio_98b00d16c5.mp3?filename=water-stream-ambient-110682.mp3"
    },
    "Creative": {
        "color": "#F3E5F5",
        "emoji": "🎨",
        "quotes": [
            "Creativity is intelligence having fun.",
            "Every artist was first an amateur.",
            "Your imagination can build worlds."
        ],
        "sound": "https://cdn.pixabay.com/download/audio/2021/09/09/audio_1e87921a91.mp3?filename=soft-piano-ambient-110980.mp3"
    },
    "Stressed": {
        "color": "#FFEBEE",
        "emoji": "😖",
        "quotes": [
            "Breathe. This too shall pass.",
            "Relax — even the sky takes breaks.",
            "Take one step at a time."
        ],
        "sound": "https://cdn.pixabay.com/download/audio/2021/08/08/audio_1d1a45efb8.mp3?filename=waves-beach-ambience-6071.mp3"
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

    # --- Apply background color with smooth transition ---
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

    # --- Display mood content ---
    st.markdown(f"<h2 style='text-align:center;'>{emoji} {mood} {emoji}</h2>", unsafe_allow_html=True)
    st.markdown(f"<h3 style='text-align:center; color:#4A148C;'>“{quote}”</h3>", unsafe_allow_html=True)

    # --- Local timezone (UTC+5 for Pakistan) ---
    now_pk = datetime.now(timezone(timedelta(hours=5)))
    st.markdown(f"<p style='text-align:center; color:#616161;'>Mood logged at {now_pk.strftime('%I:%M %p')}</p>", unsafe_allow_html=True)

    # --- Auto-play sound ---
    st.markdown(
        f"""
        <audio autoplay loop>
            <source src="{mood_data['sound']}" type="audio/mpeg">
        </audio>
        """,
        unsafe_allow_html=True
    )

st.markdown("---")
st.markdown("<p style='text-align:center; color:gray;'>Made with ❤️ using Streamlit</p>", unsafe_allow_html=True)
