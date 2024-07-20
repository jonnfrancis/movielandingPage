from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone
from decimal import Decimal
# Create your models here.


class Category(models.Model):
    category = models.CharField(max_length=30)



    def __str__(self):
        return f"{self.category}"


class Actor(models.Model):
    name = models.CharField(max_length=60)



    def __str__(self):
        return f"{self.name}"

class Director(models.Model):
    name = models.CharField(max_length=60)


    def __str__(self):
        return f"{self.name}"

class Type(models.Model):
    type = models.CharField(max_length=15)


    def __str__(self):
        return f"{self.type}"

    def get_absolute_url(self):
        return f'/types?type_id={self.type}'


class Movie(models.Model):
    title = models.CharField(max_length=45)
    releaseDate = models.DateField(default=0)
    cool = models.BooleanField(default=False)
    kindaCool = models.BooleanField(default=False)
    clasId = models.CharField(max_length=2)
    trailer = models.CharField(max_length=50)
    storyline = models.CharField(max_length=600)
    runtime = models.IntegerField(default=0)
    year = models.IntegerField(default=0)
    actors = models.ManyToManyField(Actor, blank=True, related_name='get_actors')
    directors = models.ManyToManyField(Director, blank=True, related_name='get_directors')
    categories = models.ManyToManyField(Category, blank=True, related_name='list_categories')
    type = models.ForeignKey(Type, on_delete=models.CASCADE, related_name='get_type') 
    tagline = models.CharField(max_length=150)
    imdb_rating = models.DecimalField(max_digits=3, decimal_places=1, default=Decimal('0.0'))

    def __str__(self):
        return f"{self.title} - {self.releaseDate}"

    class Meta:
        indexes = [
            models.Index(fields=['imdb_rating']),
            models.Index(fields=['releaseDate']),
        ]

    def get_absolute_url(self):
        return f'/{self.id}'


class Photo(models.Model):
    image = models.CharField(max_length=350)
    altText = models.CharField(max_length=30)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, blank=True, related_name='get_pictures')


    def __str__(self):
        return f"{self.image}"


class backgroundPhoto(models.Model):
    image = models.CharField(max_length=350)
    altText = models.CharField(max_length=30)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, blank=True, related_name='get_background')


    def __str__(self):
        return f"{self.image}"

          
class Comment(models.Model):
    comment = models.CharField(max_length=100)
    createdDate = models.DateTimeField(default=timezone.now)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name="get_comments")

    def get_creation_date(self):
        return self.createdDate.strftime('%B %d %Y')
 