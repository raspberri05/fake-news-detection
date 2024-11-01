# Fake News Detection

## About
This project has two parts to it. 

### Data
Data is scraped from PolitiFact that includes how truthful political statements/comments made by political figures or social media are. This data is saved in a csv file.

The dataset is provided in this repository for any use by developers/researchers as long as the usage complies with the open source license of this repository.

### Machine Learning
The dataset is used to create a model that can help figure out how truthful political news/commentary is. I am currently using Tensorflow for the model.

## Dataset
Packages required to run the notebooks are defined in `requirements.txt`. 
You can install from this file with the command `pip install -r requirements.txt` if you are using `pip`. `requirements.txt` has the CUDA-enabled version of Tensorflow. If you want to train the model on CPU, you will have to install the appropriate type of Tensorflow. Follow the instructions at https://www.tensorflow.org/install for both GPU and/or CPU setup.

This dataset was generated on November 1, 2024. If you want more up-to-date data I recommend running `main.ipynb` to create the most up-to-date dataset.
Otherwise, you can just use dataset (csv) that is in this repository.

*Note: Running the Notebook to generate the dataset will take multiple minutes (it took 5 minutes for me)*

### Shape

1801 rows x 7 columns

#### Columns

ruling - the ruling of truthfulness

name - name of person or group making the statement

quote - the statement itself

description - information about where this quote is from

day - the day the quote was said

month - the month the quote was said

year - the year the quote was said
