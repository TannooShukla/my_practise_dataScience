import streamlit as st

def about_ui():
    st.markdown(
        """
        <div style='text-align:center; margin-top:40px;'>
            <h1>About SkinWise</h1>
            <p style='font-size:18px; opacity:0.8;'>Your personalized skincare companion for flawless, healthy skin</p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.write("\n")

    col1, col2 = st.columns([1, 1.3])

    with col2:
        st.markdown(
            """
            ### **Our Mission**
            At SkinWise, we believe that everyone deserves skincare solutions that truly understand their unique skin.
            Our mission is to simplify the overwhelming world of skincare.

            ### **How It Works**
            We evaluate:
            - Ingredient compatibility
            - Product formulations
            - Price points

            ### **The Science Behind It**
            We use machine learning to understand ingredients and skin types.
            """,
            unsafe_allow_html=True,
        )

    with col1:
        st.markdown("<div style='width:100%; height:300px; background:#f7e5ee; border-radius:12px;'></div>", unsafe_allow_html=True)

    st.write("\n\n")

    st.markdown(
        """
        <div style='text-align:center;'>
            <h3>Our Team</h3>
            <p style='max-width:700px; margin:auto;'>
                SkinWise was created by <b>Tannoo Shukla, Tannu Modanwal, Trapti Rajput, and Vanshika Srivastava</b>.
            </p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.write("\n")

    st.markdown(
        """
        <div style='background:#fde7f3; padding:30px; border-radius:16px; text-align:center;'>
            <h4>Start Your Beauty Journey</h4>
            <p>Discover products perfect for your skin.</p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    colA, colB = st.columns([1, 1])

    # ✅ Buttons that trigger internal page switch
    with colA:
        if st.button("Get Recommendations", use_container_width=True, key="about_goto_home"):
            st.session_state["page"] = "Home"
            st.experimental_rerun()

    with colB:
        if st.button("Take the Skin Quiz", use_container_width=True, key="about_goto_quiz"):
            st.session_state["page"] = "Skin Quiz"
            st.experimental_rerun()
