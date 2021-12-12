import pandas as pd

movies_df = pd.read_csv("movies.csv")
pg_movies = movies_df[movies_df['rating'] == 'PG']
pg_movies.to_csv('pg_movies.csv', index=False)
