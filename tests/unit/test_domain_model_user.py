import pytest

from domainmodel.movie import Movie
from domainmodel.actor import Actor
from domainmodel.director import Director
from domainmodel.genre import Genre
from domainmodel.review import Review
from domainmodel.user import User

def test_username_valid():
    user1 = User("test1", "password1")
    user1.username = "test2"
    assert user1.username == "test2"

def test_username_invalid():
    user1 = User("test1", "password1")
    user1.username = 100
    assert user1.username is None

def test_username_whitespace_case():
    user1 = User("test1", "password1")
    user1.username = "  TEST1  "
    assert user1.username == "test1"

def test_password_valid():
    user1 = User("test1", "password1")
    user1.password = "password2"
    assert user1.password == "password2"

def test_password_invalid():
    user1 = User("test1", "password1")
    user1.password = 5334
    assert user1.password is None

def test_init_valid():
    user1 = User("test1", "password1")
    assert user1.username == "test1"
    assert user1.password is "password1"

def test_init_username_format():
    user1 = User(" This Is a Test  ", "password1")
    assert user1.username == "this is a test"

def test_init_username_int():
    user1 = User(131, "password1")
    assert user1.username is None

def test_init_passowrd_int():
    user1 = User("Test1", 9999)
    assert user1.password is None

def test_eq_same():
    user1 = User("Test1", "password1")
    user2 = User("  test1  ", "password2")
    assert user1 == user2

def test_eq_different():
    user1 = User("Test1", "password1")
    user2 = User("Test2", "password1")
    assert user1 != user2

def test_repr_valid():
    user1 = User("  Test1  ", "password1")
    assert repr(user1) == "<User test1>"

def test_lt_valid():
    user1 = User("  Test1  ", "password")
    user2 = User("test2", "password")
    assert user1 < user2

def test_hash_same():
    user1 = User("Test1", "password1")
    user2 = User("  test1  ", "password2")
    assert hash(user1) == hash(user2)

def test_eq_different():
    user1 = User("Test1", "password1")
    user2 = User("Test2", "password1")
    assert hash(user1) != hash(user2)

def test_watched_movies_valid():
    user1 = User("test1", "password1")
    movie1 = Movie("Moana", 2016)
    movie2 = Movie("Moana2", 2020)
    movies = []
    movies.append(movie1)
    movies.append(movie2)
    user1.watched_movies = movies
    assert user1.watched_movies == [movie1, movie2]

def test_watched_movies_invalid():
    user1 = User("test1", "password1")
    movie1 = Movie("Moana", 2016)
    user1.watched_movies = movie1
    assert user1.watched_movies == []

def test_reviews_valid():
    user1 = User("test1", "password1")
    movie1 = Movie("Moana", 2016)
    review1 = Review(movie1, "Text", 8)
    review2 = Review(movie1, "More Text", 7)
    reviews = []
    reviews.append(review1)
    reviews.append(review2)
    user1.reviews = reviews
    assert user1.reviews == [review1, review2]

def test_reviews_invalid():
    user1 = User("test1", "password1")
    movie1 = Movie("Moana", 2016)
    review1 = Review(movie1, "Test", 7)
    user1.reviews = review1
    assert user1.reviews == []

def time_spent_valid():
    user1 = User("test1", "password1")
    user1.time_spent_watching_movies_minutes = 100
    assert user1.time_spent_watching_movies_minutes == 100

def time_spent_negative():
    user1 = User("test1", "password1")
    user1.time_spent_watching_movies_minutes = -1
    assert user1.time_spent_watching_movies_minutes == 0

def time_spent_string():
    user1 = User("test1", "password1")
    user1.time_spent_watching_movies_minutes = "hundred"
    assert user1.time_spent_watching_movies_minutes == 0

def test_watch_movie_valid():
    user1 = User("test1", "password1")
    movie1 = Movie("Moana", 2016)
    movie1.runtime_minutes = 100
    user1.watch_movie(movie1)
    assert user1.watched_movies == [movie1]
    assert user1.time_spent_watching_movies_minutes == 100
    movie2 = Movie("Moana2", 2020)
    movie2.runtime_minutes = 120
    user1.watch_movie(movie2)
    assert user1.watched_movies == [movie1, movie2]
    assert user1.time_spent_watching_movies_minutes == 220

def test_watch_movie_invalid():
    user1 = User("test1", "password1")
    movie1 = Movie("Moana", 2016)
    movie1.runtime_minutes = 100
    user1.watch_movie(movie1)
    movie2 = ("Moana 2", 120)
    user1.watch_movie(movie2)
    assert user1.watched_movies == [movie1]
    assert user1.time_spent_watching_movies_minutes == 100

def test_review_valid():
    user1 = User("test1", "password1")
    movie1 = Movie("Moana", 2016)
    review1 = Review(movie1, "Text", 8)
    review2 = Review(movie1, "More Text", 7)
    user1.add_review(review1)
    user1.add_review(review2)
    assert user1.reviews == [review1, review2]

def test_review_valid():
    user1 = User("test1", "password1")
    movie1 = Movie("Moana", 2016)
    review1 = Review(movie1, "Text", 8)
    review2 = (movie1, "More Text", 7)
    user1.add_review(review1)
    user1.add_review(review2)
    assert user1.reviews == [review1]