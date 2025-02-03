from transformers import pipeline
import pandas as pd


pipe = pipeline("feature-extraction", model="google-bert/bert-base-uncased")
df = pd.read_csv('test.csv')


high_energy_keywords = ['high voltage', 'heavy machinery', 'explosives', 'high pressure', 'high temperature']
high_energy_incident_keywords = ['explosion', 'electrocution', 'fire', 'collapse', 'spill']
serious_injury_keywords = ['fracture', 'burn', 'amputation', 'fatality', 'loss of limb']
direct_control_keywords = ['safety harness', 'lockout/tagout', 'protective barriers', 'PPE', 'safety procedures']


def check_keywords(comment, keywords):
    return any(keyword in comment.lower() for keyword in keywords)

def encode_comments(comments):
    encoded_comments = []
    for comment in comments:
        features = pipeline(comment, truncation=True, padding=True)
        comment_features = features[0]
        avg_features = [sum(col) / len(col) for col in zip(*comment_features)]
        encoded_comments.append(avg_features)
    return encoded_comments

comments = df['Comments'].tolist()
encoded_comments = encode_comments(comments)

encoded_df = pd.DataFrame(encoded_comments)

df = pd.concat([df, encoded_df], axis=1)

df['High Energy Present'] = df['Comments'].apply(lambda x: check_keywords(x, high_energy_keywords))
df['High Energy Incident'] = df['Comments'].apply(lambda x: check_keywords(x, high_energy_incident_keywords))
df['Serious Injury'] = df['Comments'].apply(lambda x: check_keywords(x, serious_injury_keywords))
df['Direct Control Present'] = df['Comments'].apply(lambda x: check_keywords(x, direct_control_keywords))

def classify_observation(row):
    if row['High Energy Present']:
        if row['High Energy Incident']:
            if row['Serious Injury']:
                if not row['Direct Control Present']:
                    return 'HSIF'
                else:
                    return 'Capacity'
            else:
                if not row['Direct Control Present']:
                    return 'PSIF'
                else:
                    return 'Capacity'
        else:
            if not row['Direct Control Present']:
                return 'Exposure'
            else:
                return 'Success'
    else:
        if row['Serious Injury']:
            return 'LSIF'
        else:
            return 'Low-Severity'

df['Classification'] = df.apply(classify_observation, axis=1)

high_value_observations = df[df['Classification'].isin(['HSIF', 'PSIF'])]
print(high_value_observations)

high_value_observations.to_csv('test-result.csv', index=False)

