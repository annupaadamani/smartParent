# Script to set environment variable for your API Key
# Pre-Requisite: Create a .env file and assign API key as value to OPENAI_API_KEY
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Retrieve the API key from the environment variables
api_key = os.getenv("OPENAI_API_KEY")

# Now you can use the api_key variable in your OpenAI API requests
print(f"API Key: {api_key}")
