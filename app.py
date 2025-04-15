import streamlit as st

st.set_page_config(page_title="Translator App", page_icon="🌐")
st.title("🌐 AI-Powered Translator")

st.markdown("Translate text in real-time across languages using AI!")

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
    st.write("🔄 Translating... (feature coming tomorrow!)")
