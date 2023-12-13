# loading a pre-trained LLM
# options are GPT-2, GPT-3, or GPT-4. GPT-4 requires paid subscription

from transformers import GPT2LMHeadModel, GPT2Tokenizer

model_name = "gpt3"  # Or specify a specific GPT-3 variant such as "gpt3-medium"
tokenizer = GPT2Tokenizer.from_pretrained(model_name)
model = GPT2LMHeadModel.from_pretrained(model_name)
