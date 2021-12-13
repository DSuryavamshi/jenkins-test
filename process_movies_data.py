import pandas as pd


def pg_movies(df):
    return movies_df[movies_df['rating'] == 'PG']

movies_df = pd.read_csv("movies.csv")
pg_movie_names = pg_movies(movies_df)
pg_movie_names.to_csv('pg_movies.csv', index=False)
