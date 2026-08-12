import streamlit as st

# =============================
# Skin Quiz Module
# =============================

def skin_quiz_ui():
    st.header("🧪 Skin Type Quiz")
    st.write("Answer a few quick questions — we'll detect your skin type.")

    q1 = st.radio(
        "How does your skin feel after washing?",
        ["Tight & dry", "Normal", "Oily", "Dry cheeks, oily T-zone"],
        index=None
    )

    q2 = st.radio(
        "How shiny does your face get by midday?",
        ["Never", "Sometimes", "Often", "Only T-zone"],
        index=None
    )

    q3 = st.radio(
        "Do you notice flakiness?",
        ["Yes", "No", "Sometimes"],
        index=None
    )

    q4 = st.radio(
        "How visible are your pores?",
        ["Very small", "Normal", "Large", "Large on T-zone"],
        index=None
    )

    if st.button("Get My Skin Type", use_container_width=True):
        if None in (q1, q2, q3, q4):
            st.warning("Please answer all questions.")
            return

        dry = oily = combo = normal = sens = 0

        if q1 == "Tight & dry": dry += 2
        if q1 == "Oily": oily += 2
        if q1 == "Dry cheeks, oily T-zone": combo += 2
        if q1 == "Normal": normal += 2

        if q2 == "Never": dry += 1
        if q2 == "Often": oily += 2
        if q2 == "Only T-zone": combo += 2

        if q3 == "Yes": dry += 1; sens += 1
        if q3 == "Sometimes": sens += 1

        if q4 == "Very small": dry += 1
        if q4 == "Large": oily += 2
        if q4 == "Large on T-zone": combo += 2

        scores = {
            "Dry": dry,
            "Oily": oily,
            "Combination": combo,
            "Normal": normal,
            "Sensitive": sens,
        }

        skin = max(scores, key=scores.get)
        st.success(f"Your skin type is: **{skin}**")

        st.session_state["quiz_skin_type"] = skin
