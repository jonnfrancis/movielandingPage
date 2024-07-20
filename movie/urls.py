from django.urls import path, include
import debug_toolbar
from django.conf import settings
from django.views.generic.base import TemplateView

from . import views
from .views import MovieJsonListView

#sitemaps
from django.contrib.sitemaps.views import sitemap
from movie.sitemaps import *

sitemaps = {
    'static' : StaticSitemap,
    'categories' : CategorySitemap,
    'moviepages' : MoviepageSitemap
}

urlpatterns = [
    path("", views.index, name='index'),
    path("movies-json/<int:num_movies>/", MovieJsonListView.as_view(), name='movies_json'),
    path("categories", views.category, name='category'),
    path("robots.txt/", TemplateView.as_view(template_name="robots.txt", content_type="text/plain") ), 
    path('sitemap.xml/', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
    path("actors", views.actor, name='actor'),
    path("directors", views.director, name='director'),
    path("<int:movie_id>", views.moviePage, name='moviePage'),
    path('types', views.type_view, name='type'),
    path('workon', views.workon, name='workon'),
]
