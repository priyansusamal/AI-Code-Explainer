import streamlit as st
from utils.llm import explain_code

st.set_page_config(
    page_title="AI Code Explainer",
    page_icon="🤖",
    layout="wide"
)

st.title("🤖 AI Code Explainer")
st.write("Understand, improve, and optimize your code with Generative AI.")

st.divider()

language = st.selectbox(
    "Programming Language",
    ["Python", "C++", "Java", "JavaScript"]
)

code = st.text_area(
    "Paste your code here:",
    height=300,
    placeholder="Paste your code here..."
)

if st.button("🔍 Explain Code", type="primary"):

    if code.strip() == "":
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