import pandas as pd
import json

this_title = "SF-12"
this_author = "Laurel Dernbach"
this_standard_frequency = 'weekly'
this_description = 'short-form questionnaire to measure quality of life'


# https://stackoverflow.com/questions/944700/how-can-i-check-for-nan-values
def isNaN(num):
    return num != num


def scorecard_generator(csv_filename):
    df = pd.read_csv(csv_filename)
    scorecard = {}
    # create question dictionaries
    for index, row in df.iterrows():
        categories = str(row['section']).split(' | ')  # different categories for each question
        for i in range(len(categories)):
            curr_question = {}
            question_num = str(row['id'])
            values = str(row['answer_values']).split('\n')
            scores_lines = str(row['answer_scores']).split('\n')
            for v in range(len(values)):
                score = scores_lines[v].split(' | ')
                curr_question[values[v]] = float(score[i])

            if categories[i] in scorecard.keys():
                scorecard[categories[i]][question_num] = curr_question
            else:
                scorecard[categories[i]] = {}
                scorecard[categories[i]][question_num] = curr_question

    return scorecard


def questions_generator(csv_filename):
    df = pd.read_csv(csv_filename)
    all_questions = {}
    for index, row in df.iterrows():
        curr_question = {}
        responses = {}
        values = str(row['answer_values']).split('\n')
        texts = str(row['answer_text']).split('\n')
        for i in range(len(values)):
            responses[values[i]] = None if texts[i] == 'nan' else texts[i]
        curr_question["instructions"] = None if isNaN(row["instructions"]) else row['instructions']
        curr_question["question"] = None if isNaN(row['question']) else row['question']
        curr_question["response_type"] = None if isNaN(row['response_type']) else row['response_type']
        curr_question["responses"] = responses

        all_questions[row['id']] = curr_question

    return all_questions


def questionnaire_generator(csv_filename, title, author, standard_frequency, description):
    questionnaire = {'title': title, 'author': author, 'standard_frequency': standard_frequency,
                     'description': description, 'questions': questions_generator(csv_filename),
                     'scoring_schema': scorecard_generator(csv_filename)}

    json_filename = title + 'questionnaire.json'
    with open(json_filename, "w") as outfile:
        json.dump(questionnaire, outfile, indent=4)
    outfile.close()


questionnaire_generator('SF-12 - SF-12_questions-and-scores (1).csv', this_title, this_author, this_standard_frequency,
                        this_description)
