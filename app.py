import streamlit as st
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import os
from dotenv import load_dotenv
import requests

# Load API key
load_dotenv()
API_KEY = os.getenv("API_NINJAS_KEY")

# Function to fetch lyrics
import urllib.parse

def get_lyrics(song_title: str, artist: str = "Taylor Swift"):
    base_url = f"https://api.lyrics.ovh/v1/{artist}/{song_title}"
    response = requests.get(base_url)
    if response.status_code == 200:
        return response.json().get("lyrics", "")
    else:
        st.error(f"Error {response.status_code}: Could not fetch lyrics.")
        return ""



# Streamlit UI
st.set_page_config(page_title="🎤 Taylor Swift Lyrics Visualizer")
st.title("🎤 Sing with Streamlit")
st.subheader("Taylor Swift Lyrics Visualizer")

song_title = st.text_input("Enter a Taylor Swift song title:", placeholder="e.g., Love Story")

if song_title:
    with st.spinner("Fetching lyrics..."):
        lyrics = get_lyrics(song_title)
        if lyrics:
            st.success("Lyrics loaded!")
            st.text_area("📜 Lyrics", lyrics, height=300)

            # Word cloud
            st.subheader("☁️ Word Cloud")
            wordcloud = WordCloud(width=800, height=400, background_color="white").generate(lyrics)
            fig, ax = plt.subplots(figsize=(10, 5))
            ax.imshow(wordcloud, interpolation="bilinear")
            ax.axis("off")
            st.pyplot(fig)
        else:
            st.warning("No lyrics found. Try another song.")
