from django.contrib.sitemaps import Sitemap
from django.urls import reverse
from .models import Type, Movie

class StaticSitemap(Sitemap):
    def items(self):
        return ['index', 'type', 'category', 'director']

    def location (self, item):
        return reverse(item)


class CategorySitemap(Sitemap):
    def items(self):
        return Type.objects.all()

class MoviepageSitemap(Sitemap):
    def items(self):
        return Movie.objects.all()[:40]