
# 🎤 Sing with Streamlit: Taylor Swift Lyrics Visualizer

Are you a Swiftie and a Pythonista? This interactive web app blends your love for Taylor Swift's lyrics with the magic of data visualization — all powered by Python and Streamlit!

## ✨ Features

- 🔎 Search any **Taylor Swift** song
- 🎶 Fetch **real-time lyrics** via the **Genius API**
- 📜 View lyrics in a scrollable textbox
- ☁️ Generate a **word cloud** from lyrics

---

## 🛠 Tech Stack

- [Streamlit](https://streamlit.io/)
- [LyricsGenius API](https://genius.com/developers)
- [WordCloud](https://github.com/amueller/word_cloud)
- [Matplotlib](https://matplotlib.org/)
- [Streamlit-Lottie](https://github.com/andfanilo/streamlit-lottie)
- [Python-Dotenv](https://pypi.org/project/python-dotenv/)

---

## 📦 Setup Instructions

1. **Clone the repo**

```bash
git clone https://github.com/your-username/song-visualizer.git
cd song-visualizer
````

2. **Install dependencies**

```bash
pip install -r requirements.txt
```

3. **Get your Genius API token**

* Visit: [https://genius.com/developers](https://genius.com/developers)
* Generate a **Client Access Token**

4. **Add your token to a `.env` file**

```
GENIUS_ACCESS_TOKEN=your_genius_token_here
```

5. **Run the app**

```bash
streamlit run app.py
```

---

## 🚀 Live Demo

> \[Coming Soon – Deploy to Streamlit Cloud or Hugging Face Spaces]



---

## 🧠 Describe Your Approach

I used Streamlit to create a responsive UI for lyrics input, fetched real-time data using the Genius API with `lyricsgenius`, and visualized the lyrics via a dynamic word cloud. I enhanced the experience using Lottie animations and seasonal themes for Swiftie-inspired flair.

---

## 📄 License

MIT © \[Your Name]

```

Let me know if you'd like [screenshot placeholders](f), a [deploy button for Streamlit Cloud](f), or to turn this into a [multi-page Streamlit app](f).
```
