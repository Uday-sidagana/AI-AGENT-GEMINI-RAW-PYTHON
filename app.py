# from google import genai

from openai import OpenAI

from dotenv import load_dotenv
import os

load_dotenv()

api_key = os.getenv("GPT_KEY")


client = OpenAI(
  api_key=api_key
)

completion = client.chat.completions.create(
  model="gpt-4o-mini",
  store=True,
  messages=[
    {"role": "user", "content": "Tell me how to make an AI Agent who can automatically fill a google form"}
  ]
)

print(completion.choices[0].message)
