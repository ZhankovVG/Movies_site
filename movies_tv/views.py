from django.shortcuts import render, redirect
from django.views.generic.base import View
from .models import *
from django.views.generic import ListView, DetailView, CreateView
from .forms import *
from django.db.models import Q
from django.contrib.auth.forms import UserCreationForm



class GenreYear:
    # Жанры и года выхода фильмов
    def get_genres(self):
        return Genre.objects.all()
    
    def get_years(self):
        return Movie.objects.filter(draft=False).values('year')


class MoviesView(GenreYear, ListView):
    # Список фильмов
    model = Movie
    queryset = Movie.objects.filter(draft=False)
    template_name = 'movies_tv/movie_list.html'


class MovieDatailView(GenreYear, DetailView):
    # Полное описание фильмов
    model = Movie
    slug_field = 'url'
    form = ReviewsForm


class AddReview(View):
    # Отзывы
    def post(self, request, pk):
        form = ReviewsForm(request.POST)
        movie = Movie.objects.get(id = pk)
        if form.is_valid():
            form = form.save(commit=False)
            form.movie = movie
            form.save()
        return redirect(movie.get_absolute_url())


class ActorView(GenreYear, DetailView):
    model = Actor
    template_name = 'movies_tv/actor.html'
    slug_field = 'name'


class FilterMoviesView(GenreYear, ListView):
    # Фильтр фильмов
    def get_queryset(self):
        queryset = Movie.objects.filter(
            Q(year__in=self.request.GET.getlist('year')) | 
            Q(genres__in=self.request.GET.getlist('genre'))
        )
        return queryset
    

class Search(GenreYear, ListView):
    # поиск фильмов
    def get_queryset(self):
        return Movie.objects.filter(title__icontains=self.request.GET.get('search'))