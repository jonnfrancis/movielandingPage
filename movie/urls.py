from django.urls import path, include
import debug_toolbar
from django.conf import settings

from . import views
from .views import MovieJsonListView

urlpatterns = [
    path("", views.index, name='index'),
    path("movies-json/", MovieJsonListView.as_view(), name='movies_json'),
    path("categories", views.category, name='category'),
    path("actors", views.actor, name='actor'),
    path("directors", views.director, name='director'),
    path("<int:movie_id>", views.moviePage, name='moviePage'),
    path('types', views.type_view, name='type'),
    path('workon', views.workon, name='workon'),
]