from domainmodel.genre import Genre
from domainmodel.actor import Actor
from domainmodel.director import Director
from domainmodel.movie import Movie
from domainmodel.review import Review

class User:
    def __init__(self, username, password):
        if username == "" or type(username) is not str:
            self.__username = None
        else:
            self.__username = username.strip().lower()
        if password == "" or type(password) is not str:
            self.__password = None
        else:
            self.__password = password.strip()
        self.__watched_movies = []
        self.__reviews = []
        self.__time_spent_watching_movies_minutes = 0

    def __repr__(self):
        return f"<User {self.__username}>"

    def __eq__(self, other):
        return self.__username == other.username

    def __lt__(self, other):
        return self.__username < other.username

    def __hash__(self):
        return hash(self.__username)

    @property
    def username(self):
        return self.__username

    @username.setter
    def username(self, username):
        if username == "" or type(username) is not str:
            self.__username = None
        else:
            self.__username = username.strip().lower()

    @property
    def password(self):
        return self.__password

    @password.setter
    def password(self, password):
        if password == "" or type(password) is not str:
            self.__password = None
        else:
            self.__password = password.strip()

    @property
    def watched_movies(self):
        return self.__watched_movies

    @watched_movies.setter
    def watched_movies(self, watched_movies):
        if type(watched_movies) is not list:
            self.__watched_movies = []
        else:
            self.__watched_movies = watched_movies

    @property
    def reviews(self):
        return self.__reviews

    @reviews.setter
    def reviews(self, reviews):
        if type(reviews) is not list:
            self.__reviews = []
        else:
            self.__reviews = reviews

    @property
    def time_spent_watching_movies_minutes(self):
        return self.__time_spent_watching_movies_minutes

    @time_spent_watching_movies_minutes.setter
    def time_spent_watching_movies_minutes(self, minutes):
        if type (minutes) is not int or minutes < 0:
            self.__time_spent_watching_movies_minutes = 0
        else:
            self.__time_spent_watching_movies_minutes = minutes

    def watch_movie(self, movie):
        if type(movie) is not Movie:
            return
        else:
            self.__watched_movies.append(movie)
            self.__time_spent_watching_movies_minutes += movie.runtime_minutes

    def add_review(self, review):
        if type(review) is not Review:
            return
        else:
            self.__reviews.append(review)