#  AI Code Explainer

An AI-powered application that helps beginners understand, improve, and optimize programming code using Generative AI.

The application allows users to paste their code, select the programming language, and use AI to analyze the code in a simple and beginner-friendly way.

---

##  Features

###  Explain Code

Analyze code and get a beginner-friendly explanation covering:

- What the code does
- How the code works
- Time complexity
- Space complexity
- Important functions
- Important variables

###  Improve Code

Get practical suggestions to make code:

- More readable
- Better structured
- Easier to understand
- More maintainable
- Better aligned with coding best practices

The AI is instructed to keep improvements at approximately the same difficulty level as the original code.

###  Optimize Code

Analyze the efficiency of an algorithm and identify:

- Current time complexity
- Current space complexity
- Performance bottlenecks
- Optimization strategies
- Optimized code
- New time and space complexity
- Comparison between the original and optimized versions

###  Multiple Programming Languages

Currently supports:

-  Python
-  C++
-  Java
-  JavaScript

---

## Tech Stack

| Technology | Purpose |
|---|---|
| Python | Application development |
| Streamlit | Web interface |
| Groq API | Generative AI |
| GPT-OSS 20B | Code analysis and generation |
| OpenAI Python SDK | API communication |
| python-dotenv | Environment variable management |

---

## Project Structure

```text
AI-Code-Explainer/
│
├── app.py
├── README.md
├── requirements.txt
├── .gitignore
│
├── prompts/
│   ├── explain.txt
│   ├── improve.txt
│   └── optimize.txt
│
└── utils/
    ├── __init__.py
    └── llm.py