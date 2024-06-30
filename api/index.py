import json
from django.core.cache import cache
from django.http import JsonResponse
from movie.models import Movie, Type
import random
import secrets

CACHE_TTL = 60 * 15  # 15 minutes

def index(request):
    cached_data = cache.get('index_view_data')
    if cached_data:
        response = JsonResponse(cached_data)
        response['Cache-Control'] = 'public, max-age=3600'
        return response
    
    movies = list(Movie.objects.prefetch_related('get_pictures', 'get_background').all())
    cool_movies = list(Movie.objects.filter(cool=True))
    random.shuffle(cool_movies)

    random_movie = secrets.choice(movies)    
    random_movie2 = secrets.choice(movies)
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

    cache.set('index_view_data', response_data, timeout=CACHE_TTL)
    
    response = JsonResponse(response_data)
    response['Cache-Control'] = 'public, max-age=3600'
    return response

# Vercel's serverless function handler
def handler(request):
    request_body = json.loads(request.body.decode('utf-8'))
    return index(request_body)
