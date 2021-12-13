import process_movies_data as pmd
import pandas as pd

def test_pg_movies():
    """
    Make sure that this function returns movies that are only PG rated
    """
    output = pmd.pg_movies(pd.read_csv('movies.csv'))
    assert output.rating.unique()[0] == 'PG'
