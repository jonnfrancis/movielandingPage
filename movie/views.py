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
    # Try to fetch from cache first
    cached_data = cache.get('index_view_data')
    if cached_data:
        return render(request, 'movie/index.html', cached_data)
        print('load by Cache')

    # If not in cache, generate the data
    movies = list(Movie.objects.prefetch_related('get_pictures', 'get_background').all())
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
    print('load by db')
    
    # Cache the generated data
    cache.set('index_view_data', context, CACHE_TTL)
    
    return render(request, 'movie/index.html', context)

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
            print('load by DB')

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


