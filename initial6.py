
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
    decision = generate_response2(row, "follow these conditions: if high energy is present (High energy includes things such as Gravity (Example: potential for things/people to fall),\
        Motion (Examples: Possible Motor vehicle incident like a crash), Mechanical\
        (Example: Heavy Rotating Equipment), Temperature (Examples: High Temperature, Fires),\
        Pressure (Example: Explosions), Electrical (Examples: Electrical Contact with Source, Arc Flash), Chemical/Radiation\
        (Example: High Dose of Toxic Chemical or Radiation)) then check if there was a high energy incident (which is when high energy is present in the situation, the the energy is released (Example: a tool that is dropped or a person falls),\
        and a person is affected by what happened). Then check if the person was injured seriouly (more than just a bruise, severe illnesses are also considered being injured seriously). If all of these conditions are true then write out the OBSRVTN_NB and a designation of HSIF. if the person was not injured seriously \
        check if the writing says if a direct control (something that stopped the person from getting injured)\
        then write out the OBSRVTN_NB and the designation of Capacity. if there was no direct control and the person was not injured but there was a high energy incident, write out the OBSRVTN_NB and the designation of PSIF\
        If there was was high energy present but no high-energy incident check if direct control present was present. If direct control was present, write out the OBSRVTN_NB and a designation of Success \
        else if there was high energy present but no high-energy incident and no direct control present write out the OBSRVTN_NB and a designation of Exposure. \
        if there was no high energy present and there was a serious injury sustained, write out the OBSRVTN_NB and a designation of LSIF\
        if there was no high energy present and there was no serious injury sustained, only write out the OBSRVTN_NB and a designation of Low-Severity\
        when writing a response write in the format 'BSRVTN_NB (number): and a designation of HSIF, Capacity, PSIF, Success, Exposure, LSIF, or Low-Severity' also write what could be done to stop potential injuries and any improvements that can be made")
    return decision


while True:
    i = 0
    for index, row in df.iterrows():
        response = scl_classification_decision_tree(i)
        i += 1
    break
txt_file_path = 'result.txt'

with open(txt_file_path, 'w') as file:
    file.write(response)

