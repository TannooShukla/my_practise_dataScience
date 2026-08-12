import streamlit as st
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# =============================
# Build TF-IDF Vectorizer
# =============================
@st.cache_resource(show_spinner=True)
def build_vectorizer(df):
    vect = TfidfVectorizer(ngram_range=(1, 2), min_df=1)
    X = vect.fit_transform(df["text"].values)
    return vect, X

# =============================
# Rank Candidates
# =============================
@st.cache_data(show_spinner=False)
def rank_candidates(query_text, candidate_indices, _X_all, _vect):
    if len(candidate_indices) == 0:
        return []

    q = _vect.transform([query_text])
    sims = cosine_similarity(q, _X_all[candidate_indices]).ravel()

    order = sims.argsort()[::-1]
    ranked = [candidate_indices[i] for i in order]

    return ranked