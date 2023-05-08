import openai
import os

from dotenv import load_dotenv

load_dotenv()  # load environment variables from .env file

api_key = os.getenv("openaikey")
openai.api_key = api_key
def open_website(prompt):
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt="create homepage link for" + prompt,
        temperature=0.7,
        max_tokens=1024,
        n=1,
        stop=None,
        timeout=15,
    )
    return response.choices[0].text.strip()