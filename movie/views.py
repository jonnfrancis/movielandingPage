from django.shortcuts import render, redirect
import random
import secrets
from django.core.cache import cache
from django.views.decorators.cache import cache_page, cache_control
from django.http import JsonResponse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from .models import *

import json
   
CACHE_TTL = 60 * 15
# Create your views here.

def index(request):
    movies_list = Movie.objects.all()
    paginator = Paginator(movies_list, 10)  # Show 10 movies per page

    page_number = request.GET.get('page')
    if page_number:
        try:
            page_obj = paginator.page(page_number)
        except PageNotAnInteger:
            page_obj = paginator.page(1)
        except EmptyPage:
            page_obj = paginator.page(paginator.num_pages)
        
        movies = []
        for movie in page_obj:
            background = movie.get_background.first()
            background_url = background.image.url if background and hasattr(background, 'image') else ''
            movies.append({
                'id': movie.id,
                'title': movie.title,
                'year': movie.year,
                'tagline': movie.tagline,
                'type': movie.type.name if movie.type else '',
                'background': background_url,
            })

        return JsonResponse({'movies': movies})

    page_obj = paginator.page(1)
    context = {
        'types': Type.objects.all(),
        'movies': page_obj,
        'page_obj': page_obj,
    }
    response = render(request, 'movie/index.html', context)
    response['Cache-Control'] = 'public, max-age=900'
    return response


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


