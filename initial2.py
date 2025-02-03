import pandas as pd
from transformers import AutoModelForQuestionAnswering, AutoTokenizer
import torch

# Load the CSV file (adjust the path if needed)
df = pd.read_csv('test.csv')

# Load a more capable model for future use (if required)
model_name = "deepset/roberta-base-squad2"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForQuestionAnswering.from_pretrained(model_name)

def filter_data(query):
    query = query.lower()
    
    mask = (
        df['Date'].str.lower().str.contains(query, na=False) |
        df['Observation Type'].str.lower().str.contains(query, na=False) |
        df['Observation Sub-Type'].str.lower().str.contains(query, na=False) |
        df['Comments'].str.lower().str.contains(query, na=False)
    )

    filtered_df = df[mask]
    
    return filtered_df

def format_answer(filtered_df):
    if filtered_df.empty:
        return "No relevant data found."
    
    answers = []
    for _, row in filtered_df.iterrows():
        observation_details = (
            f"Observation ID: {row['Observation ID']}, "
            f"Date: {row['Date']}, "
            f"Type: {row['Observation Type']}, "
            f"Sub-Type: {row['Observation Sub-Type']}, "
            f"Comments: {row['Comments']}"
        )
        answers.append(observation_details)
    
    return "\n".join(answers)

def main():
    print("Welcome to the CSV Chatbot! Type 'exit' to quit.")
    while True:
        question = input("You: ")
        if question.lower() == 'exit':
            break
        
        filtered_df = filter_data(question)
        
        formatted_answer = format_answer(filtered_df)
        
        print(f"Bot: {formatted_answer}\n")

if __name__ == '__main__':
    main()
