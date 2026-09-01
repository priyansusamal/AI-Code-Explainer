import streamlit as st
from utils.llm import explain_code, improve_code


# ============================================================
# PAGE CONFIGURATION
# ============================================================

st.set_page_config(
    page_title="AI Code Explainer",
    page_icon="🤖",
    layout="wide"
)


# ============================================================
# HEADER
# ============================================================

st.title("🤖 AI Code Explainer")

st.write(
    "Understand, improve, and optimize your code with Generative AI."
)

st.divider()


# ============================================================
# CODE INPUT
# ============================================================

language = st.selectbox(
    "Programming Language",
    ["Python", "C++", "Java", "JavaScript"]
)

code = st.text_area(
    "Paste your code here:",
    height=300,
    placeholder="Paste your code here..."
)


# ============================================================
# EXPLAIN CODE
# ============================================================

if st.button("🔍 Explain Code", type="primary"):

    if not code.strip():

        st.warning("Please enter some code first.")

    else:

        with st.spinner("🤖 AI is analyzing your code..."):

            try:

                explanation = explain_code(code, language)

                st.divider()

                st.subheader("📖 Code Explanation")

                st.markdown(explanation)

            except Exception as e:

                st.error(f"Something went wrong: {e}")


# ============================================================
# IMPROVE CODE
# ============================================================

st.divider()

if st.button("✨ Improve Code"):

    if not code.strip():

        st.warning("Please enter some code first.")

    else:

        with st.spinner("✨ AI is reviewing your code..."):

            try:

                improvement = improve_code(code, language)

                st.divider()

                st.subheader("✨ Code Improvement")

                st.markdown(improvement)

            except Exception as e:

                st.error(f"Something went wrong: {e}")