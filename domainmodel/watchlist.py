from domainmodel.movie import Movie
from domainmodel.actor import Actor
from domainmodel.director import Director
from domainmodel.genre import Genre
from domainmodel.review import Review
from domainmodel.user import User

class WatchList:
    def __init__(self):
        self.__watchlist = []

    @property
    def watchlist(self):
        return self.__watchlist

    @watchlist.setter
    def watchlist(self, watchlist):
        if watchlist == "" or type(watchlist) is not list:
            self.__watchlist = []
        else:
            self.__watchlist = watchlist

    def add_movie(self, movie):
        if type(movie) is not Movie:
            return
        elif movie in self.__watchlist:
            return
        else:
            self.__watchlist.append(movie)

    def remove_movie(self, movie):
        if type(movie) is not Movie:
            return
        elif movie not in self.__watchlist:
            return
        else:
            self.__watchlist.pop(self.__watchlist.index(movie))

    def select_movie_to_watch(self, index):
        if type(index) is not int:
            return None
        elif index >= len(self.__watchlist):
            return None
        else:
            return self.__watchlist[index]

    def size(self):
        return len(self.__watchlist)

    def first_movie_in_watchlist(self):
        if len(self.__watchlist) == 0:
            return None
        else:
            return self.__watchlist[0]

    def __iter__(self):
        self.__index = 0
        return self

    def __next__(self):
        if self.__index < len(self.__watchlist):
            movie = self.__watchlist[self.__index]
            self.__index += 1
            return movie
        else:
            raise StopIteration

    def watch_next_movie(self, user):
        if type(user) is not User:
            return
        else:
            movie = self.first_movie_in_watchlist()
            self.remove_movie(movie)
            user.watch_movie(movie)