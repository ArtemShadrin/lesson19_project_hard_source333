from unittest.mock import MagicMock

import pytest
from dao.movie import MovieDAO
from dao.model.movie import Movie
from service.movie import MovieService


@pytest.fixture()
def movie_dao():
    movie_init = MovieDAO(None)

    movie_1 = Movie(id=1, title="name_1")
    movie_2 = Movie(id=2, title="name_2")

    movie_init.get_one = MagicMock(return_value=movie_1)
    movie_init.get_all = MagicMock(return_value=[movie_1, movie_2])
    movie_init.create = MagicMock(return_value=movie_1)
    movie_init.delete = MagicMock(return_value=True)
    movie_init.update = MagicMock(return_value=True)

    return movie_init


class TestMovieService:
    @pytest.fixture(autouse=True)
    def movie_service(self, movie_dao):
        self.movie_service = MovieService(movie_dao)

    def test_get_one(self):
        movie = self.movie_service.get_one(1)
        assert movie is not None
        assert movie.id is not None

    def test_all(self):
        assert len(self.movie_service.get_all()) == 2

    def test_delete(self):
        assert self.movie_service.delete(1) is True

    def test_update(self):
        assert self.movie_service.update(1) is True
