from django.shortcuts import render, redirect
from django.views.generic.base import View
from .models import *
from django.views.generic import ListView, DetailView
from .forms import ReviewsForm


class GenreYear:
    # Жанры и года выхода фильмов
    def get_genres(self):
        return Genre.objects.all()
    
    def get_years(self):
        return Movie.objects.all().values('year')


class MoviesView(GenreYear, ListView):
    # Список фильмов
    model = Movie
    queryset = Movie.objects.all()
    template_name = 'movies_tv/movie_list.html'


class MovieDatailView(GenreYear, DetailView):
    # Полное описание фильмов
    model = Movie
    slug_field = 'url'


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


class FilterMovieView(GenreYear, ListView):
    # Фильтр фильмов
    def get_queryset(self):
        queryset = Movie.objects.filter(year__in = self.queryset.GET.getlist('year'))
        return queryset