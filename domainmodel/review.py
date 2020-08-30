from datetime import datetime

from domainmodel.movie import Movie
from domainmodel.actor import Actor
from domainmodel.director import Director
from domainmodel.genre import Genre

class Review:
    def __init__(self, movie, review_text, rating):
        if type(movie) is not Movie:
            self.__movie = None
        else:
            self.__movie = movie
        if type(review_text) is not str:
            self.__review_text = None
        else:
            self.__review_text = review_text
        if type(rating) is not int:
            self.__rating = None
        elif rating < 1 or rating > 10:
            self.__rating = None
        else:
            self.__rating = rating
        self.__timestamp = datetime.today()

    def __repr__(self):
        return f"<Movie {self.__movie.title}, {self.__movie.release_year}, Reviewed {self.__timestamp}>"

    def __eq__(self, other):
        return self.__movie == other.movie and self.__review_text == other.review_text and self.__rating == other.rating and self.__timestamp == other.timestamp

    @property
    def movie(self):
        return self.__movie

    @movie.setter
    def movie(self, movie):
        if type(movie) is not Movie:
            self.__movie = None
        else:
            self.__movie = movie

    @property
    def review_text(self):
        return self.__review_text

    @review_text.setter
    def review_text(self, review_text):
        if type(review_text) is not str:
            self.__review_text = None
        else:
            self.__review_text = review_text

    @property
    def rating(self):
        return self.__rating

    @rating.setter
    def rating(self, rating):
        if type(rating) is not int:
            self.__rating = None
        elif rating < 1 or rating > 10:
            self.__rating = None
        else:
            self.__rating = rating

    @property
    def timestamp(self):
        return self.__timestamp

    @timestamp.setter
    def timestamp(self, timestamp):
        if type(timestamp) is not datetime:
            self.__timestamp = None
        else:
            self.__timestamp = timestamp