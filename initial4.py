
from gpt4all import GPT4All
import pandas as pd

df = pd.read_csv('observation_data_with_additional_columns.csv')


model = GPT4All("Meta-Llama-3-8B-Instruct.Q4_0.gguf")


def prepare_csv_prompt(question):
    prompt = f"The user has asked a question about a dataset:\n\n{df.head(df.shape[0]).to_string()}\n\n"
    prompt += f"Question: {question}\n\n"
    prompt += "Based on the above data from the CSV file, provide an answer to the question."
    return prompt


def generate_response(question):

    prompt = prepare_csv_prompt(question)
    

    with model.chat_session():
        llm_response = model.generate(prompt, max_tokens=1024)
    return llm_response
def generate_response2(row, question):

    prompt = prepare_csv_prompt("In row" + str(row) + " " + question + "In the Observation Type, Observation Sub-Type, or Comments")
    

    with model.chat_session():
        llm_response = model.generate(prompt, max_tokens=1024)
    return llm_response

def scl_classification_decision_tree(row):
    decision = generate_response2(row, "Was high energy present? If yes, was there a high-energy incident (Where High energy is present, the energy is released, and there was contact/proximity)?\
         If yes, was a serious injury sustained? If yes, the designation is HSIF. If no, was direct control present?\
              If yes, the designation is Capacity, if no, the designation is PSIF. If there was no high-energy incident,\
                   was direct control present? If yes, the designation is Success, if no, the designation is Exposure.\
                        If high energy was not present, was a serious injury sustained? If yes, the designation is LSIF,\
                             if no, the designation is Low-Severity. only write out the designation as a response, nothing else")
    return decision


while True:
    #user_question = input("Ask a question about the CSV (or type 'exit' to quit): ")
    #if user_question.lower() == "exit":
    #    break
    i = 0
    #print(df.shape[0])
    for index, row in df.iterrows():
        response = scl_classification_decision_tree(i)
        i += 1
        print(response)
    break
