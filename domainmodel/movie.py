from domainmodel.genre import Genre
from domainmodel.actor import Actor
from domainmodel.director import Director

class Movie:

    def __init__(self, title: str, release_year: int):
        if title == "" or type(title) is not str:
            self.__title = None
        else:
            self.__title = title.strip()
        if release_year == "" or type(release_year) is not int or release_year < 1900:
            self.__release_year = None
        else:
            self.__release_year = release_year
        self.__description = None
        self.__director = None
        self.__actors = []
        self.__genres = []
        self.__runtime_minutes = None

    def __repr__(self):
        return f"<Movie {self.__title}, {self.__release_year}>"

    def __eq__(self, other):
        return self.__title == other.title and self.__release_year == other.release_year

    def __lt__(self, other):
        if self.__title == other.title:
            return self.__release_year < other.release_year
        else:
            return self.__title < other.title

    def __hash__(self):
        return hash((self.__title, self.__release_year))

    @property
    def title(self) -> str:
        return self.__title

    @title.setter
    def title(self, title):
        if title == "" or type(title) is not str:
            self.__title = None
        else:
            self.__title = title.strip()

    @property
    def release_year(self) -> int:
        return self.__release_year

    @release_year.setter
    def release_year(self, release_year):
        if release_year == "" or type(release_year) is not int or release_year < 1900:
            self.__release_year = None
        else:
            self.__release_year = release_year

    @property
    def description(self) -> str:
        return self.__description

    @description.setter
    def description(self, description):
        if description == "" or type(description) is not str:
            self.__description = None
        else:
            self.__description = description.strip()

    @property
    def director(self):
        return self.__director

    @director.setter
    def director(self, director):
        if type(director) is not Director:
            self.__director = None
        else:
            self.__director = director

    @property
    def actors(self):
        return self.__actors

    @actors.setter
    def actors(self, actors):
        if type(actors) is not list:
            self.__actors = []
        else:
            self.__actors = actors

    @property
    def genres(self):
        return self.__genres

    @genres.setter
    def genres(self, genres):
        if type(genres) is not list:
            self.__genres = []
        else:
            self.__genres = genres

    @property
    def runtime_minutes(self):
        return self.__runtime_minutes

    @runtime_minutes.setter
    def runtime_minutes(self, runtime_minutes):
        if type(runtime_minutes) is not int:
            raise ValueError
        elif runtime_minutes < 1:
            raise ValueError
        else:
            self.__runtime_minutes = runtime_minutes

    def add_actor(self, actor):
        if type(actor) is not Actor:
            raise TypeError
        else:
            self.__actors.append(actor)

    def remove_actor(self, actor):
        if type(actor) is not Actor:
            return
        elif actor not in self.__actors:
            return
        else:
            self.__actors.pop(self.__actors.index(actor))

    def add_genre(self, genre):
        if type(genre) is not Genre:
            raise TypeError
        else:
            self.__genres.append(genre)

    def remove_genre(self, genre):
        if type(genre) is not Genre:
            return
        elif genre not in self.__genres:
            return
        else:
            self.__genres.pop(self.__genres.index(genre))