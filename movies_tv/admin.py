from django.contrib import admin
from .models import *



@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    # Категории
    list_display = ('id', 'name', 'url')
    list_display_links = ('name',)


class ReviewInline(admin.StackedInline):
    # Прикрипление отзывов к фильму
    model = Reviews
    readonly_fields = ('name', 'email')
    extra = 1


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    # Фильмы
    list_display = ('title', 'category', 'url', 'draft')
    list_filter = ('category', 'year')
    search_fields = ('title', 'category__name')
    inlines = [ReviewInline]
    list_editable = ('draft',)


@admin.register(Reviews)
class ReviewsAdmin(admin.ModelAdmin):
    # Отзывы
    list_display = ('id', 'name', 'email', 'parent', 'movie')
    readonly_fields = ('name', 'email')


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    # Жанры
    list_display = ('id', 'name', 'url')


@admin.register(Actor)
class ActorAdmin(admin.ModelAdmin):
    # Актеры
    list_display = ('name', 'age')


@admin.register(MovieShots)
class MovieShotsAdmin(admin.ModelAdmin):
    # Кадры из фильма
    list_display = ('title', 'movie')


@admin.register(Reting)
class RetingAdmin(admin.ModelAdmin):
    # Рейтинг
    list_display = ('ip', 'star')


admin.site.register(RatingsStar)
