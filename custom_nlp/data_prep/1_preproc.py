import json
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences

# Load the JSON file
with open('final_data_dictionary.json', 'r') as file:
    data = json.load(file)

# Extract story content
stories = [story['content'] for story in data['StoryBooks']]

# Tokenization
tokenizer = Tokenizer()
tokenizer.fit_on_texts(stories)

# Convert text to sequences of integers
sequences = tokenizer.texts_to_sequences(stories)

# Padding sequences to make them uniform length
max_len = 1000  # Adjust the max sequence length based on your data
padded_sequences = pad_sequences(sequences, maxlen=max_len, padding='post', truncating='post')

# Vocabulary size
vocab_size = len(tokenizer.word_index) + 1  # Adding 1 for the padding token

# Example of accessing tokens and padded sequences
print("Original Story:\n", stories[0])
print("\nTokenized Sequence:\n", sequences[0])
print("\nPadded Sequence:\n", padded_sequences[0])
