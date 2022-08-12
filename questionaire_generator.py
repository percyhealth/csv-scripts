import pandas as pd
import json
import pprint

pp = pprint.PrettyPrinter(indent=4)

this_title = "SF-12"
this_author = "Laurel Dernbach"
this_standard_frequency = 'weekly'
this_description = 'short-form questionnaire to measure quality of life'

# https://stackoverflow.com/questions/944700/how-can-i-check-for-nan-values
def isNaN(num):
    return num != num

# id,section,instructions,question,response_type,answer_text,answer_values,answer_scores
def scorecard_generator(csv_filename):
    df = pd.read_csv(csv_filename)
    scorecard = {}
    # create question dictionaries
    for index, row in df.iterrows():
        sections = str(row['section']).split(' | ') # different categories for each question
        # print(sections)
        # print(row['id'])
        for i in range(len(sections)):
            curr_question = {}
            question = str(row['id'])
            values = str(row['answer_values']).split('\n') # split by \n
            scores_lines = str(row['answer_scores']).split('\n') # split by \n and get i index
            for v in range(len(values)):
                score = scores_lines[v].split(' | ')
                curr_question[values[v]] = float(score[i])

            if sections[i] in scorecard.keys():
                scorecard[sections[i]][row['id']] = curr_question
            else:
                scorecard[sections[i]] = {}
                scorecard[sections[i]][row['id']] = curr_question

    pp.pprint(scorecard)

    return scorecard


def questions_generator(csv_filename):
    df = pd.read_csv(csv_filename)
    all_questions = {}
    # create question dictionaries
    for index, row in df.iterrows():
        curr_question = {}
        responses = {}
        values = str(row['answer_values']).split('\n')
        texts = str(row['answer_text']).split('\n')
        for i in range(len(values)):
            responses[values[i]] = None if texts[i] == 'nan' else texts[i]
        # handle NaN entries (NA in the .csv)
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

#pp.pprint(questions_generator('SF-12 - SF-12_questions-and-scores (1).csv'))

# scorecard_generator('SF-12 - SF-12_questions-and-scores (1).csv')
