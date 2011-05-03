from movie import Movie
print Movie('pulp fiction', 1995)
print Movie('pulp fiction', '1995')
print Movie.create_movie_from_query('the prestige')
print Movie.create_movie_from_query('matrix')
print Movie.create_movie_from_query('TheDarkKnight')
print Movie.create_movie_from_query('lord.of.rings-two.towers')