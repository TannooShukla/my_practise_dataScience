import requests
from bs4 import BeautifulSoup
import streamlit as st

# =============================
# IMAGE FETCHING FROM PRODUCT URL
# =============================

@st.cache_data(show_spinner=False)
def fetch_image_from_url(url):
    """
    Automatically fetches product images using OpenGraph metadata.
    If an image is not found, a placeholder is returned.
    """
    try:
        r = requests.get(url, timeout=5, headers={"User-Agent": "Mozilla/5.0"})
        soup = BeautifulSoup(r.text, "html.parser")

        og = soup.find("meta", property="og:image")
        if og and og.get("content"):
            return og.get("content")

    except Exception:
        pass

    # ✅ Placeholder Image
    return "https://via.placeholder.com/300x300.png?text=No+Image"