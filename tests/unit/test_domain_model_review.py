import pytest

from datetime import datetime

from domainmodel.movie import Movie
from domainmodel.actor import Actor
from domainmodel.director import Director
from domainmodel.genre import Genre
from domainmodel.review import Review

def test_init_review_valid():
    movie1 = Movie("Moana", 2016)
    review1 = Review(movie1, "Review Text", 5)
    assert review1.movie == movie1
    assert review1.review_text == "Review Text"
    assert review1.rating == 5
    assert type(review1.timestamp) is datetime

def test_init_review_empty():
    review1 = Review("", "", "")
    assert review1.movie is None
    assert review1.review_text == ""
    assert review1.rating is None
    assert type(review1.timestamp) is datetime

def test_init_review_movie_invalid():
    review1 = Review("Movie", "Review Text", 5)
    assert review1.movie is None

def test_init_review_review_text_invalid():
    review1 = Review("Movie", ("review", "text"), 5)
    assert review1.movie is None

def test_init_review_rating_high():
    movie1 = Movie("Moana", 2016)
    review1 = Review(movie1, "Review Text", 11)
    assert review1.rating is None

def test_init_review_rating_low():
    movie1 = Movie("Moana", 2016)
    review1 = Review(movie1, "Review Text", 0)
    assert review1.rating is None

def test_set_movie():
    review1 = Review("", "", "")
    movie1 = Movie("Moana", 2016)
    review1.movie = movie1
    assert review1.movie == movie1

def test_set_movie_string():
    review1 = Review("", "", "")
    review1.movie = "movie1"
    assert review1.movie == None

def test_set_review_text():
    review1 = Review("", "", "")
    review1.review_text = "Test Review"
    assert review1.review_text == "Test Review"

def test_set_review_text_list():
    review1 = Review("", "", "")
    review1.review_text = ["Test Review"]
    assert review1.review_text is None

def test_set_rating_valid():
    review1 = Review("", "", "")
    review1.rating = 10
    assert review1.rating == 10

def test_set_rating_high():
    review1 = Review("", "", "")
    review1.rating = 11
    assert review1.rating is None

def test_set_rating_low():
    review1 = Review("", "", "")
    review1.rating = 0
    assert review1.rating is None

def test_set_rating_string():
    review1 = Review("", "", "")
    review1.rating = "Zero"
    assert review1.rating is None

def test_set_timestamp_valid():
    review1 = Review("", "", "")
    timestamp = datetime.today()
    review1.timestamp = timestamp
    assert review1.timestamp == timestamp

def test_set_timestamp_string():
    review1 = Review("", "", "")
    timestamp = "30-08-2020"
    review1.timestamp = timestamp
    assert review1.timestamp is None

def test_eq_same():
    movie1 = Movie("Moana", 2016)
    review1 = Review(movie1, "Good Movie", 8)
    review2 = Review(movie1, "Good Movie", 8)
    timestamp = datetime.today()
    review1.timestamp = timestamp
    review2.timestamp = timestamp
    assert review1 == review2

def test_eq_same_movie():
    movie1 = Movie("Moana", 2016)
    movie2 = Movie("Moana", 2016)
    review1 = Review(movie1, "Good Movie", 8)
    review2 = Review(movie2, "Good Movie", 8)
    timestamp = datetime.today()
    review1.timestamp = timestamp
    review2.timestamp = timestamp
    assert review1 == review2

def test_eq_different_movie():
    movie1 = Movie("Moana", 2016)
    movie2 = Movie("Moana", 2020)
    review1 = Review(movie1, "Good Movie", 8)
    review2 = Review(movie2, "Good Movie", 8)
    timestamp = datetime.today()
    review1.timestamp = timestamp
    review2.timestamp = timestamp
    assert review1 != review2

def test_eq_different_rating():
    movie1 = Movie("Moana", 2016)
    movie2 = Movie("Moana", 2016)
    review1 = Review(movie1, "Good Movie", 8)
    review2 = Review(movie2, "Good Movie", 7)
    timestamp = datetime.today()
    review1.timestamp = timestamp
    review2.timestamp = timestamp
    assert review1 != review2

def test_eq_different_review():
    movie1 = Movie("Moana", 2016)
    movie2 = Movie("Moana", 2016)
    review1 = Review(movie1, "Good Movie", 8)
    review2 = Review(movie2, "Bad Movie", 8)
    timestamp = datetime.today()
    review1.timestamp = timestamp
    review2.timestamp = timestamp
    assert review1 != review2

def test_repr_valid():
    movie1 = Movie("Moana", 2016)
    review1 = Review(movie1, "Good Movie", 8)
    timestamp = datetime.today()
    review1.timestamp = timestamp
    assert repr(review1) == f"<Movie Moana, 2016, Reviewed {timestamp}>"