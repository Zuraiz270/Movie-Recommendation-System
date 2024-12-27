# Movie Recommendation System

This project is a Movie Recommendation System built using Python, Streamlit, and machine learning techniques. The system recommends movies based on the similarity of their descriptions.

## Files in the Project

- `similarity.pkl`: A pickle file containing the similarity matrix.
- `movies_list.pkl`: A pickle file containing the list of movies.
- `movie-recommendation-system.ipynb`: A Jupyter notebook containing the code for data preprocessing, model building, and evaluation.
- `app.py`: A Streamlit application to interact with the recommendation system.

## Requirements

- Python 3.10 or higher
- Streamlit
- Pandas
- Scikit-learn
- Numpy
- NLTK

## Usage

1. Open the Streamlit application in your browser.
2. Select a movie from the dropdown menu.
3. Choose the number of recommendations.
4. Click the "Recommend" button to get the list of recommended movies.

## Data Preprocessing and Model Building

The Jupyter notebook [movie-recommendation-system.ipynb] contains the following steps:
1. Loading the dataset.
2. Data preprocessing: filling missing values, removing punctuations, and stopwords.
3. Building the model using TF-IDF Vectorizer and Truncated SVD.
4. Calculating the cosine similarity matrix.
5. Normalizing the similarity matrix.
6. Saving the model and data using pickle.

## Acknowledgements

- Kaggle for providing the dataset.
- Streamlit for the web application framework.
