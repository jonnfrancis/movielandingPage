from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(Category)
admin.site.register(Photo)
admin.site.register(backgroundPhoto)
admin.site.register(Actor)
admin.site.register(Director)
admin.site.register(Movie)
admin.site.register(Comment)
admin.site.register(Type)