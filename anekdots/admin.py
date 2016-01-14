# coding: utf-8
from django.contrib import admin
from .models import Joke, Category, Grade
# Register your models here.
class JokeAdmin(admin.ModelAdmin):
    list_display = ('text', 'pub_date')

admin.site.register(Category)
admin.site.register(Joke, JokeAdmin)
admin.site.register(Grade)