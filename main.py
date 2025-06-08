import os
import re
import tempfile
from typing import Optional

import streamlit as st
import yt_dlp
import librosa
import whisper
import plotly.graph_objects as go
from transformers import pipeline


@st.cache_resource(show_spinner=False)
def load_models():
    whisper_model = whisper.load_model("base")
    accent_model = pipeline("audio-classification", model="dima806/english_accents_classification")
    return whisper_model, accent_model


def sanitize_filename(filename: str) -> str:
    return re.sub(r"[^\w\-_\. ]", "_", filename)


def download_audio(url: str) -> Optional[str]:
    temp_dir = tempfile.mkdtemp()
    ydl_opts = {
        "format": "bestaudio/best",
        "outtmpl": os.path.join(temp_dir, "%(title)s.%(ext)s"),
        "postprocessors": [{
            "key": "FFmpegExtractAudio",
            "preferredcodec": "wav",
            "preferredquality": "192",
        }],
        "quiet": True,
    }
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=True)
            title = sanitize_filename(info.get("title", "audio"))
            wav_path = os.path.join(temp_dir, f"{title}.wav")
            if not os.path.exists(wav_path):
                for file in os.listdir(temp_dir):
                    if file.endswith(".wav"):
                        return os.path.join(temp_dir, file)
            return wav_path
    except Exception as e:
        st.error(f"❌ Error downloading audio: {str(e)}")
        return None


def classify_accent(audio_path: str, model) -> list:
    audio, _ = librosa.load(audio_path, sr=16000)
    return model(audio)


def plot_accent_scores(scores):
    labels = [s['label'].capitalize() for s in scores]
    values = [s['score'] * 100 for s in scores]
    fig = go.Figure([go.Bar(x=labels, y=values, marker_color='mediumturquoise')])
    fig.update_layout(
        title="🌍 Accent Prediction Scores",
        xaxis_title="Accent",
        yaxis_title="Confidence (%)",
        template="plotly_white"
    )
    return fig


def main():
    st.set_page_config(page_title="Accent Detector", page_icon="🎙️", layout="centered")
    st.markdown("<h1 style='text-align: center;'>🎙️ Accent Detector</h1>", unsafe_allow_html=True)
    st.caption("🔍 Detect accents from English audio using Whisper + Transformers")

    whisper_model, accent_model = load_models()
    input_method = st.selectbox("Select Input Type", ["Upload File", "YouTube URL"])
    user_input = None

    if input_method == "Upload File":
        user_input = st.file_uploader("📎 Upload audio or video file", type=["mp4", "mp3", "wav", "m4a"])
    else:
        user_input = st.text_input("🔗 Enter YouTube URL", placeholder="https://youtube.com/...")

    if st.button("🔍 Analyze Accent"):
        audio_path = None
        title = "Uploaded Audio"

        if input_method == "Upload File" and user_input:
            temp_dir = tempfile.mkdtemp()
            audio_path = os.path.join(temp_dir, user_input.name)
            with open(audio_path, "wb") as f:
                f.write(user_input.read())
            title = user_input.name
        elif input_method == "YouTube URL" and user_input:
            audio_path = download_audio(user_input)
            title = "YouTube Audio"
        else:
            st.warning("⚠️ Please upload a file or enter a valid URL.")
            return

        if not audio_path:
            st.error("❌ Failed to retrieve audio.")
            return

        st.audio(audio_path)
        st.info("🔄 Transcribing with Whisper...")
        result = whisper_model.transcribe(audio_path)
        transcript = result.get("text", "")
        language = result.get("language", "unknown")

        st.subheader("📜 Transcript")
        st.write(transcript)
        st.write(f"🌐 Detected Language: `{language.upper()}`")

        if language == "en":
            st.info("🔄 Classifying accent...")
            scores = classify_accent(audio_path, accent_model)
            predicted = scores[0]['label'].capitalize()
            confidence = scores[0]['score'] * 100

            st.subheader("🌍 Predicted Accent")
            st.success(f"**{predicted}** ({confidence:.2f}% confidence)")

            st.plotly_chart(plot_accent_scores(scores), use_container_width=True)
        else:
            st.warning("⚠️ This app only supports English speech.")

        os.remove(audio_path)


if __name__ == "__main__":
    main()
