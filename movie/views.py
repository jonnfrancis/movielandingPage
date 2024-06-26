from django.shortcuts import render, redirect
from django.core.cache import cache
from django.core.cache.backends.base import DEFAULT_TIMEOUT
from django.conf import settings
import random
import secrets
from django.urls import reverse

from .models import *

import json

CACHE_TTL = getattr(settings, 'CACHE_TTL', 60 * 5)
   

# Create your views here.

def index(request):
    # Cache keys
    movies_cache_key = 'movies_data'
    cool_movies_cache_key = 'cool_movies_data'
    types_cache_key = 'types_data'
    kinda_cool_cache_key = 'kinda_cool_movies_data'

    # Try to get data from cache
    movies = cache.get(movies_cache_key)
    cool_movies = cache.get(cool_movies_cache_key)
    types = cache.get(types_cache_key)
    kinda_cool = cache.get(kinda_cool_cache_key)

    if not movies:
        movies = list(Movie.objects.all())
        for movie in movies:
            movie.Picture = movie.get_pictures.filter(id=movie.id)
        cache.set(movies_cache_key, movies, CACHE_TTL)

    if not cool_movies:
        cool_movies = list(Movie.objects.filter(cool=True))
        random.shuffle(cool_movies)
        cache.set(cool_movies_cache_key, cool_movies, CACHE_TTL)

    if not types:
        types = list(Type.objects.all())
        cache.set(types_cache_key, types, CACHE_TTL)

    if not kinda_cool:
        kinda_cool = list(Movie.objects.filter(kindaCool=True))
        cache.set(kinda_cool_cache_key, kinda_cool, CACHE_TTL)

    random_movie = secrets.choice(movies)    
    random_movie2 = random.choice(movies)
    number = random.randint(1, 10)
        
    return render(request, 'movie/index.html', {
        "types": types,
        "movies": movies,
        'coolmovies': cool_movies,
        'kindaCool': kinda_cool,
        "random": random_movie,
        "random2": random_movie2,
        "number": number
    })


def category(request):
    category_id = request.GET.get('categories', None)
    if category_id is None:
        movies = Movie.objects.filter(kindaCool=True)
    else:
        movies = Movie.objects.filter(categories=category_id)
    categories = Category.objects.all()
    
    return render(request, 'movie/categories.html', {
        "categories": categories,
        "category_id": category_id,
        "movies": movies
    })


def actor(request):
    category_id = request.GET.get('category', None) 
    
    if category_id is None:
        movies = Movie.objects.filter(kindaCool=True)
    else:
        movies = Movie.objects.filter(actors__id=category_id)
    
    categories = Actor.objects.all()
    
    return render(request, 'movie/actors.html', {
        'categories': categories,
        'category_id': category_id,
        'movies': movies,
    })

def director(request):
    category_id = request.GET.get('category', None)
    
    if category_id is None:
        movies = Movie.objects.filter(kindaCool=True)
    else:
        movies = Movie.objects.filter(directors__id=category_id)
    
    categories = Director.objects.all()
    
    return render(request, 'movie/directors.html', {
        'categories': categories,
        'category_id': category_id,
        'movies': movies,
    })  

def moviePage(request, movie_id):
    # Try to get the movie from the cache
    movie = cache.get(movie_id)
    
    if not movie:
        # If not found in cache, fetch from database
        try:
            movie = Movie.objects.get(id=movie_id)
            # Store movie in cache
            cache.set(movie_id, movie, timeout=CACHE_TTL)
        except Movie.DoesNotExist:
            return redirect('/')
    
    return render(request, 'movie/page.html', {
        "movie": movie, 
        "backgroundMovie": movie.get_background.all(),
        "pictureMovie": movie.get_pictures.all()
    })

def type_view(request):
    type_id = request.GET.get('type_id', None)
    if type_id is None:
        movies = Movie.objects.filter(kindaCool=True)
    else:
        movies = Movie.objects.filter(type_id=type_id)
    types = Type.objects.all()

    return render(request, 'movie/types.html', {
        "types": types,
        "type_id": type_id,
        "movies": movies
    })

def workon(request): 
    message = "This is still under construction"
    return render(request, 'movie/wait.html',{
        "message": message
    })   


