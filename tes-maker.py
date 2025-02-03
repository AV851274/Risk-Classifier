import pandas as pd

# Data extracted from the new image provided
data_with_additional_columns = {
    "OBSRVTN_NB": [330560, 164330, 265239, 404438, 83172, 438962, 485230, 40409, 424794],
    "DATETIME_DTM": ["3/15/2023 11:01", "7/9/2019 10:00", "8/1/2022 10:15", "10/18/2023 12:06", 
                     "3/3/2021 11:00", "2/22/2024 12:24", "8/5/2024 9:30", "6/24/2020 10:03", 
                     "12/28/2023 11:02"],
    "PNT_NM": [
        "Did you recognize additional slip, trip, or fall hazards that had not already been recognized and mitigated? If so, please select or describe these hazards in the At-Risk notes.",
        "Vehicle Operating Condition",
        "Suspended Load/Overhead Work",
        "PPE - Workforce",
        "Climbing - Procedures",
        "PPE",
        "PPE - Transmission",
        "Complete job briefing given (Forestry)",
        "Stop When Uncertain"
    ],
    "QUALIFIER_TXT": [
        "Awareness of environment",
        "Other - Vehicle Operating Condition",
        "Other - Suspended Load/Overhead Work",
        "Other - PPE Workforce",
        "Was a drop zone established, and clearly marked?",
        "Personal voltage detector",
        "Hearing protection as required by OSHA and in Owner-designated areas",
        "Other / Job Briefing",
        "Assistance requested"
    ],
    "PNT_ATRISKNOTES_TX": [
        "[NAME] was working a near by cliff that had about a 20' drop off, crew didn't discuss as a hazard on briefing, i discussed with GF and he told the foreman to make the corrections and place something out there to give crews a visual.",
        "[NAME] trucks with cut out bumpers need a hitch step fabricated to facilitate safe entry and exit from the back",
        "Employee rigged a concrete culvert to be off load from a flat bed trailer. Employee was in line of fire when culvert was being lifted.",
        "[NAME] tender was not wearing his Hardhat. I recommended they discuss PPE use during the after lunch briefing.",
        "A drop zone was not clearly marked by the crew while the climber aloft was bringing the tree down to a spar.",
        "Discussed the need to utilize PVDs during assessment with unknown conditions and downed lines. AEP Utilities - PVD Policy",
        "Team was wearing all appropriate PPE for the tasks at hand until the hydrovac team started their work. I noticed that the equipment was rather loud, so I conducted a noise survey and shared the results with the team. I also shared the NIOSH app that I was using with the crew leaders as well. They weren't familiar with it, and they downloaded the application for their use too. Kudos to the team, as they all went and got their hearing protection and thanked me for sharing the results.",
        "No [NAME] version available. [NAME] went over briefing with us. Explained the need for and purpose of [NAME] briefing. Need more detail on ATE fire briefing; no assignments, water source, or humidity.",
        "After looking at the job LCS requested a Vac truck due to seeing the markings of all underground utilities in the area."
    ],
    "PNT_ATRISKFOLWUPNTS_TX": [""] * 9  # No follow-up notes provided in the image
}

# Convert the data into a DataFrame
df_additional = pd.DataFrame(data_with_additional_columns)

# Save the DataFrame as a CSV file
csv_file_path_additional = 'test.csv'
df_additional.to_csv(csv_file_path_additional, index=False)

csv_file_path_additional
