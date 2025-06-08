# 🎙️ Accent Detection and Audio Analysis from YouTube & Uploaded Files

This project enables automated audio transcription and accent classification from audio or video inputs. Built with Streamlit for interactivity, Whisper for transcription, and a fine-tuned Hugging Face model for accent detection, the application supports both direct file uploads and YouTube URLs.

---

## 🚀 Features

- 📥 **Flexible Input Options**  
  - Upload local audio/video files (`.mp3`, `.wav`, `.m4a`, `.mp4`)
  - Paste YouTube links to extract and analyze audio automatically

- 🧠 **AI-Powered Transcription**  
  - Uses OpenAI's [Whisper](https://github.com/openai/whisper) for accurate multilingual transcription  
  - Displays detected language and transcript in real time

- 🌍 **Accent Classification**  
  - English accent classification using a Hugging Face model (`dima806/english_accents_classification`)  
  - Predicts accent and visualizes confidence scores via Plotly bar charts

- 🎧 **Streamlined Audio Extraction**  
  - Automatic audio extraction using `yt_dlp` and `moviepy`  
  - Supports conversion from video to `.wav` or `.mp3`

- ⚡ **Interactive Web Interface**  
  - Built using Streamlit with modern UI/UX best practices

---

## 🛠️ Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/your-org/accent-detector.git
cd accent-detector
