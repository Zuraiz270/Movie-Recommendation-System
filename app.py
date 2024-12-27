import streamlit as st
import pickle

st.title('Movie Recommender System')

SIMILARITY_PATH = 'similarity.pkl'
MOVIES_LIST = 'movies_list.pkl'

@st.cache_resource
def load_data():
    movies = pickle.load(open(MOVIES_LIST, 'rb'))
    similarity = pickle.load(open(SIMILARITY_PATH, 'rb'))
    return movies, similarity

movies, similarity = load_data()

def recommendation(movie_name, no_of_recommendation):
    # Get the index of the movie
    index = movies[movies['title'] == movie_name].index[0]
    # Get the similarity of the movie with other movies
    distance = sorted(list(enumerate(similarity[index])), reverse = True, key = lambda vector:vector[1])
    recommended_movies = []
    for i in distance[1:no_of_recommendation + 1]:
        # Append the title of the movie to the recommended_movies list
        recommended_movies.append(movies.iloc[i[0]].title)
        print(movies.iloc[i[0]].title)
    return recommended_movies

movie_name = st.selectbox('Select a movie', movies['title'].values)
no_of_recommendation = st.slider('Number of recommendations', 1, 10, 1)

if st.button('Recommend'):
    recommended_movies = recommendation(movie_name, no_of_recommendation)
    # Display the recommended movies
    for i in range(no_of_recommendation):
        st.write(f'{i+1}. {recommended_movies[i]}')
        