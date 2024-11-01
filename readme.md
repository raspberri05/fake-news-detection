# fake-news-detection

## About
This project has two parts to it. 

1) Getting Data - Data is scraped from PolitiFact that includes how truthful political statements made by political figures or social media is. This data is put into a csv data for ML purposes.
2) Machine Learning - The dataset will be used to create a model that can help figure out how truthful news is. I haven't gotten to this part yet, but I will most likely use Tensorflow.

The dataset is also provided in this repository for any use by developers/researchers that complies with the open source license of this repository.

## Dataset
Packages required to run the notebooks are defined in `requirements.txt`. 
You can install from this file with the command `pip install -r requirements.txt` if you are using `pip`. Otherwise package managers will have other methods of doing this. 

This dataset was generated on October 31, 2024. If you want more up-to-date data I recommend running `main.ipynb` to create the most up-to-date dataset.
Otherwise, you can just use dataset (csv) that is in this repository.

*Note: Running the Notebook to generate the dataset will take multiple minutes (it took 5 minutes for me)*

### Shape

1801 rows x 5 columns

#### Columns

Ruling - the ruling of truthfulness

Name - name of person or site making the statement

Quote - the statement itself

Description - information about where this quote is from

Date - the date the quote was said

