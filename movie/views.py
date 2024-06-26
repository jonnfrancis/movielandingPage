from django.shortcuts import render, redirect
import random
import secrets
from django.core.cache import cache
from django.views.decorators.cache import cache_page, cache_control
from django.http import JsonResponse

from .models import *

import json
   
CACHE_TTL = 60 * 15
# Create your views here.

def index(request):
    if request.path.startswith('/api/'):
        return handle_index_api(request)
        
    movies = Movie.objects.all()
    
    for movie in movies:
        movie.Picture= movie.get_pictures.filter(id=movie.id)

    cool_movies = list(Movie.objects.filter(cool=True))
    random.shuffle(cool_movies)

    random_movie=secrets.choice(movies)    
    random_movie2=random.choice(movies)
    number=random.randint(1,10)
        
    context = {
        "types": Type.objects.all(),
        "movies": movies,
        'coolmovies': cool_movies,
        'kindaCool': Movie.objects.filter(kindaCool=True),
        "random": random_movie,
        "random2": random_movie2,
        "number": number
    }
    
    response = render(request, 'movie/index.html', context)
    response['Cache-Control'] = 'public, max-age=900'
    return response

def handle_index_api(request):
    movies = list(Movie.objects.all())
    for movie in movies:
        movie.Picture = movie.get_pictures.filter(id=movie.id)

    cool_movies = list(Movie.objects.filter(cool=True))
    random.shuffle(cool_movies)

    random_movie = secrets.choice(movies)
    random_movie2 = random.choice(movies)
    number = random.randint(1, 10)

    response_data = {
        "types": list(Type.objects.all().values()),
        "movies": [movie.id for movie in movies],
        'coolmovies': [movie.id for movie in cool_movies],
        'kindaCool': list(Movie.objects.filter(kindaCool=True).values()),
        "random": random_movie.id,
        "random2": random_movie2.id,
        "number": number
    }

    return JsonResponse(response_data)

@cache_page(CACHE_TTL)
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

@cache_page(CACHE_TTL)
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

@cache_page(CACHE_TTL)
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


