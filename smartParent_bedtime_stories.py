# Using GPT 3.5 turbo model to generate response based on user inputs.
# NOTE: You will need your own API key to succesfully execute this script
# Author: Aayush Damani
from openai import OpenAI
from dotenv import load_dotenv
import os
import requests
import json


with open('final_data_dictionary.json', 'r') as file:
    stories_data = json.load(file)

 # file reads in your own API KEY. Look at load_env.py file for details
load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

client = OpenAI(
        # Defaults to os.environ.get("OPENAI_API_KEY")
        api_key=api_key,
)

# function to search stories using data provided by you. If nothing available, then generate a story from GPT-3.5
def search_stories(user_input):
    matched_stories = []
    for story in stories_data['StoryBooks']:
        if user_input.lower() in story['title'].lower() or user_input.lower() in story['content'].lower():
            matched_stories.append(story['content'])
    if matched_stories:
        cleaned_story = [story.replace("[",'').replace("]","") for story in matched_stories]
        return cleaned_story
    else:
         # if no matching stories found, generate a story using GPT-3
         prompt = user_input
         if(len(prompt.split())) < 3:
            prompt += "I want to get a story about"
         return generate_story(prompt)

# function to generate story using GPT-3.5 turbo model
def generate_story(prompt):

    # define API endpoints and headers
    endpoint = 'https://api.openai.com/v1/engines/text-davinci-003/completions'
    headers = {
            'Authorization': f'Bearer {api_key}',
            'Content-Type': 'application/json'
        }

    # Define the request payload with your prompt
    payload = {
            'prompt': prompt,
            'max_tokens': 1000,  # Define the maximum number of tokens for the response
            'temperature': 0.7
        }

        # Make a POST request to the API
    response = requests.post(endpoint, json=payload, headers=headers)

        # Check if the request was successful
    if response.status_code == 200:
            return response.json()['choices'][0]['text']
    else:
            return f"Error: {response.status_code} - {response.text}"

# Sample user interaction loop 1
user_prompt = input("Enter a prompt(or 'exit' to quit):")
if user_prompt.lower() == 'exit':
 exit()

result = search_stories(user_prompt)


## Sample outputs to check your work below

#print(result)
#for story in result:
#     print("Title:", story['title'])
#     print("Content:", story['content'])
#     print("\n")

# Sample user interaction loop 2
#while True:
#    user_input = input("Enter your prompt (or 'exit' to quit): ")
#    if user_input.lower() == 'exit':
#        break

    # Process user input to select relevant story data (title or content)
#    relevant_story = None
#    for story in stories_data['StoryBooks']:
#        if user_input.lower() in story['title'].lower() or user_input.lower() in story['content'].lower():
 #           relevant_story = story
  #          break
#
 #   if relevant_story:
  #      prompt = relevant_story['title'] + ' ' + relevant_story['content'] + ' ' + user_input
   #     generated_story = generate_story(prompt)
    #    print("Generated Story:")
     #   print(generated_story)
    #else:
    #    print("No matching story found for the prompt.")
        #generated_story = generate_story(user_input)
        #print("Generated Story:")
        #print(generated_story)

# Usage example 2
#user_input = "give me a story about a fox"
#generated_story = generate_story(user_input)
#print("Generated Story:")
#print(generated_story)