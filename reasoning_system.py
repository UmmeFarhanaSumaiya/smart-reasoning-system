import os
from dotenv import load_dotenv
from google import genai

load_dotenv()
key = os.getenv("GEMINI_API_KEY")

def decompose_problem(problem):

    Client = genai.Client()
    response = Client.models.generate_content(
    model="gemini-3.5-flash",
    contents="Break down the complex thought into smaller one. The thought is:" +problem
    )
    return(response)

def analyze_parts(problem):

    Client = genai.Client()
    response = Client.models.generate_content(
    model="gemini-3.5-flash",
    contents="Analyze the result into very samaller part. do a deep analyze and explain why:" +problem
    )
    return(response)

question = input("Write your complex thought here: ")
result = decompose_problem(question)
print(result.text)

result2 = analyze_parts(result.text)
print(result2.text)