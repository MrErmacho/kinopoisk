from django.urls import path
from .views import *

app_name = 'kinopoisk'

urlpatterns = [
    path('', main, name='main'),  # Главная страница.

    path('movies/', movie_list, name='movie_list'),  # Список всех фильмов.

    path('person_list/<str:person_type>', person_list, name='person_list'),

    path('genres/', genre_list, name='genre_list'),  # Список всех жанров.

    path('movie/<int:movie_id>/', movie_detail, name='movie_detail'),  # Детали фильма.

    path('add_review/', add_review, name='add_review'),
    
    path('director/<int:person_id>/', person_detail, name='person_detail'),

    path('genre/<int:genre_id>/', genre_detail, name='genre_detail'),  # Фильмы по жанру.
]