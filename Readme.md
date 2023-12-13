# Project: Smart Parent

Welcome to Smart Parent. My first attempt in utilizing OpenAI's provided APIs leveraging GPT-3.5 turbo LLM. GPT is a generative pre-trained tranformer model (or LLM).

## Prompt
My toddler is keen on listening to new stories everyday. I found myself short of being innovative in creating playful, imaginative stories for her on a daily basis.
Hence, I created SMART PARENT; an easy way to generate new stories that will make you look like a Smart (and interesting) Parent.

## Content
- smartParent_bedtime_stories.py: Main script to generate story. You likely do not need to run anything else unless you need to do some customizations.
- load_env.py: Loading your API KEY
- pilot_openai.py: A simple example using Open AI API. Highly recommedn starting here if you are using these APIs for the first time.

## Additional Information
- You can access data dictionary used in the 'final_data_dictionary.json' file. Scripts to generate this data can be found under .\custom_nlp\data_prep
- To leverage your own model, you can use some the scripts provided under .\custom_nlp\data_prep to clean your data, proprocess, and generate tokens. Currently, I don't have enough of my own data to inform my model; hence, it is not yet published. 

Feel free to reach out to me for any questions by leaving comments on my [website](https://aadamani.com/projects)

## Sources
- https://freekidsbooks.org/toddler/
- https://platform.openai.com/docs/api-reference/chat

