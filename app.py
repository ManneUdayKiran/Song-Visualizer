import streamlit as st
import lyricsgenius
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import os
from dotenv import load_dotenv
from streamlit_lottie import st_lottie
import requests

load_dotenv()

# Set Genius Access Token
GENIUS_ACCESS_TOKEN = os.getenv("GENIUS_ACCESS_TOKEN")

if not GENIUS_ACCESS_TOKEN:
    st.error("❌ Genius API token not found! Please create a .env file with GENIUS_ACCESS_TOKEN.")
    st.stop()

# ✅ Now it's safe to initialize Genius
genius = lyricsgenius.Genius(GENIUS_ACCESS_TOKEN)
# Page setup
st.set_page_config(page_title="🎤 Taylor Swift Lyrics Visualizer", layout="centered")

st.title("🎤 Sing with Streamlit")

st.caption("Built with ❤️ for Swifties and Pythonistas")

# Input field
song_title = st.text_input("Enter a Taylor Swift song title:", placeholder="e.g., Love Story")


st.subheader("Taylor Swift Lyrics Visualizer")

# Fetch lyrics
if song_title:
    with st.spinner("Fetching lyrics..."):
        try:
            song = genius.search_song(song_title, "Taylor Swift")
            if song:
                lyrics = song.lyrics
                # Clean lyrics (remove metadata like chorus, verse etc.)
                cleaned_lyrics = "\n".join([line for line in lyrics.split("\n") if "[" not in line and "]" not in line])
                
                st.success("Lyrics loaded!")
                st.text_area("📜 Lyrics", cleaned_lyrics, height=300)

                # Generate word cloud
                st.subheader("☁️ Word Cloud")
                wordcloud = WordCloud(width=800, height=400, background_color="white").generate(cleaned_lyrics)

                fig, ax = plt.subplots(figsize=(10, 5))
                ax.imshow(wordcloud, interpolation="bilinear")
                ax.axis("off")
                st.pyplot(fig)
            else:
                st.error("Couldn't find that song. Try another one!")
        except Exception as e:
            st.error(f"Error: {e}")
# Load a music-themed Lottie animation

