import json
import subprocess

with open('final_data_dictionary.json','r') as file:
    data = json.load(file)

stories = data['StoryBooks']

# preparing a list of store prompt response pairs
prompt_response_pairs = []

def search_prompt(prompt):
    matching_stories = []
    for story in stories:
        title = story['title']
        content = story['content']
        
        # Check if prompt is in title or content
        if prompt in title or prompt in content:
            matching_stories.append(story)
    
    return matching_stories

# Generate prompt-response pairs
for story in stories:
    title = story['title']
    content = story['content']
    
    # Create a prompt using title and content
    prompt = f"Title: {title}\nContent: {content}"  
    # Add the prompt to a list or dictionary as needed
    prompt_response_pairs.append({'prompt': prompt, 'story_title': title, 'story_content': content})
    
    #if responses:
     #   for response in responses:
      #      response_text = f"Title: {response['title']}\nContent: {response['content']}"
       #     prompt_response_pairs.append({'prompt': prompt, 'response': response_text})

# Example of using the generated prompt-response pairs
for pair in prompt_response_pairs:
    print(f"Story Title: {pair['story_title']}")
    print(f"Prompt: {pair['prompt']}\n")

        

