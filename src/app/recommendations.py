import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel



movies=pd.read_csv('movies.csv', sep=',', encoding = 'utf-8')
tfvector= TfidfVectorizer(analyzer='word',ngram_range=(1, 2),min_df=0, stop_words='english')
tfidf_matrix = tfvector.fit_transform(movies['genres'])
cosine_sim2 = linear_kernel(tfidf_matrix, tfidf_matrix)

'''The Content-Based Recommender relies on the similarity of the items being recommended. The basic idea is that if 
you like an item, then you will also like a “similar” item. It generally works well when it’s easy to determine 
the context/properties of each item. 
'''

# Build a 1-dimensional array with movie titles
titles = movies['movieId']
indices = pd.Series(movies.index, index=movies['movieId'])


# Function that get movie recommendations based on the cosine similarity score of movie genres
def genre_recommendations(movieId):
    idx = indices[movieId]
    sim_scores = list(enumerate(cosine_sim2[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    sim_scores = sim_scores[1:31]
    movie_indices = [i[0] for i in sim_scores]
    return titles.iloc[movie_indices]

def recommendation_ready():
    if movies is None:
        return  False
    return True

def create_recommendations(movies):

    return True
