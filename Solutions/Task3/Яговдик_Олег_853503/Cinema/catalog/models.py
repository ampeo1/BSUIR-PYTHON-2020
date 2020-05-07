# -*- coding: utf-8 -*-
from django.db import models
from django.urls import reverse


class Producer(models.Model):
    name = models.CharField(max_length=20)
    photo = models.ImageField(upload_to='media')
    biography = models.TextField()

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('producer-detail', args=[str(self.id)])

    def get_delete(self):
        return reverse('producer-delete', args=[str(self.id)])

    def get_update(self):
        return reverse('producer-update', args=[str(self.id)])


class Film(models.Model):
    name = models.CharField(max_length=20)
    poster = models.ImageField(upload_to='media')
    description = models.TextField()
    producer = models.ForeignKey('Producer', on_delete=models.SET_NULL, null=True, help_text="Выберите режиссёра")
    genre = models.ManyToManyField('Genre', help_text="Выберите жанр фильм")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('film-detail', args=[str(self.id)])

    def get_delete(self):
        return reverse('film-delete', args=[str(self.id)])

    def get_update(self):
        return reverse('film-update', args=[str(self.id)])

    class Meta:
        permissions = (('admin', 'user'),)


class Genre(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('index')
# Create your models here.


