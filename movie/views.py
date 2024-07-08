from django.shortcuts import render, redirect
import random
import secrets
from django.core.cache import cache
from django.views.decorators.cache import cache_page, cache_control
from django.http import JsonResponse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic import View, TemplateView

from .models import *

import json
   
CACHE_TTL = 60 * 15
# Create your views here.

def index(request):
    page_number = request.GET.get('page', 1)
    movies_list = Movie.objects.all()
    
    # Paginate movies, showing 10 movies per page
    paginator = Paginator(movies_list, 6)
    
    try:
        movies = paginator.page(page_number)
    except PageNotAnInteger:
        movies = paginator.page(1)
    except EmptyPage:
        movies = paginator.page(paginator.num_pages)
    
    for movie in movies:
        movie.Picture = movie.get_pictures.filter(id=movie.id)

    cool_movies = list(Movie.objects.filter(cool=True))
    random.shuffle(cool_movies)

    random_movie = secrets.choice(movies_list)
    random_movie2 = random.choice(movies_list)
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

    response = render(request, 'movie/index.html', context)
    response['Cache-Control'] = 'public, max-age=900'
    return response

class MovieJsonListView(View):
    def get(self, *args, **kwargs):
        upper = int(self.request.GET.get('num_movies', 6))
        lower = upper - 6

        # Check if the data is in the cache
        cache_key = f'movies_{lower}_{upper}'
        movies = cache.get(cache_key)

        if not movies:
            # If not, fetch the data from the database
            movies_queryset = Movie.objects.prefetch_related('get_pictures', 'get_background')[lower:upper]
            movies = []
            for movie in movies_queryset:
                background = movie.get_background.first()
                background_url = background.image if background else ''  # Access the background image URL

                movies.append({
                    'id': movie.id,
                    'title': movie.title,
                    'year': movie.year,
                    'tagline': movie.tagline,
                    'type': movie.type.type,  # Access the type field from the Type model
                    'background': background_url
                })

            # Cache the data
            cache.set(cache_key, movies, timeout=3600)  # Cache timeout set to 1 hour

        movies_size = Movie.objects.count()
        size = upper >= movies_size
        return JsonResponse({'data': movies, 'max': size}, safe=False)

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


