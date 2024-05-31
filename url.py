import pyshorteners
import pyperclip
import streamlit as st

st.title("URL SHORTENER")
st.sidebar.header("Options")
url = st.text_input("Enter URL")

if st.button("Generate Short Url"):
    if url:
        url_add = pyshorteners.Shortener().tinyurl.short(url)
        st.session_state.url_add = url_add  # Store the shortened URL in session_state
        st.success("Shortened URL: " + url_add)
    else:
        st.warning("Please enter a URL to shorten")

if st.button("Copy"):
    url_add = st.session_state.get("url_add", "")
    if url_add:
        pyperclip.copy(url_add)
        st.success("URL copied to clipboard")
    else:
        st.warning("No URL to copy")
