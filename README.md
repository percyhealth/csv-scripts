# csv-scripts

python scripts to generate json document of a questionnaire, to be added to a Mongo database.

`questionaire.py`'s main function is
`def questionnaire_generator` which takes the following parameters:
1. `csv_filename` : a `string` name for a `.csv` file which included all the relevant text and scoring for a questionnaire. See `SF-12 - SF-12_questions-and-scores (1).csv` for an example of proper formatting.
2. `title`: a `string` with the title of the questionnaire. Will all be used to name the `.json` output file.
3. `author` a `string` with the authors name. 
4. `standard_frequency`: a `string` with the survey's intended standard frequency. ex: weekly, daily, monthly, etc.
5. `description`: a `string` with a description of the questionnaire and/or its purpose.

see `SF-12questionnaie.json` for an example output
