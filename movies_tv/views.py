from django.shortcuts import render
from django.views.generic.base import View
from .models import *
from django.views.generic import ListView, DetailView


class MoviesView(ListView):
    # Список фильмов
    model = Movie
    queryset = Movie.objects.all()
    template_name = 'movies_tv/movie_list.html'


class MovieDatailView(DetailView):
    # Полное описание фильмов
    model = Movie
    slug_field = 'url'
