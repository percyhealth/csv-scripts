import pandas as pd
import json


def scorecard_csv_to_json(csv_filename, json_filename):
    df = pd.read_csv(csv_filename)
    questions = {}
    # create question dictionaries
    for index, row in df.iterrows():
        question = str(row['Question'])
        answer = str(row['Answer'])
        score = float(row['Score'])
        if question in questions:
            questions[question][answer] = score
        else:
            questions[question] = {}
            questions[question][answer] = score

    categories = {}
    for index, row in df.iterrows():
        code = str(row['CODE'])
        question = str(row['Question'])
        if code in categories:
            categories[code][question] = questions[question]
        else:
            categories[code] = {}
            categories[code][question] = questions[question]

    with open(json_filename, "w") as outfile:
        json.dump(categories, outfile, indent=4)
    outfile.close()


scorecard_csv_to_json('PRO-scoringtables - SF-36.csv', 'SF-36scorecard.json')



