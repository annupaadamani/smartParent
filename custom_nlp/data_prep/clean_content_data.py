import json

# Read the JSON file
with open('./story_titles.json', 'r') as titles:
    data_titles = json.load(titles)

with open('./story_content.json', 'r') as content:
    data_content = json.load(content)

# Replace Unicode quotes in each string of the array
modified_strings = [string.replace('\u201c', '"').replace('\u201d', '"') for string in data_content['content']]

data_content['content'] = modified_strings
# Remove specific Unicode characters
characters_to_remove = ['\u2019', '\u2018', '\u2026', '\ufb02', '\u00a7','\u00e9','\u2013','\ufffd']

text_list = data_content['content']  
cleaned_text_list = []

for text in text_list:
    cleaned_text = text
    for char in characters_to_remove:
        cleaned_text = cleaned_text.replace(char, '')
    cleaned_text_list.append(cleaned_text)

# Update the data dictionary with cleaned text
data_content['content'] = cleaned_text_list

# Write the updated content back to the JSON file
with open('story_content.json', 'w') as file:
    json.dump(data_content, file, indent=4)

with open('story_content.json', 'r') as content:
    data_content = json.load(content)

# Merge titles and contents based on index or position
merged_data = {
    "StoryBooks": [
        {"title": titles, "content": content}
        for titles, content in zip(data_titles['titles'], data_content['content'])
    ]
}

# Write the merged data to a new JSON file
with open('final_data_dictionary.json', 'w') as file:
    json.dump(merged_data, file, indent=4)
