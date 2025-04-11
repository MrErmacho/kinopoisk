from django.shortcuts import render, redirect

from .models import MoviePerson, Genre, Movie, MovieReview

def main(request):
    return render(request, 'kinopoisk/main.html')

def movie_list(request):
    movies = Movie.objects.all()
    return render(request, 'kinopoisk/movie_list.html', {'movies': movies})

def person_list(request, person_type):
    print(person_type)
    if person_type == 'actor':
        persons = MoviePerson.objects.filter(role=MoviePerson.RoleType.ACTOR)
        title =  'Актёры'
    else:
        persons = MoviePerson.objects.filter(role=MoviePerson.RoleType.DIRECTOR)
        title =  'Режиссеры'
    return render(request, 'kinopoisk/person_list.html', {'persons': persons, 'title': title })

def genre_list(request):
    genres = Genre.objects.all()
    return render(request, 'kinopoisk/genre_list.html', {'genres': genres})

def movie_detail(request, movie_id):
    movie = Movie.objects.get(id=movie_id)
    return render(request, 'kinopoisk/movie_detail.html', {'movie': movie, 'reviews': MovieReview.objects.filter(movie_id=movie.id)})

def add_review(request):
    movie_id = request.POST.get('movie_id')
    review_text = request.POST.get('review_text')
    movie = Movie.objects.get(id=movie_id)
    
    MovieReview.objects.create(
        author = request.user,
        text = review_text,
        movie = movie
    )
    return redirect('kinopoisk:movie_detail', movie_id=movie_id)

def person_detail(request, person_id):
    person = MoviePerson.objects.get(id=person_id)

    if person.role == MoviePerson.RoleType.ACTOR:
        movies = person.acted_in_movies.all()
    else:
        movies = person.directed_movies.all()

    return render(request, 'kinopoisk/person_detail.html', {'person': person, 'movies': movies})

def genre_detail(request, genre_id):
    genre = Genre.objects.get(id=genre_id)
    movies = genre.movies.all()
    return render(request, 'kinopoisk/genre_detail.html', {'genre': genre, 'movies': movies})