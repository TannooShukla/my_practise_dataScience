import streamlit as st
from data_loader import load_data, get_dropdown_values
from vectorizer import build_vectorizer
from filters import filter_candidates
from quiz import skin_quiz_ui
from home import home_ui
from about import about_ui
from pathlib import Path

# =============================
# App Config
# =============================
st.set_page_config(
    page_title="SkinWise — Smart Skincare Recommendations",
    page_icon="🧴",
    layout="wide",
)


# ✅✅✅ NAVBAR (INLINE + FIXED VERSION)
def navbar():

    # ✅ Navbar Styling
    st.markdown("""
        <style>
        .navbar {
            position: sticky;
            top: 0;
            z-index: 9999;
            width: 100%;
            background: linear-gradient(90deg, #f8cdda, #fbc2eb);
            padding: 14px 0;
            display: flex;
            justify-content: center;
            align-items: center;
            gap: 30px;
            box-shadow: 0 3px 10px rgba(0,0,0,0.15);
        }
        .nav-logo {
            position: absolute;
            left: 25px;
            font-size: 26px;
            font-weight: 800;
            color: #d63384;
        }
        .nav-btn {
            background: none;
            border: none;
            font-size: 18px;
            font-weight: 600;
            color: #444;
            padding: 8px 20px;
            border-radius: 8px;
            cursor: pointer;
            transition: all 0.3s ease;
        }
        .nav-btn:hover {
            background: rgba(255,255,255,0.6);
            transform: translateY(-3px);
            color: #d63384;
        }
        .active-btn {
            background: white !important;
            color: #d63384 !important;
            box-shadow: 0 2px 8px rgba(0,0,0,0.2);
        }
        </style>
    """, unsafe_allow_html=True)

    # ✅ Navbar Header
    st.markdown("<div class='navbar'><div class='nav-logo'>SkinWise</div></div>", unsafe_allow_html=True)

    # ✅ Navbar Buttons in 3 columns
    col1, col2, col3 = st.columns([1,1,1], gap="small")

    # ✅ HOME button
    with col1:
        btn_class = "active-btn" if st.session_state["page"] == "Home" else "nav-btn"
        if st.button("Home", key="nav_home", help="Go to Home"):
            st.session_state["page"] = "Home"
            st.experimental_rerun()
        st.markdown(f"<span class='{btn_class}'></span>", unsafe_allow_html=True)

    # ✅ SKIN QUIZ button
    with col2:
        btn_class = "active-btn" if st.session_state["page"] == "Skin Quiz" else "nav-btn"
        if st.button("Skin Quiz", key="nav_quiz", help="Take the Skin Quiz"):
            st.session_state["page"] = "Skin Quiz"
            st.experimental_rerun()
        st.markdown(f"<span class='{btn_class}'></span>", unsafe_allow_html=True)

    # ✅ ABOUT button
    with col3:
        btn_class = "active-btn" if st.session_state["page"] == "About" else "nav-btn"
        if st.button("About", key="nav_about", help="About SkinWise"):
            st.session_state["page"] = "About"
            st.experimental_rerun()
        st.markdown(f"<span class='{btn_class}'></span>", unsafe_allow_html=True)


# =============================
# Main
# =============================
def main():
    DEFAULT_DATA_PATH = Path("skin_type_concer.csv")

    df = load_data(DEFAULT_DATA_PATH)
    skin_types, concerns, product_types, price_bounds = get_dropdown_values(df)
    vect, X = build_vectorizer(df)

    # ✅ Ensure session_state has page
    if "page" not in st.session_state:
        st.session_state["page"] = "Home"

    # ✅ Show the Top Navbar
    navbar()

    # ✅ ROUTING
    page = st.session_state["page"]

    if page == "Home":
        home_ui(skin_types, concerns, product_types, price_bounds, df, vect, X)

    elif page == "Skin Quiz":
        skin_quiz_ui()

    elif page == "About":
        about_ui()


if __name__ == "__main__":
    main()
