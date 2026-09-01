import streamlit as st

from utils.llm import (
    explain_code,
    improve_code,
    optimize_code
)


# ============================================================
# PAGE CONFIGURATION
# ============================================================

st.set_page_config(
    page_title="AI Code Explainer",
    page_icon="",
    layout="wide"
)


# ============================================================
# HEADER
# ============================================================

st.title("AI Code Explainer")

st.write(
    "Understand, improve, and optimize your code with Generative AI."
)

st.divider()


# ============================================================
# CODE INPUT
# ============================================================

language = st.selectbox(
    "Programming Language",
    [
        "Python",
        "C++",
        "Java",
        "JavaScript"
    ]
)

code = st.text_area(
    "Paste your code here:",
    height=300,
    placeholder="Paste your code here..."
)


# ============================================================
# ACTION BUTTONS
# ============================================================

col1, col2, col3 = st.columns(3)


# ============================================================
# EXPLAIN CODE
# ============================================================

with col1:

    explain_button = st.button(
        "Explain Code",
        use_container_width=True,
        type="primary"
    )


# ============================================================
# IMPROVE CODE
# ============================================================

with col2:

    improve_button = st.button(
        "Improve Code",
        use_container_width=True
    )


# ============================================================
# OPTIMIZE CODE
# ============================================================

with col3:

    optimize_button = st.button(
        "Optimize Code",
        use_container_width=True
    )


# ============================================================
# EXPLAIN CODE RESULT
# ============================================================

if explain_button:

    if not code.strip():

        st.warning("Please enter some code first.")

    else:

        with st.spinner("AI is analyzing your code..."):

            try:

                explanation = explain_code(
                    code,
                    language
                )

                st.divider()

                st.subheader("Code Explanation")

                st.markdown(explanation)

            except Exception as e:

                st.error(
                    f"Something went wrong: {e}"
                )


# ============================================================
# IMPROVE CODE RESULT
# ============================================================

if improve_button:

    if not code.strip():

        st.warning("Please enter some code first.")

    else:

        with st.spinner("AI is reviewing your code..."):

            try:

                improvement = improve_code(
                    code,
                    language
                )

                st.divider()

                st.subheader("Code Improvement")

                st.markdown(improvement)

            except Exception as e:

                st.error(
                    f"Something went wrong: {e}"
                )


# ============================================================
# OPTIMIZE CODE RESULT
# ============================================================

if optimize_button:

    if not code.strip():

        st.warning("Please enter some code first.")

    else:

        with st.spinner(" AI is optimizing your code..."):

            try:

                optimization = optimize_code(
                    code,
                    language
                )

                st.divider()

                st.subheader("Code Optimization")

                st.markdown(optimization)

            except Exception as e:

                st.error(
                    f"Something went wrong: {e}"
                )