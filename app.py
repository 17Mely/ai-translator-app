import streamlit as st
from googletrans import Translator
import speech_recognition as sr
from gtts import gTTS
import os
import tempfile

# Set up the page
st.set_page_config(page_title="Real-Time Translator", layout="centered")
st.title("🌍 Real-Time Multilingual Translator")

# Initialize translator
translator = Translator()

# Supported languages
LANGUAGES = {
    'English': 'en',
    'Spanish': 'es',
    'French': 'fr',
    'German': 'de',
    'Hindi': 'hi',
    'Chinese (Simplified)': 'zh-cn',
    'Japanese': 'ja',
    'Korean': 'ko',
    'Arabic': 'ar'
}

# Language selection
col1, col2 = st.columns(2)
with col1:
    source_lang = st.selectbox("Select input language", list(LANGUAGES.keys()), index=0)
with col2:
    target_lang = st.selectbox("Select target language", list(LANGUAGES.keys()), index=1)

# Input text box
text_input = st.text_area("Enter text to translate")

# Translate button
if st.button("Translate Text"):
    if text_input.strip():
        translated = translator.translate(text_input, src=LANGUAGES[source_lang], dest=LANGUAGES[target_lang])
        st.success(f"Translated Text: {translated.text}")
        # Text-to-speech for translated output
        tts = gTTS(translated.text, lang=LANGUAGES[target_lang])
        with tempfile.NamedTemporaryFile(delete=True, suffix=".mp3") as tmpfile:
            tts.save(tmpfile.name)
            audio_file = open(tmpfile.name, 'rb')
            st.audio(audio_file.read(), format='audio/mp3')
    else:
        st.warning("Please enter some text to translate.")

# Speech input and translate
st.markdown("---")
st.markdown("🎙️ Or press below to speak:")
if st.button("Record and Translate"):
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        st.info("Listening... Speak now.")
        audio = recognizer.listen(source, phrase_time_limit=5)
    try:
        spoken_text = recognizer.recognize_google(audio, language=LANGUAGES[source_lang])
        st.write(f"You said: {spoken_text}")
        translated = translator.translate(spoken_text, src=LANGUAGES[source_lang], dest=LANGUAGES[target_lang])
        st.success(f"Translated Speech: {translated.text}")
        # Play audio of translated speech
        tts = gTTS(translated.text, lang=LANGUAGES[target_lang])
        with tempfile.NamedTemporaryFile(delete=True, suffix=".mp3") as tmpfile:
            tts.save(tmpfile.name)
            audio_file = open(tmpfile.name, 'rb')
            st.audio(audio_file.read(), format='audio/mp3')
    except Exception as e:
        st.error(f"Error recognizing speech: {str(e)}")
