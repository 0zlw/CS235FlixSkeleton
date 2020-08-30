import csv

from domainmodel.movie import Movie
from domainmodel.actor import Actor
from domainmodel.genre import Genre
from domainmodel.director import Director

class MovieFileCSVReader:

    def __init__(self, file_name: str):
        self.__file_name = file_name
        self.__dataset_of_movies = []
        self.__dataset_of_actors = []
        self.__dataset_of_directors = []
        self.__dataset_of_genres = []

    def read_csv_file(self):
        with open(self.__file_name, mode='r', encoding='utf-8-sig') as csvfile:
            movie_file_reader = csv.DictReader(csvfile)

            for row in movie_file_reader:
                movie = Movie(row['Title'], int(row['Year']))
                self.__dataset_of_movies.append(movie)
                director = Director(row['Director'])
                if director not in self.__dataset_of_directors:
                    self.__dataset_of_directors.append(director)
                actors = row['Actors'].split(",")
                for actor_full_name in actors:
                    actor = Actor(actor_full_name)
                    if actor not in self.__dataset_of_actors:
                        self.__dataset_of_actors.append(actor)
                genres = row['Genre'].split(",")
                for genre_name in genres:
                    genre = Genre(genre_name)
                    if genre not in self.__dataset_of_genres:
                        self.__dataset_of_genres.append(genre)

    @property
    def dataset_of_movies(self):
        return self.__dataset_of_movies

    @property
    def dataset_of_actors(self):
        return self.__dataset_of_actors

    @property
    def dataset_of_directors(self):
        return self.__dataset_of_directors

    @property
    def dataset_of_genres(self):
        return self.__dataset_of_genres