import os
from dotenv import load_dotenv
from openai import OpenAI


# ============================================================
# CONFIGURATION
# ============================================================

load_dotenv()

# Try to get API key from local .env
api_key = os.getenv("GROQ_API_KEY")

# If running on Streamlit Cloud, get API key from Secrets
if not api_key:
    try:
        import streamlit as st
        api_key = st.secrets["GROQ_API_KEY"]
    except Exception:
        pass

# Stop the app if no API key is available
if not api_key:
    raise ValueError(
        "GROQ_API_KEY not found. "
        "Add it to .env locally or Streamlit Secrets."
    )


# ============================================================
# GROQ CLIENT
# ============================================================

client = OpenAI(
    api_key=api_key,
    base_url="https://api.groq.com/openai/v1"
)

MODEL = "openai/gpt-oss-20b"


# ============================================================
# EXPLAIN CODE
# ============================================================

def explain_code(code, language):

    prompt = (
        "You are a friendly programming tutor who explains code "
        "to beginners.\n\n"

        f"Analyze the following {language} code:\n\n"

        f"CODE:\n"
        f"{code}\n\n"

        "Explain the code in simple, beginner-friendly language.\n"
        "Assume the user may be new to programming.\n"
        "Explain technical terms whenever necessary.\n\n"

        "Use exactly these sections:\n\n"

        "## What the Code Does\n"
        "Explain the overall purpose of the code.\n\n"

        "## How It Works\n"
        "Explain the logic step by step.\n\n"

        "## Time Complexity\n"
        "Give the Big-O time complexity and explain why.\n\n"

        "## Space Complexity\n"
        "Give the Big-O space complexity and explain why.\n\n"

        "## Important Functions\n"
        "List the important functions and explain what each one does.\n\n"

        "## Important Variables\n"
        "List the important variables and explain their purpose.\n\n"

        "Keep the explanation clear, concise, and beginner-friendly."
    )

    response = client.responses.create(
        model=MODEL,
        input=prompt
    )

    return response.output_text


# ============================================================
# IMPROVE CODE
# ============================================================

def improve_code(code, language):

    prompt = (
        "You are a beginner-friendly programming tutor and code reviewer.\n\n"

        f"Review the following {language} code:\n\n"

        f"CODE:\n"
        f"{code}\n\n"

        "Your goal is to make the code cleaner, clearer, and easier "
        "for a beginner to understand.\n\n"

        "IMPORTANT RULES:\n"
        "- Keep the original functionality unchanged.\n"
        "- Make simple and practical improvements.\n"
        "- Keep the improved code at approximately the same difficulty "
        "level as the original code.\n"
        "- Prefer readable code over clever code.\n"
        "- Use meaningful variable and function names.\n"
        "- Remove unnecessary code when appropriate.\n"
        "- Add simple comments only when they genuinely help understanding.\n"
        "- Do NOT introduce advanced programming concepts.\n"
        "- Do NOT introduce complex data structures unless they are already "
        "used in the original code.\n"
        "- Do NOT introduce unnecessary libraries.\n"
        "- Do NOT make the code unnecessarily longer.\n"
        "- Do NOT completely redesign a simple program.\n"
        "- If the original code is already good, make only small improvements "
        "or explain that no major changes are needed.\n\n"

        "Use exactly these sections:\n\n"

        "## Code Review\n"
        "Briefly explain what could be improved.\n\n"

        "## Suggested Improvements\n"
        "List simple improvements and explain why each one is useful.\n\n"

        "## Improved Code\n"
        f"Provide the complete improved {language} code.\n\n"

        "## Why This Version Is Better\n"
        "Explain the improvements in simple language."
    )

    response = client.responses.create(
        model=MODEL,
        input=prompt
    )

    return response.output_text


# ============================================================
# OPTIMIZE CODE
# ============================================================

def optimize_code(code, language):

    prompt = (
        "You are an expert programming tutor who specializes in "
        "algorithm optimization.\n\n"

        f"Analyze the following {language} code:\n\n"

        f"CODE:\n"
        f"{code}\n\n"

        "Your goal is to improve the efficiency of the code while "
        "keeping it understandable for a beginner.\n\n"

        "IMPORTANT RULES:\n"
        "- Keep the original functionality unchanged.\n"
        "- First analyze the current algorithm.\n"
        "- Identify the current time complexity.\n"
        "- Identify the current space complexity.\n"
        "- Look for unnecessary loops, repeated calculations, "
        "or inefficient operations.\n"
        "- Only optimize when a meaningful optimization is possible.\n"
        "- Prefer simple and understandable solutions.\n"
        "- Do NOT introduce unnecessarily advanced concepts.\n"
        "- Do NOT use unnecessary libraries.\n"
        "- Do NOT sacrifice readability for a very small performance gain.\n\n"

        "Use exactly these sections:\n\n"

        "## Current Complexity\n"
        "Give the current time and space complexity and explain why.\n\n"

        "## Bottleneck\n"
        "Identify the main part of the code that affects performance.\n\n"

        "## Optimization Strategy\n"
        "Explain the approach used to make the code more efficient.\n\n"

        "## Optimized Code\n"
        f"Provide the complete optimized {language} code.\n\n"

        "## New Complexity\n"
        "Give the new time and space complexity and explain the improvement.\n\n"

        "## Comparison\n"
        "Compare the original and optimized versions in simple language."
    )

    response = client.responses.create(
        model=MODEL,
        input=prompt
    )

    return response.output_text