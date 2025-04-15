import streamlit as st
from googletrans import Translator

st.set_page_config(page_title="Translator App", page_icon="🌐")
st.title("🌐 AI-Powered Translator")

st.markdown("Translate text in real-time across languages using AI")

text = st.text_area("Enter text you want to translate:")

languages = {
    "English": "en",
    "French": "fr",
    "Spanish": "es",
    "Hindi": "hi",
    "German": "de",
    "Chinese (Simplified)": "zh-cn"
}

src_lang = st.selectbox("Select the source language:", ["Auto Detect"] + list(languages.keys()))
target_lang = st.selectbox("Select the target language:", list(languages.keys()))

if st.button("Translate"):
    if text:
        translator = Translator()
        src_code = languages.get(src_lang) if src_lang != "Auto Detect" else None
        dest_code = languages.get(target_lang)

        try:
            translation = translator.translate(text, src=src_code, dest=dest_code)
            st.success(f"**Translated Text:**\n\n{translation.text}")
        except Exception as e:
            st.error(f"Translation failed: {e}")
    else:
        st.warning("Please enter text to translate.")
