import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

api_key = os.getenv("GROQ_API_KEY")

if not api_key:
    raise ValueError("GROQ_API_KEY not found in .env")

client = OpenAI(
    api_key=api_key,
    base_url="https://api.groq.com/openai/v1"
)


def explain_code(code, language):

    prompt = (
        "You are an expert programming tutor who explains code to beginners.\n\n"
        f"Analyze the following {language} code:\n\n"
        f"CODE:\n{code}\n\n"
        "Explain the code in a simple and beginner-friendly way.\n\n"
        "Use these sections:\n\n"
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
        "Keep the explanation beginner-friendly."
    )

    response = client.responses.create(
        model="openai/gpt-oss-20b",
        input=prompt
    )

    return response.output_text