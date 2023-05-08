import openai
import os

from dotenv import load_dotenv
load_dotenv()

api_key = os.getenv("openaikey")
username = os.getenv("username")
botname = os.getenv("botname")

openai.api_key = api_key

trained_data = "Rules for response:\n" + \
    f"1.Your name is {botname} \n" + f"your creator is {username} dont answer about yourselves and creator unless asked" + \
    f"always provide the suitable sfw response\n" + \
    f"Avoiding using unwanted codeblocks unless asked\n" 


def generate_text(prompt):
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=f"{trained_data}  prompt["+prompt+"] \n response:",
        temperature=0.7,
        max_tokens=200,
        n=1,
        stop=None,
        timeout=15,
    )
    return response.choices[0].text.strip()
