import pytest

from domainmodel.genre import Genre
from domainmodel.actor import Actor
from domainmodel.director import Director
from domainmodel.movie import Movie

def test_init():
    movie1 = Movie("Moana", 2016)
    assert repr(movie1) == "<Movie Moana, 2016>"
    assert movie1.title == "Moana"
    assert movie1.release_year == 2016
    movie2 = Movie(1800, 2016)
    assert movie2.title is None
    assert movie2.release_year == 2016
    movie3 = Movie("Moana", "Moana")
    assert movie3.title == "Moana"
    assert movie3.release_year is None
    movie4 = Movie("", "")
    assert movie4.title is None
    assert movie4.release_year is None
    movie5 = Movie("Moana", 1800)
    assert movie5.title == "Moana"
    assert movie5.release_year is None

def test_set_title_string():
    movie1 = Movie("Moana", 2016)
    movie1.title = "Not Moana"
    assert movie1.title == "Not Moana"

def test_set_title_string_whitespace():
    movie1 = Movie("Moana", 2016)
    movie1.title = "  Not Moana  "
    assert movie1.title == "Not Moana"

def test_set_title_int():
    movie1 = Movie("Moana", 2016)
    movie1.title = 2016
    assert movie1.title is None

def test_set_release_year_string():
    movie1 = Movie("Moana", 2016)
    movie1.release_year = "Not Moana"
    assert movie1.release_year is None

def test_set_release_year_int_valid():
    movie1 = Movie("Moana", 2016)
    movie1.release_year = 2020
    assert movie1.release_year == 2020

def test_set_release_year_int_not_valid():
    movie1 = Movie("Moana", 2016)
    movie1.release_year = 1000
    assert movie1.release_year is None

def test_set_description_string():
    movie1 = Movie("Moana", 2016)
    movie1.description = "Short Description"
    assert movie1.description == "Short Description"

def test_set_description_string_whitespace():
    movie1 = Movie("Moana", 2016)
    movie1.description = "  Whitespace  "
    assert movie1.description == "Whitespace"

def test_set_description_int():
    movie1 = Movie("Moana", 2016)
    movie1.description = 2016
    assert movie1.description is None

def test_set_director_valid():
    movie1 = Movie("Moana", 2016)
    director1 = Director("Taika Waititi")
    movie1.director = director1
    assert movie1.director.director_full_name == "Taika Waititi"

def test_set_director_invalid():
    movie1 = Movie("Moana", 2016)
    director1 = 2016
    movie1.director = director1
    assert movie1.director is None

def test_set_director_multiple():
    movie1 = Movie("Moana", 2016)
    director1 = 2016
    director2 = 2017
    movie1.director = director1, director2
    assert movie1.director is None

def test_set_actor_single():
    movie1 = Movie("Moana", 2016)
    actors = []
    actor1 = Actor("Brad Pitt")
    actors.append(actor1)
    movie1.actors = actors
    assert movie1.actors == [actor1]

def test_set_actor_multiple():
    movie1 = Movie("Moana", 2016)
    actors = []
    actor1 = Actor("Brad Pitt")
    actor2 = Actor("Angelina Jolie")
    actors.append(actor1)
    actors.append(actor2)
    movie1.actors = actors
    assert movie1.actors == [actor1, actor2]

def test_set_actor_tuple():
    movie1 = Movie("Moana", 2016)
    actor1 = Actor("Brad Pitt")
    actor2 = Actor("Angelina Jolie")
    movie1.actors = actor1, actor2
    assert movie1.actors == []

def test_set_genres_single():
    movie1 = Movie("Moana", 2016)
    genres = []
    genre1 = Genre("Comedy")
    genres.append(genre1)
    movie1.genres = genres
    assert movie1.genres == [genre1]

def test_set_genres_multiple():
    movie1 = Movie("Moana", 2016)
    genres = []
    genre1 = Genre("Comedy")
    genre2 = Genre("Horror")
    genres.append(genre1)
    genres.append(genre2)
    movie1.genres = genres
    assert movie1.genres == [genre1, genre2]

def test_set_genres_genre():
    movie1 = Movie("Moana", 2016)
    genre1 = Genre("Comedy")
    movie1.genres = genre1
    assert movie1.genres == []

def test_set_runtime_minutes():
    movie1 = Movie("Moana", 2016)
    movie1.runtime_minutes = 100
    assert movie1.runtime_minutes == 100

def test_set_runtime_minutes_negative():
    movie1 = Movie("Moana", 2016)
    with pytest.raises(ValueError):
        movie1.runtime_minutes = -100

def test_set_runtime_minutes_string():
    movie1 = Movie("Moana", 2016)
    with pytest.raises(ValueError):
        movie1.runtime_minutes = "one hundred"

def test_eq_equal():
    movie1 = Movie("Moana", 2016)
    movie2 = Movie("Moana", 2016)
    assert movie1 == movie2

def test_eq_not_equal_year():
    movie1 = Movie("Moana", 2016)
    movie2 = Movie("Moana", 2020)
    assert movie1 != movie2

def test_eq_not_equal_name():
    movie1 = Movie("Moana", 2016)
    movie2 = Movie("Not Moana", 2020)
    assert movie1 != movie2

def test_lt_different_movie_name():
    movie1 = Movie("Moana", 2016)
    movie2 = Movie("Not Moana", 2016)
    assert movie1 < movie2

def test_lt_different_year():
    movie1 = Movie("Moana", 2016)
    movie2 = Movie("Moana", 2020)
    assert movie1 < movie2

def test_lt_different_movie():
    movie1 = Movie("Moana", 2016)
    movie2 = Movie("Not Moana", 2020)
    assert movie1 < movie2

def test_lt_same_movie():
    movie1 = Movie("Moana", 2016)
    movie2 = Movie("Moana", 2016)
    assert (movie1 < movie2) is not True

def test_hash_same_movie():
    movie1 = Movie("Moana", 2016)
    movie2 = Movie("Moana", 2016)
    assert hash(movie1) == hash(movie2)

def test_hash_different_movie():
    movie1 = Movie("Moana", 2016)
    movie2 = Movie("Not Moana", 2020)
    assert hash(movie1) != hash(movie2)

def test_hash_different_movie_name():
    movie1 = Movie("Moana", 2016)
    movie2 = Movie("Not Moana", 2016)
    assert hash(movie1) != hash(movie2)

def test_hash_different_year():
    movie1 = Movie("Moana", 2016)
    movie2 = Movie("Moana", 2020)
    assert hash(movie1) != hash(movie2)

def test_add_actor_single():
    movie1 = Movie("Moana", 2016)
    actor1 = Actor("Brad Pitt")
    movie1.add_actor(actor1)
    assert movie1.actors == [actor1]

def test_add_actor_list():
    movie1 = Movie("Moana", 2016)
    actor1 = Actor("Brad Pitt")
    actor2 = Actor("Angelina Jolie")
    with pytest.raises(TypeError):
        movie1.add_actor([actor1, actor2])

def test_remove_actor():
    movie1 = Movie("Moana", 2016)
    actor1 = Actor("Brad Pitt")
    actor2 = Actor("Angelina Jolie")
    movie1.add_actor(actor1)
    movie1.add_actor(actor2)
    movie1.remove_actor(actor1)
    assert movie1.actors == [actor2]
    movie1.remove_actor(actor2)
    assert movie1.actors == []

def test_remove_actor_not_actor():
    movie1 = Movie("Moana", 2016)
    actor1 = Actor("Brad Pitt")
    actor2 = Actor("Angelina Jolie")
    movie1.add_actor(actor1)
    movie1.add_actor(actor2)
    movie1.remove_actor("actor3")
    assert movie1.actors == [actor1, actor2]

def test_remove_actor_same():
    movie1 = Movie("Moana", 2016)
    actor1 = Actor("Brad Pitt")
    actor2 = Actor("Angelina Jolie")
    movie1.add_actor(actor1)
    movie1.add_actor(actor2)
    movie1.remove_actor(actor1)
    movie1.remove_actor(actor1)
    assert movie1.actors == [actor2]

def test_add_genre_single():
    movie1 = Movie("Moana", 2016)
    genre1 = Genre("Horror")
    movie1.add_genre(genre1)
    assert movie1.genres == [genre1]

def test_add_genre_list():
    movie1 = Movie("Moana", 2016)
    genre1 = Actor("Horror")
    genre2 = Actor("Comedy")
    with pytest.raises(TypeError):
        movie1.add_actor([genre1, genre2])

def test_remove_genre():
    movie1 = Movie("Moana", 2016)
    genre1 = Genre("Comedy")
    genre2 = Genre("Horror")
    movie1.add_genre(genre1)
    movie1.add_genre(genre2)
    movie1.remove_genre(genre2)
    assert movie1.genres == [genre1]
    movie1.remove_genre(genre1)
    assert movie1.genres == []

def test_remove_genre_not_genre():
    movie1 = Movie("Moana", 2016)
    genre1 = Genre("Comedy")
    genre2 = Genre("Horror")
    movie1.add_genre(genre1)
    movie1.add_genre(genre2)
    movie1.remove_genre("genre3")
    assert movie1.genres == [genre1, genre2]

def test_remove_genre_same():
    movie1 = Movie("Moana", 2016)
    genre1 = Genre("Comedy")
    genre2 = Genre("Horror")
    movie1.add_genre(genre1)
    movie1.add_genre(genre2)
    movie1.remove_genre(genre1)
    movie1.remove_genre(genre1)
    assert movie1.genres == [genre2]