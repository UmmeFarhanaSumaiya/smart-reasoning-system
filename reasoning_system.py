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

def summarize(analysis):

    Client = genai.Client()
    response = Client.models.generate_content(
        model="gemini-3.5-flash",
        contents="Analyse all the thoughts, and give an impactful summary: "+analysis
    )
    return(response)


question = input("Write your complex thought here: ")
result_phase1 = decompose_problem(question)
print(result_phase1.text)

result_phase2 = analyze_parts(result_phase1.text)
print(result_phase2.text)

result_phase3 = summarize(result_phase2.text)
print(result_phase3.text)