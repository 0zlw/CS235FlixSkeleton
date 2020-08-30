import pytest

from domainmodel.movie import Movie
from domainmodel.actor import Actor
from domainmodel.director import Director
from domainmodel.genre import Genre
from domainmodel.review import Review
from domainmodel.user import User
from domainmodel.watchlist import WatchList

def test_init_valid():
    watchlist1 = WatchList()
    assert type(watchlist1) is WatchList

def test_set_watchlist_valid():
    watchlist1 = WatchList()
    movie1 = Movie("Moana", 2016)
    movie2 = Movie("Moana 2", 2020)
    movies = []
    movies.append(movie1)
    movies.append(movie2)
    watchlist1.watchlist = movies
    assert watchlist1.watchlist == [movie1, movie2]

def test_set_watchlist_movie():
    watchlist1 = WatchList()
    movie1 = Movie("Moana", 2016)
    watchlist1.watchlist = movie1
    assert watchlist1.watchlist == []

def test_add_movie_single():
    watchlist1 = WatchList()
    movie1 = Movie("Moana", 2016)
    watchlist1.add_movie(movie1)
    assert watchlist1.watchlist == [movie1]

def test_add_movie_multiple():
    watchlist1 = WatchList()
    movie1 = Movie("Moana", 2016)
    movie2 = Movie("Moana 2", 2020)
    watchlist1.add_movie(movie1)
    watchlist1.add_movie(movie2)
    assert watchlist1.watchlist == [movie1, movie2]

def test_add_movie_repeat():
    watchlist1 = WatchList()
    movie1 = Movie("Moana", 2016)
    watchlist1.add_movie(movie1)
    watchlist1.add_movie(movie1)
    assert watchlist1.watchlist == [movie1]

def test_add_movie_same_hash():
    watchlist1 = WatchList()
    movie1 = Movie("Moana", 2016)
    movie2 = Movie("Moana", 2016)
    watchlist1.add_movie(movie1)
    watchlist1.add_movie(movie2)
    assert watchlist1.watchlist == [movie1]

def test_add_movie_invalid():
    watchlist1 = WatchList()
    movie1 = ("Moana", 2016)
    watchlist1.add_movie(movie1)
    assert watchlist1.watchlist == []

def test_remove_movie_single():
    watchlist1 = WatchList()
    movie1 = Movie("Moana", 2016)
    watchlist1.add_movie(movie1)
    watchlist1.remove_movie(movie1)
    assert watchlist1.watchlist == []

def test_remove_movie_multiple():
    watchlist1 = WatchList()
    movie1 = Movie("Moana", 2016)
    movie2 = Movie("Moana 2", 2020)
    watchlist1.add_movie(movie1)
    watchlist1.add_movie(movie2)
    watchlist1.remove_movie(movie1)
    assert watchlist1.watchlist == [movie2]
    watchlist1.remove_movie(movie2)
    assert watchlist1.watchlist == []

def test_remove_movie_not_in_list():
    watchlist1 = WatchList()
    movie1 = Movie("Moana", 2016)
    watchlist1.remove_movie(movie1)
    assert watchlist1.watchlist == []

def test_remove_movie_different_hash():
    watchlist1 = WatchList()
    movie1 = Movie("Moana", 2016)
    movie2 = Movie("Moana", 2016)
    watchlist1.add_movie(movie1)
    watchlist1.remove_movie(movie2)
    assert watchlist1.watchlist == []

def test_select_single():
    watchlist1 = WatchList()
    movie1 = Movie("Moana", 2016)
    watchlist1.add_movie(movie1)
    assert watchlist1.select_movie_to_watch(0) == movie1

def test_select_multiple():
    watchlist1 = WatchList()
    movie1 = Movie("Moana", 2016)
    movie2 = Movie("Moana 2", 2020)
    watchlist1.add_movie(movie1)
    watchlist1.add_movie(movie2)
    assert watchlist1.select_movie_to_watch(1) == movie2

def test_select_out_of_range():
    watchlist1 = WatchList()
    movie1 = Movie("Moana", 2016)
    movie2 = Movie("Moana 2", 2020)
    watchlist1.add_movie(movie1)
    watchlist1.add_movie(movie2)
    assert watchlist1.select_movie_to_watch(2) is None

def test_select_string():
    watchlist1 = WatchList()
    movie1 = Movie("Moana", 2016)
    movie2 = Movie("Moana 2", 2020)
    watchlist1.add_movie(movie1)
    watchlist1.add_movie(movie2)
    assert watchlist1.select_movie_to_watch("two") is None

def test_size_zero():
    watchlist1 = WatchList()
    assert watchlist1.size() == 0

def test_size_single():
    watchlist1 = WatchList()
    movie1 = Movie("Moana", 2016)
    watchlist1.add_movie(movie1)
    assert watchlist1.size() == 1

def test_size_multiple():
    watchlist1 = WatchList()
    movie1 = Movie("Moana", 2016)
    movie2 = Movie("Moana 2", 2020)
    watchlist1.add_movie(movie1)
    watchlist1.add_movie(movie2)
    assert watchlist1.size() == 2

def test_first_movie_single():
    watchlist1 = WatchList()
    movie1 = Movie("Moana", 2016)
    watchlist1.add_movie(movie1)
    assert watchlist1.first_movie_in_watchlist() == movie1

def test_first_movie_multiple():
    watchlist1 = WatchList()
    movie1 = Movie("Moana", 2016)
    movie2 = Movie("Moana 2", 2016)
    watchlist1.add_movie(movie1)
    watchlist1.add_movie(movie2)
    assert watchlist1.first_movie_in_watchlist() == movie1

def test_first_movie_none():
    watchlist1 = WatchList()
    assert watchlist1.first_movie_in_watchlist() is None

def test_iter_multiple():
    watchlist1 = WatchList()
    movie1 = Movie("Moana", 2016)
    movie2 = Movie("Moana 2", 2016)
    watchlist1.add_movie(movie1)
    watchlist1.add_movie(movie2)
    movies = []
    for movie in watchlist1:
        movies.append(movie)
    assert movies == [movie1, movie2]

def test_iter_multiple():
    watchlist1 = WatchList()
    movie1 = Movie("Moana", 2016)
    watchlist1.add_movie(movie1)
    movies = []
    for movie in watchlist1:
        movies.append(movie)
    assert movies == [movie1]

def test_iter_zero():
    watchlist1 = WatchList()
    movies = []
    for movie in watchlist1:
        movies.append(movie)
    assert movies == []

def test_watch_next_movie_single():
    watchlist1 = WatchList()
    user1 = User("user", "password")
    movie1 = Movie("Moana", 2020)
    movie1.runtime_minutes = 100
    watchlist1.add_movie(movie1)
    watchlist1.watch_next_movie(user1)
    assert watchlist1.watchlist == []
    assert user1.watched_movies == [movie1]
    assert user1.time_spent_watching_movies_minutes == 100

def test_watch_next_movie_multiple():
    watchlist1 = WatchList()
    user1 = User("user", "password")
    movie1 = Movie("Moana", 2016)
    movie1.runtime_minutes = 100
    movie2 = Movie("Moana 2", 2020)
    movie2.runtime_minutes = 120
    watchlist1.add_movie(movie2)
    watchlist1.add_movie(movie1)
    watchlist1.watch_next_movie(user1)
    assert watchlist1.watchlist == [movie1]
    assert user1.watched_movies == [movie2]
    assert user1.time_spent_watching_movies_minutes == 120
    watchlist1.watch_next_movie(user1)
    assert watchlist1.watchlist == []
    assert user1.watched_movies == [movie2, movie1]
    assert user1.time_spent_watching_movies_minutes == 220