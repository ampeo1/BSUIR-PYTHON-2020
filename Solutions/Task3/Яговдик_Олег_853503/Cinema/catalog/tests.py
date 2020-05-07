from django.test import Client

from django.test import TestCase
from catalog.models import Film, Producer, Genre


class FilmTestCase(TestCase):
    def setUp(self):
        prod = Producer.objects.create(name="prod", photo="media/iphone360_30650.jpg", biography="bio")
        gen = Genre.objects.create(name="genre")
        Film.objects.create(name="name", poster="media/ButterflyEffect.jpg", description="kek", producer=prod)
        film = Film.objects.get(name="name")
        film.genre.add(gen)

    def test_save(self):
        prod = Producer.objects.get(name="prod")
        gen = Genre.objects.get(name="genre")
        film = Film.objects.get(name="name")
        assert prod.name == "prod"
        assert prod.__str__() == "prod"
        assert gen.name == "genre"
        assert gen.__str__() == "genre"
        assert film.name == "name"
        assert film.__str__() == "name"
        assert film.poster == "media/ButterflyEffect.jpg"
        assert film.producer == prod
        assert film.description == "kek"
        assert prod.photo == "media/iphone360_30650.jpg"

    def test_login(self):
        c = Client()
        response = c.post("/accounts/login/?next=/catalog/")
        assert response.status_code == 200
        response = c.post("/accounts/login/?next=/catalog/, {'username': kek, 'password': 'aaa12345'}")
        assert response.status_code == 200

    def test_films(self):
        c = Client()
        response = c.get('/catalog/films/')
        assert response.status_code == 200

    def test_prod(self):
        c = Client()
        response = c.get('/catalog/producers/')
        assert response.status_code == 200
        #response = c.get('/catalog/producer/1')
        #assert response.status_code == 200

    def test_index(self):
        c = Client()
        response = c.get('/catalog/')
        assert response.status_code == 200
