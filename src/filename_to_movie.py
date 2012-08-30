import tokens_to_exclude_before_splitting.tokens as exclude_before
import tokens_to_exclude_after_splitting.tokens as exclude_after
import re

def create_movie_from_filename(filename):
    filename_before_split = exclude_tokens(filename, exclude_before).lower()
    splitted_filename = split(filename_before_split)
    final_filename = exclude_tokens(splitted_filename, exclude_after)
    return final_filename

def exclude_tokens(filename, tokens_to_exclude):
    filename_after_exclustion = filename
    for t in tokens_to_exclude:
        filename_after_exclustion = filename_after_exclustion.replace(t, '')

def split(filename): 
    splitted_filename = ''
    words = re.compile(r'[^a-z0-9]+').split(filename)
    for w in words:
        splitted_filename += w
    return splitted_filename