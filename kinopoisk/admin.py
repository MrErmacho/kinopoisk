from django.contrib import admin

from .models import Movie, MoviePerson, MovieReview, Genre


admin.site.register(Movie)
admin.site.register(MoviePerson)
admin.site.register(MovieReview)
admin.site.register(Genre)
