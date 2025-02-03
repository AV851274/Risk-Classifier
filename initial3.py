"""from gpt4all import GPT4All

import pandas as pd

df = pd.read_csv('test.csv')

model = GPT4All("Meta-Llama-3-8B-Instruct.Q4_0.gguf") # downloads / loads a 4.66GB LLM
with model.chat_session():
    print(model.generate("How can I run LLMs efficiently on my laptop?", max_tokens=1024))
"""
from gpt4all import GPT4All
import pandas as pd

# Load the CSV file into a DataFrame
df = pd.read_csv('test.csv')

# Initialize the LLM model
model = GPT4All("Meta-Llama-3-8B-Instruct.Q4_0.gguf")

# Function to prepare a CSV-based prompt
def prepare_csv_prompt(question):
    prompt = f"The user has asked a question about a dataset:\n\n{df.head(5).to_string()}\n\n"
    prompt += f"Question: {question}\n\n"
    prompt += "Based on the above data from the CSV file, provide an answer to the question."
    return prompt

# Function to generate a response using the LLM
def generate_response(question):
    # Prepare the prompt by including relevant data from the CSV
    prompt = prepare_csv_prompt(question)
    
    # Use the LLM to generate a response
    with model.chat_session():
        llm_response = model.generate(prompt, max_tokens=1024)
    return llm_response

# Example usage: Asking the chatbot a question
while True:
    user_question = input("Ask a question about the CSV (or type 'exit' to quit): ")
    if user_question.lower() == "exit":
        break
    response = generate_response(user_question)
    print(response)
