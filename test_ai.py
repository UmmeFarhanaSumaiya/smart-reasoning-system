import os
from dotenv import load_dotenv
from google import genai

load_dotenv()
key = os.getenv("GEMINI_API_KEY")

question = input("Write your question here: ")

client = genai.Client()

response = client.models.generate_content(
    model="gemini-3.5-flash",
    contents="Think step by step and explain this problem. For each step, explain WHY it is true. The problem is: " + question
)

print(response.text)