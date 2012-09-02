from movie import Movie
from imdbquery import ImdbQuery
import os

def rename(filename):
    filename_without_extension, extension = os.path.splitext(filename)
    query = ImdbQuery.create_query_from_filename(filename_without_extension)
    movie = Movie.create_movie_from_imdb_query(query)
    return str(movie) + extension