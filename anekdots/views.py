# coding: utf-8
import os
import threading
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
import pickle
from funsite.settings import BASE_DIR
from .models import Joke, Category, Grade
from django.core.paginator import Paginator
# Create your views here.


class JokeListView(ListView):
    model = Joke

    queryset = Joke.objects.order_by('-pub_date')[:10]


    def get_context_data(self, **kwargs):
        context = super(JokeListView, self, **kwargs).get_context_data(**kwargs)
        context['category_list'] = Category.objects.all()
        return context

class CategoryView(DetailView):
    model = Category


def vote(request, joke_id, grade):
    grade = Grade(joke = get_object_or_404(Joke, pk=joke_id), grades = grade)
    grade.save()
    url = '/category/' + str(get_object_or_404(Joke, pk=joke_id).category.id) + '#'+joke_id
    return HttpResponseRedirect(url)

#@login_required(login_url='/login/')
def load_jokes(self):
    TIME_JOKE = 60.0 * 10
    FILE = 'anekdots/static/anekdots/jokes.jks'

    def load_joke():
        with open(os.path.join(BASE_DIR, FILE), 'rb') as file:
            jokes = pickle.load(file)
            print('Загружен файл с шутками')
            file.close()
        joke = jokes.pop()
        try:
            cat = Category.objects.get(title=joke['category'])
        except Category.DoesNotExist:
            cat = Category(title=joke['category'], alias='none')
            cat.save()
        newjoke = Joke(category = cat, text = joke['joke'])
        newjoke.save()
        print('Шутка добавлена')
        with open(os.path.join(BASE_DIR, FILE), 'wb') as file:
            pickle.dump(jokes, file)
            print('Сохранение завершено')
            file.close()

        # timer = threading.Timer(TIME_JOKE, load_joke)
        # timer.start()
        # print('Таймер на следующую шутку запущен')

    timer = threading.Timer(TIME_JOKE, load_joke)
    timer.start()
    return HttpResponse('Таймер запущен...')
