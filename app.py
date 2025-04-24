import streamlit as st
from googletrans import Translator
import speech_recognition as sr
from gtts import gTTS
import tempfile
import os
import time

st.set_page_config(page_title="Real-Time Translator", layout="centered")

st.title("🌍 Real-Time Multilingual Translator")
st.write("Translate text or speech into multiple languages, with voice input and audio playback.")

translator = Translator()

# --- Language Options ---
languages = {
    "English": "en",
    "Hindi": "hi",
    "Spanish": "es",
    "French": "fr",
    "German": "de",
    "Chinese (Simplified)": "zh-cn",
    "Japanese": "ja",
    "Korean": "ko",
    "Arabic": "ar"
}

source_lang = st.selectbox("Source Language", list(languages.keys()))
target_lang = st.selectbox("Target Language", list(languages.keys()))

# --- Text Translation ---
input_text = st.text_area("Enter text to translate", "")

if st.button("Translate Text"):
    if input_text.strip() != "":
        translated = translator.translate(input_text, src=languages[source_lang], dest=languages[target_lang])
        st.success(f"**Translation:** {translated.text}")

        # Text-to-speech output
        tts = gTTS(translated.text, lang=languages[target_lang])
        with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as tmp:
            tts.save(tmp.name)
            st.audio(tmp.name, format="audio/mp3")
    else:
        st.warning("Please enter some text.")

st.markdown("---")

# --- Voice Input and Translation ---
st.header("🎙️ Speak and Translate")

if st.button("Start Recording"):
    recognizer = sr.Recognizer()
    mic = sr.Microphone()

    with mic as source:
        st.info("Listening... Speak now!")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source, phrase_time_limit=5)

    try:
        st.success("Recognizing speech...")
        voice_text = recognizer.recognize_google(audio, language=languages[source_lang])
        st.write(f"**You said:** {voice_text}")

        translated_voice = translator.translate(voice_text, src=languages[source_lang], dest=languages[target_lang])
        st.success(f"**Translation:** {translated_voice.text}")

        # Voice Output
        tts_voice = gTTS(translated_voice.text, lang=languages[target_lang])
        with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as tmp2:
            tts_voice.save(tmp2.name)
            st.audio(tmp2.name, format="audio/mp3")

    except sr.UnknownValueError:
        st.error("Sorry, could not understand the audio.")
    except sr.RequestError as e:
        st.error(f"Could not request results; {e}")
