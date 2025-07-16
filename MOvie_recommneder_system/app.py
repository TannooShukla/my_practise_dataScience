

import streamlit as st
import pickle
import pandas as pd
import requests

# ---------- Load Data ----------
movies = pickle.load(open('movies_list.pkl', 'rb'))
similarity = pickle.load(open('similarity.pkl', 'rb'))

# ---------- OMDb API ----------
OMDB_API_KEY = "45f527bd"

def fetch_poster(title):
    url = f"http://www.omdbapi.com/?t={title}&apikey={OMDB_API_KEY}"
    try:
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            poster_url = data.get('Poster')
            if poster_url and poster_url != "N/A":
                return poster_url
    except:
        pass
    # fallback
    return "https://via.placeholder.com/300x450?text=No+Poster"

# ---------- Recommendation Function ----------
def recommend(movie):
    if movie not in movies['title'].values:
        return [], []

    index = movies[movies['title'] == movie].index[0]
    distances = similarity[index]
    movie_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    recommended_movies = []
    recommended_posters = []
    for i in movie_list:
        movie_title = movies.iloc[i[0]]['title']
        recommended_movies.append(movie_title)
        recommended_posters.append(fetch_poster(movie_title))
    return recommended_movies, recommended_posters

# ---------- Streamlit App ----------
st.set_page_config(page_title="Movie Recommendation System", layout="wide")
st.title("🎬 Movie Recommendation System")
st.markdown("Get movie recommendations based on your favorite film.")

selected_movie = st.selectbox(
    "Choose a movie you like:",
    movies['title'].values
)

if st.button("Recommend"):
    names, posters = recommend(selected_movie)
    if names:
        cols = st.columns(5)
        for i in range(len(names)):
            with cols[i]:
                st.image(posters[i], use_container_width=True)
                st.markdown(f"**{names[i]}**")
    else:
        st.warning("No recommendations available.")
