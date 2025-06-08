# 🎙️ Accent Detection and Audio Analysis from YouTube & Uploaded Files

A powerful Streamlit-based application for extracting audio from uploaded files or YouTube URLs, transcribing speech using Whisper, and classifying English accents using a transformer-based classifier.

---

## 🚀 Features

- 📥 **Dual Input Modes**  
  - Upload audio/video files (`.mp3`, `.wav`, `.m4a`, `.mp4`)  
  - Paste YouTube URLs for automatic download and analysis

- 🧠 **Speech-to-Text via Whisper**  
  - High-quality transcription using [OpenAI Whisper](https://github.com/openai/whisper)  
  - Multilingual support with accurate language detection

- 🌍 **Accent Detection**  
  - Uses `dima806/english_accents_classification` model from Hugging Face  
  - Predicts and visualizes English accents with confidence scores

- 📊 **Interactive Visualization**  
  - Clean and intuitive UI using Streamlit  
  - Dynamic Plotly charts for accent prediction results

---

## ⚡ Performance Considerations

> ✅ **Recommended for Local Use:**  
- **[Groq](https://groq.com/)** or **OpenAI Whisper (via local models)** are recommended for fast, cost-effective, and scalable transcription on personal devices.  
- **Local inference with Whisper** ensures data privacy and works well for non-streaming applications.

> 🌐 **Cloud-First or Streaming Use:**  
- **Google Gemini Audio Input** offers superior real-time performance in multi-speaker scenarios and conversational audio. Ideal for production-grade pipelines involving rich multimodal context or conversational nuance.

---

## 🛠️ Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/your-org/accent-detector.git
cd accent-detector
