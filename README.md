# csv-scripts

python scripts to generate json document of a questionnaire, to be added to a Mongo database.

`questionnaire_generator.py`'s main function is
`questionnaire_generator` which takes the following parameters:
1. `csv_filename`: `string` name for a `.csv` file which includes all relevant text and scoring for a questionnaire. See `SF-12.csv` for an example of proper formatting. Generated from [this Google Sheet](https://docs.google.com/spreadsheets/d/1QSqy19XCddhdCWZ7mWeo-4cOWPriJMeyZc9HENoJ3hA/edit?usp=sharing).
2. `title`: `string` with the title of the questionnaire. Will also be used to name the `.json` output file.
3. `author`: `string` with the authors name. 
4. `standard_frequency`: `string` with the survey's intended standard frequency. ex: weekly, daily, monthly, etc.
5. `description`: `string` with a description of the questionnaire and/or its purpose.

see `SF-12questionnaire.json` for an example output
