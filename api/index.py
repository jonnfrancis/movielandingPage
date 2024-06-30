import os
import json
import random
import secrets
import django
from django.http import JsonResponse
from django.conf import settings

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "landingpage.settings")
django.setup()

from movie.models import Movie, Type

def index(request):
    movies = list(Movie.objects.all())
    for movie in movies:
        movie.Picture = movie.get_pictures.filter(id=movie.id)

    cool_movies = list(Movie.objects.filter(cool=True))
    random.shuffle(cool_movies)

    random_movie = secrets.choice(movies)
    random_movie2 = secrets.choice(movies)
    number = random.randint(1, 10)

    response_data = {
        "types": list(Type.objects.all().values()),
        "movies": list(movies),
        'coolmovies': cool_movies,
        'kindaCool': list(Movie.objects.filter(kindaCool=True).values()),
        "random": random_movie.id,
        "random2": random_movie2.id,
        "number": number
    }

    return JsonResponse(response_data)

# Vercel's serverless function handler
def handler(event, context):
    request = json.loads(event["body"])
    return index(request)
