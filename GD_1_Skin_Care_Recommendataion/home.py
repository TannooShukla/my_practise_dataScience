import streamlit as st
from utils import fetch_image_from_url

# =============================
# Home Page UI
# =============================

def home_ui(skin_types, concerns, product_types, price_bounds, df, vect, X):

    # Hero Section
    st.markdown(
        '<div class="hero"><div class="title">Find Your Perfect Skincare Match</div>'
        '<p class="subtitle">Discover products tailored to your skin type and needs.</p></div>',
        unsafe_allow_html=True,
    )

    st.write("")
    col1, col2 = st.columns([1.1, 1])

    # ---------------- LEFT CARD (User Inputs) ----------------
    with col1:
        st.markdown('<div class="card">', unsafe_allow_html=True)
        st.subheader("🎯 Personalized Recommendations")

        quiz_skin = st.session_state.get("quiz_skin_type")
        skin_default = skin_types.index(quiz_skin) if quiz_skin in skin_types else 0

        skin = st.selectbox("Skin Type", skin_types, index=skin_default)
        concern = st.selectbox("Skin Concern", concerns)
        ptype = st.selectbox("Product Type", product_types)

        pmin, pmax = price_bounds
        price_min, price_max = st.slider("Price Range", pmin, pmax, (pmin, pmax))

        st.markdown('<div class="button-primary">', unsafe_allow_html=True)
        go = st.button("Recommend Now", use_container_width=True)
        st.markdown('</div>', unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)

        # ---------------- RECOMMENDATIONS ----------------
        if go:
            from filters import filter_candidates
            from vectorizer import rank_candidates

            cand_df = filter_candidates(df, skin, concern, ptype, price_min, price_max)

            if len(cand_df) == 0:
                st.warning("No products found. Try changing filters.")
                return

            cand_idx = cand_df.index.tolist()
            query = f"{skin} {concern} {ptype}".lower()
            ranked_idx = rank_candidates(query, cand_idx, X, vect)

            top = ranked_idx[:12]

            st.subheader("Top Recommendations")
            cols = st.columns(3)

            for i, idx in enumerate(top):
                row = df.loc[idx]

                with cols[i % 3]:
                    st.markdown('<div class="card">', unsafe_allow_html=True)

                    # ✅ AUTO Image from product URL
                    img = fetch_image_from_url(row['product_url'])
                    st.image(img)

                    st.write(f"**{row['product_name']}**")
                    st.write(f"💲 Price: £{row['price_numeric']}")
                    st.caption(
                        f"Type: {row['product_type']} • Skin Match: {skin} • Concern Match: {concern}"
                    )

                    st.markdown('</div>', unsafe_allow_html=True)

    # Right side empty (for balance)
    with col2:
        st.write("")