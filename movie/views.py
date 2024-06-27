from django.shortcuts import render, redirect
import random
import secrets
from django.core.cache import cache
from django.views.decorators.cache import cache_page

from .models import *

import json
   

# Create your views here.

CACHE_TTL = 60 * 15

# Cache the entire index view for 15 minutes
@cache_page(CACHE_TTL)
def index(request):
    # Use prefetch_related to minimize database hits
    movies = Movie.objects.prefetch_related('get_pictures', 'get_background').all()

    # Precompute the pictures
    for movie in movies:
        movie.Picture = movie.get_pictures.filter(id=movie.id)

    # Randomize cool_movies using Python's random module
    cool_movies = list(Movie.objects.filter(cool=True))
    random.shuffle(cool_movies)

    random_movie = secrets.choice(movies)
    random_movie2 = secrets.choice(movies)
    number = random.randint(1, 10)
    
    context = {
        "types": Type.objects.all(),
        "movies": movies,
        'coolmovies': cool_movies,
        'kindaCool': Movie.objects.filter(kindaCool=True),
        "random": random_movie,
        "random2": random_movie2,
        "number": number
    }
    
    return render(request, 'movie/index.html', context)

@cache_page(CACHE_TTL)
def category(request):
    category_id = request.GET.get('categories')
    if category_id:
        movies = Movie.objects.filter(categories=category_id)
    else:
        movies = Movie.objects.filter(kindaCool=True)
    categories = Category.objects.all()
    
    return render(request, 'movie/categories.html', {
        "categories": categories,
        "category_id": category_id,
        "movies": movies
    })

@cache_page(CACHE_TTL)
def actor(request):
    category_id = request.GET.get('category')
    if category_id:
        movies = Movie.objects.filter(actors__id=category_id)
    else:
        movies = Movie.objects.filter(kindaCool=True)
    categories = Actor.objects.all()
    
    return render(request, 'movie/actors.html', {
        'categories': categories,
        'category_id': category_id,
        'movies': movies,
    })

@cache_page(CACHE_TTL)
def director(request):
    category_id = request.GET.get('category')
    if category_id:
        movies = Movie.objects.filter(directors__id=category_id)
    else:
        movies = Movie.objects.filter(kindaCool=True)
    categories = Director.objects.all()
    
    return render(request, 'movie/directors.html', {
        'categories': categories,
        'category_id': category_id,
        'movies': movies,
    })

@cache_page(CACHE_TTL)
def moviePage(request, movie_id):
    movie = cache.get(f'movie_{movie_id}')
    if not movie:
        try:
            movie = Movie.objects.get(id=movie_id)
            cache.set(f'movie_{movie_id}', movie, timeout=CACHE_TTL)
        except Movie.DoesNotExist:
            return redirect('/')
    
    context = {
        "movie": movie,
        "backgroundMovie": movie.get_background.all(),
        "pictureMovie": movie.get_pictures.all()
    }
    return render(request, 'movie/page.html', context)

@cache_page(CACHE_TTL)
def type_view(request):
    type_id = request.GET.get('type_id')
    if type_id:
        movies = Movie.objects.filter(type_id=type_id)
    else:
        movies = Movie.objects.filter(kindaCool=True)
    types = Type.objects.all()

    return render(request, 'movie/types.html', {
        "types": types,
        "type_id": type_id,
        "movies": movies
    })

def workon(request):
    message = "This is still under construction"
    return render(request, 'movie/wait.html', {
        "message": message
    })