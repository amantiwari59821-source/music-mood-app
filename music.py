import streamlit as st
import random

# Songs database
songs = {
    "happy": [
        "https://youtu.be/kw4tT7SCmaY?feature=shared",
        "https://youtu.be/X4RFNTTUizY?feature=shared",
        "https://youtu.be/d7AqPH-LgmI?feature=shared",,
        "https://youtu.be/eM8Mjuq4MwQ?feature=shared"
    ],
    "sad": [
        "https://youtu.be/kp-Bqr1Gtyw?feature=shared",
        "https://youtu.be/x-wCUOYxYH4?feature=shared",
        "https://youtu.be/7iyBBAfd_X8?feature=shared",
        "https://youtu.be/AX6OrbgS8lI?feature=shared"
    ],
    "study": [
       "https://youtu.be/GiVxUKbIy0w?feature=shared",
       "https://youtu.be/nHvkz0dPHNM?feature=shared",
       "https://youtu.be/vB0V3iCSzQw?feature=shared",
       "https://youtu.be/tYKrORILFOg?feature=shared"
    ]
}

# Title
st.title("🎵 Mood-Based Music Recommender 🎵")

# Mood selection
mood = st.selectbox("Choose your mood:", list(songs.keys()))

# Recommend button
if st.button("Recommend Song"):
    choice = random.choice(songs[mood])
    st.success(f"👉 Recommended Song for **{mood.capitalize()}** mood:")
    
    # Clickable link (opens in YouTube)
    st.markdown(f"[🎶 Play Song]({choice})", unsafe_allow_html=True)
