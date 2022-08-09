import pandas as pd
import json


# https://stackoverflow.com/questions/944700/how-can-i-check-for-nan-values
def isNaN(num):
    return num != num


def questions_csv_to_json(csv_filename, json_filename):
    df = pd.read_csv(csv_filename)
    all_questions = {}
    # create question dictionaries
    for index, row in df.iterrows():
        curr_question = {}
        responses = {}
        values = str(row['answer_values']).split('\n')
        texts = str(row['answer_text']).split('\n')
        for i in range(len(values)):
            responses[values[i]] = texts[i]
        # handle NaN entries (NA in the .csv)
        curr_question["instructions"] = None if isNaN(row["instructions"]) else row['instructions']
        curr_question["question"] = row['question']
        curr_question["response_type"] = row['response_type']
        curr_question["responses"] = responses

        all_questions[row['id']] = curr_question

    with open(json_filename, "w") as outfile:
        json.dump(all_questions, outfile, indent=4)
    outfile.close()


questions_csv_to_json('SF36-questionnaire - Questions - python script format.csv', 'SF-36questions.json')



