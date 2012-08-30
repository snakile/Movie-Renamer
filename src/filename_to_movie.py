import tokens_to_exclude_before_splitting as exclude_before
import tokens_to_exclude_after_splitting as exclude_after
import re
from movie import Movie

def create_movie_from_filename(filename):
    return Movie.create_movie_from_query(create_imdb_query_from_filename(filename))

def create_imdb_query_from_filename(filename):
    filename_before_split = exclude_tokens(filename, exclude_before.tokens).lower()
    splitted_filename = split(filename_before_split)
    final_filename = exclude_tokens(splitted_filename, exclude_after.tokens)
    return final_filename

def exclude_tokens(filename, tokens_to_exclude):
    filename_after_exclustion = filename
    for t in tokens_to_exclude:
        filename_after_exclustion = filename_after_exclustion.replace(t, '')
    return ' '.join(filename_after_exclustion.split())
    return filename_after_exclustion

def split(filename): 
    splitted_filename = ''
    words = re.compile(r'[^a-z0-9]+').split(filename)
    for w in words:
        splitted_filename += w
    return splitted_filename