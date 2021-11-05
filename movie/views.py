from django.shortcuts import render
import random
import secrets
from django.urls import reverse

from .models import *

import json
   

# Create your views here.

def index(request):
    movies = Movie.objects.all()
    for movie in movies:
        movie.Picture= movie.get_pictures.filter(id=movie.id)
    random_movie=secrets.choice(movies)    
    random_movie2=random.choice(movies)
    number=random.randint(1,10)
        
    return render(request, 'movie/index.html',{
        "types": Type.objects.all(),
        "movies" : movies,
        'coolmovies': Movie.objects.filter(cool=True),
        'kindaCool': Movie.objects.filter(kindaCool=True),
        "random": random_movie,
        "random2": random_movie2,
        "number": number
    })

def category(request):
    category_id = request.GET.get('categories',None)
    if category_id is None:
        movies = Movie.objects.filter(kindaCool = True)
    else:
        movies = Movie.objects.filter(category=category_id)
    categories = Category.objects.all()    
    return render(request, 'movie/categories.html',{
        "categories": categories,
        "category_id": category_id,
        "movies": movies
    }) 

def actor(request):
    category_id = request.GET.get('actors',None)
    if category_id is None:
        movies = Movie.objects.filter(kindaCool = True)
    else:
        movies = Movie.objects.filter(category=category_id)
    categories = Actor.objects.all()    
    return render(request, 'movie/categories.html',{
        "categories": categories,
        "category_id": category_id,
        "movies": movies
    })

def director(request):
    category_id = request.GET.get('directors',None)
    if category_id is None:
        movies = Movie.objects.filter(kindaCool = True)
    else:
        movies = Movie.objects.filter(category=category_id)
    categories = Director.objects.all()    
    return render(request, 'movie/directors.html',{
        "categories": categories,
        "category_id": category_id,
        "movies": movies
    })    

def moviePage(request, movie_id):
    movie = Movie.objects.get(id=movie_id)
    return render(request, 'movie/page.html',{
       "movie": movie, 
       "backgroundMovie": movie.get_background.all(),
       "pictureMovie": movie.get_pictures.all()
    })

def workon(request): 
    message = "This is still under construction"
    return render(request, 'movie/wait.html',{
        "message": message
    })   


