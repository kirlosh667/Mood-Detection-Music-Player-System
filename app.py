import streamlit as st
import random
import os
from deepface import DeepFace
import pygame
import cv2
from PIL import Image
import numpy as np

# Initialize pygame for music
pygame.mixer.init()

# --- STREAMLIT PAGE CONFIG ---
st.set_page_config(page_title="Mood-Based Music Player", page_icon="🎧", layout="centered")

st.markdown("<h1 style='text-align:center; color:#00C4FF;'>🎵 Mood-Based Music Player 🎵</h1>", unsafe_allow_html=True)
st.markdown("---")

# --- IMAGE INPUT ---
st.subheader("📸 Capture or Upload Your Image")

uploaded_file = st.file_uploader("Upload your photo", type=["jpg", "jpeg", "png"])

if st.button("📷 Use Webcam"):
    cap = cv2.VideoCapture(0)
    ret, frame = cap.read()
    if ret:
        cv2.imwrite("captured.jpg", frame)
        uploaded_file = "captured.jpg"
    cap.release()
    cv2.destroyAllWindows()

# --- MOOD DETECTION ---
if uploaded_file:
    st.image(uploaded_file, caption="Your Uploaded Image", use_column_width=True)
    st.markdown("⏳ *Detecting mood... please wait...*")

    try:
        # Detect mood using DeepFace
        result = DeepFace.analyze(img_path=uploaded_file, actions=['emotion'], enforce_detection=False)
        mood = result[0]['dominant_emotion'].lower()

        # Mood emojis
        emojis = {
            "happy": "😄",
            "sad": "😢",
            "angry": "😡",
            "surprise": "😲",
            "fear": "😨",
            "disgust": "🤢",
            "neutral": "😐"
        }

        st.success(f"### {emojis.get(mood, '🙂')} Your Mood: **{mood.upper()}**")

        # --- MUSIC SELECTION ---
        folder_path = os.path.join("music", mood)
        if os.path.exists(folder_path) and os.listdir(folder_path):
            songs = [os.path.join(folder_path, s) for s in os.listdir(folder_path) if s.endswith(".mp3")]
            current_song = st.session_state.get("current_song", random.choice(songs))
            if "paused" not in st.session_state:
                st.session_state.paused = False

            st.write(f"🎶 Now Playing: **{os.path.basename(current_song)}**")

            # --- BUTTONS ---
            col1, col2, col3 = st.columns(3)
            with col1:
                if st.button("⏸️ Pause"):
                    pygame.mixer.music.pause()
                    st.session_state.paused = True
            with col2:
                if st.button("▶️ Play"):
                    if st.session_state.paused:
                        pygame.mixer.music.unpause()
                    else:
                        pygame.mixer.music.load(current_song)
                        pygame.mixer.music.play()
                    st.session_state.paused = False
            with col3:
                if st.button("⏭️ Next Song"):
                    pygame.mixer.music.stop()
                    next_song = random.choice(songs)
                    pygame.mixer.music.load(next_song)
                    pygame.mixer.music.play()
                    st.session_state.current_song = next_song
                    st.experimental_rerun()

        else:
            st.error("❌ No songs found for this mood. Please add songs to the respective folder.")
    except Exception as e:
        st.error(f"⚠️ Error analyzing image: {e}")
