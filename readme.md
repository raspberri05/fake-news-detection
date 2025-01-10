# Fake News Detection

## About
This project has two parts to it - gathering data, and using the data to generate ml models

### Data
Data is scraped from PolitiFact that includes how truthful political statements/comments made by political figures or social media are. This data is saved to `politifact.csv`.

#### Shape

17636 rows x 4 columns

##### Columns

ruling - the ruling of truthfulness

name - name of person or group making the statement

quote - the statement itself

description - information about where this quote is from and the date it was said

### Machine Learning
The dataset will be used to create a model that can help figure out how truthful political news/commentary is. I am working on cleaning the data and processing categorical data, and plan to start with using Tensorflow to train a model.

## Local Development
Packages required to run the code is defined in `requirements.txt`. 
If you are using pip, you can install these dependencies with the command `pip install -r requirements.txt`. Using a python environment such as conda or venv is recommended

This dataset was generated on November 2, 2024. You can run `main.py` to regnerate the dataset with the newest content from PolitiFact. The script may take up to a minute to run, and does not produce output in the console until completion.
