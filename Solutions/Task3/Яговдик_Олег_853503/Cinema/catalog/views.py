from django.forms import ModelForm
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic
from django.views.generic import CreateView, UpdateView, DeleteView

from .models import Film, Producer, Genre


def index(request):
    """
    Функция отображения для домашней страницы сайта.
    """
    # Генерация "количеств" некоторых главных объектов
    num_films = Film.objects.all().count()
    num_producer = Producer.objects.all().count()

    # Отрисовка HTML-шаблона index.html с данными внутри
    # переменной контекста context
    return render(
        request,
        'index.html',
        context={'num_films': num_films, 'num_producer': num_producer}
    )


class FilmListView(generic.ListView):
    model = Film


class FilmDetailView(generic.DetailView):
    model = Film


class ProducerDetailView(generic.DetailView):
    model = Producer


class ProducerListView(generic.ListView):
    model = Producer


class FilmForm(CreateView):
    model = Film
    fields = ['name', 'poster', 'description', 'producer', 'genre']


class FilmUpdate(UpdateView):
    model = Film
    fields = ['name', 'poster', 'description', 'producer', 'genre']


class FilmDelete(DeleteView):
    model = Film
    success_url = reverse_lazy('index')


class ProducerForm(CreateView):
    model = Producer
    fields = ['name', 'photo', 'biography']


class ProducerUpdate(UpdateView):
    model = Producer
    fields = ['name', 'photo', 'biography']


class ProducerDelete(DeleteView):
    model = Producer
    success_url = reverse_lazy('index')


class GenreForm(CreateView):
    model = Genre
    fields = ['name']
