import os
from dotenv import load_dotenv
from google import genai

from src.database import search_facts
from src.search import search_web

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")
client = genai.Client(api_key=api_key)


def generate_quiz(sport, difficulty):
    # Get information from local ChromaDB
    local_facts = search_facts(sport)

    # Get recent information from web search
    web_results = search_web(sport)

    context = f"""
    Local Sports Knowledge:
    {local_facts}

    Recent Web Information:
    {web_results}
    """

    prompt = f"""
    You are a sports quiz generator.

    Create exactly 5 multiple-choice quiz questions about {sport}.
    Difficulty level: {difficulty}.

    Use the following context to help create accurate questions:

    {context}

    For each question, provide:
    1. The question
    2. Four options labeled A, B, C, and D
    3. The correct answer
    4. A short explanation

    Format the quiz clearly and do not include information
    that you are unsure about.
    """

    response = client.models.generate_content(
        model="gemini-3.5-flash",
        contents=prompt
    )

    return response.text


if __name__ == "__main__":
    quiz = generate_quiz("Cricket", "Easy")
    print(quiz)