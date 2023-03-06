from django import forms
from django.contrib import admin
from .models import *
from django.utils.safestring import mark_safe

from ckeditor_uploader.widgets import CKEditorUploadingWidget


class MovieAdminForm(forms.ModelForm):
    description = forms.CharField(label='Описание', widget=CKEditorUploadingWidget())
    class Meta:
        model = Movie
        fields = '__all__'



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
    form = MovieAdminForm
    prepopulated_fields = {"url" : ("title",)}


@admin.register(Reviews)
class ReviewsAdmin(admin.ModelAdmin):
    # Отзывы
    list_display = ('id', 'name', 'email', 'parent', 'movie')
    readonly_fields = ('name', 'email')
    list_display_links = ('name',)



@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    # Жанры
    list_display = ('id', 'name', 'url')
    list_display_links = ('name',)


@admin.register(Actor)
class ActorAdmin(admin.ModelAdmin):
    # Актеры
    list_display = ('name', 'age', 'get_image')
    readonly_fields = ('get_image', )

    def get_image(self, obj):
        return mark_safe(f"<img src={obj.image.url} width='50' height='50' ")
    
    get_image.short_description = 'Изображение'


@admin.register(MovieShots)
class MovieShotsAdmin(admin.ModelAdmin):
    # Кадры из фильма
    list_display = ('title', 'movie', 'get_image')
    readonly_fields = ('get_image', )

    def get_image(self, obj):
        return mark_safe(f"<img src={obj.imege.url} width='50' height='50' ")
    
    get_image.short_description = 'Изображение'


@admin.register(Reting)
class RetingAdmin(admin.ModelAdmin):
    # Рейтинг
    list_display = ('ip', 'star')


admin.site.register(RatingsStar)
