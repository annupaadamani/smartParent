# Using GPT 3.5 turbo model to generate response based on user inputs.
# A good starter script for anyone just starting with using OpenAI APIs
# NOTE: You will need your own API key to succesfully execute this script
from openai import OpenAI
from dotenv import load_dotenv
import os

# file reads in your own API KEY. Look at load_env.py file for details
load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

client = OpenAI(
    # Defaults to os.environ.get("OPENAI_API_KEY")
    api_key=api_key,
)

chat_completion = client.chat.completions.create(
    model= "gpt-3.5-turbo",
    messages=[
        {
            "role": "system",
            "content": "You are helpful assistant"
        },
        {
            "role": "user",
            "content": "What are you doing?"
        },
      ],
      )
response = chat_completion.choices[0].message.content,

print(response)