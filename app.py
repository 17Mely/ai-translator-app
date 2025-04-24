import streamlit as st
from googletrans import Translator
from gtts import gTTS
import tempfile
import os

# Initialize translator
translator = Translator()

# Set Streamlit page config
st.set_page_config(page_title="Real-Time Translator", layout="centered")
st.title("🌍 Real-Time Text Translator with Voice Output")

# Language options
LANGUAGES = {
    'English': 'en',
    'Hindi': 'hi',
    'Spanish': 'es',
    'French': 'fr',
    'German': 'de',
    'Chinese (Simplified)': 'zh-cn',
    'Japanese': 'ja',
    'Korean': 'ko',
    'Arabic': 'ar'
}

col1, col2 = st.columns(2)
with col1:
    source_lang = st.selectbox("Select source language", list(LANGUAGES.keys()), index=0)
with col2:
    target_lang = st.selectbox("Select target language", list(LANGUAGES.keys()), index=1)

text_input = st.text_area("Enter text to translate:")

if st.button("Translate"):
    if text_input.strip() != "":
        translated = translator.translate(text_input, src=LANGUAGES[source_lang], dest=LANGUAGES[target_lang])
        st.success(f"Translated Text: {translated.text}")

        # Text-to-speech using gTTS
        tts = gTTS(translated.text, lang=LANGUAGES[target_lang])
        with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as tmpfile:
            tts.save(tmpfile.name)
            st.audio(tmpfile.name, format='audio/mp3')
    else:
        st.warning("Please enter text to translate.")
