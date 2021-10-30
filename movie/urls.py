from django.urls import path, include
import debug_toolbar
from django.conf import settings

from . import views

urlpatterns = [
    path("", views.index, name='index'),
    path("categories", views.category, name='category'),
    path("<int:movie_id>", views.moviePage, name='moviePage'),
    path('workon', views.workon, name='workon'),
    path('__debug__/', include(debug_toolbar.urls))
]