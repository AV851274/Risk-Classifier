
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
    decision = generate_response2(row, "Was high energy present (Gravity (Examples: Suspended Loads, Fall from Elevation, potential for things/people to fall),\
        Motion (Examples: Mobile Equipment/Traffic with Workers on Foot, Motor vehicle incident (occupant)), Mechanica\
        (Example: Heavy Rotating Equipment), Temperature (Examples: Steam, High Temperature, Fire with Sustained Fuel Source),\
        Pressure (Example: Explosion), Electrical (Examples: Electrical Contact with Source, Arc Flash), Chemical/Radiation\
        (Example: High Dose of Toxic Chemical or Radiation))? If yes, was there a high-energy incident (Where High\
        energy is present, the energy is released (energy release is an instance where the energy source changes\
        state while exposed to the work environment, Example: a tool that is dropped and transitions from potential\
        to kinetic energy, or a person who loses control of his or her balance and stumbles), and there was contact/proximity (Contact is defined as an instance when the high energy is transmitted\
        to the human body and proximity is defined as a hazardous circumstance where the boundary\
        of the high-energy exposure is within 6 feet of the worker who has unrestricted egress or any\
        distance to the high-energy source when there is a confined space or there is a situation with\
        restricted egress where a worker cannot escape the energy source.))? If yes, was a serious\
        injury sustained (was the person was hurt with more than a bruise)? If yes, the designation is HSIF. If no, was direct control present (a direct\
        control as one that is specifically targeted to the high-energy source; effectively mitigates\
        exposure to the high-energy source when installed, verified, and used properly (i.e., a SIF\
        High Energy Energy Release Contact or Proximity High-Energy Incident Safety Classification and Learning (SCL) Model 12 Edison Electric Institute\
        reasonable should not occur if these conditions are present); and is effective even if there is\
        unintentional human error during the work (unrelated to the installation of the control).\
        Examples of direct controls include LOTO, machine guarding, hard physical barriers, fall\
        protection, and cover-up. Examples that are not direct controls include training, warning\
        signs, rules, and experience because they are susceptible to unintentional human error.\
        Further, most standard non-specialized personal protective equipment like hard hats, gloves,\
        and boots are not direct controls because they are not specifically targeted to a high-energy\
        source.)? If yes, the\
        designation is Capacity, if no, the designation is PSIF. If there was no high-energy incident,\
        was direct control present? If yes, the designation is Success, if no, the designation is\
        Exposure. If high energy was not present, was a serious injury sustained? If yes, the\
        designation is LSIF, if no, the designation is Low-Severity. When formulating a response, write out the OBSRVTN_NB and the designation")
    return decision


while True:
    i = 0
    #print(df.shape[0])
    #llm_response = model.generate("All of the rows contain different incidents, do not use information from one incident in another", max_tokens=1024)
    for index, row in df.iterrows():
        response = scl_classification_decision_tree(i)
        i += 1
        print(response)
    #user_question = input("Ask a question about the CSV (or type 'exit' to quit): ")
    #if user_question.lower() == "exit":
    #    break
    #response = generate_response(user_question)
    #print(response)
    break

