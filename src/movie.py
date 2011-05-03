import imdb

class Movie:
    def __init__(self, name, year):
        self.name = name
        self.year = year
    
    def __str__(self):
        return self.name + ' (' + str(self.year) + ')'
    
    @staticmethod
    def create_movie_from_query(query):
        db = imdb.IMDb()
        movie_obj = db.search_movie(query, results=1)[0]
        created_movie = Movie(name=movie_obj['title'], year=movie_obj['year'])
        return created_movie