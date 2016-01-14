# coding: utf-8
from django.db import models

# Create your models here.
class Category(models.Model):
    title = models.CharField(max_length=200)
    alias = models.CharField(max_length=80)

    def __str__(self):
        return self.title

    def get_categories(self):
            return Category.objects.all()

class Joke(models.Model):
    category = models.ForeignKey(Category)
    text = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text

    def get_grade(self):
        grades = self.grade_set.all()
        if len(grades) > 0:
            summa = 0
            for item in grades:
                summa += item.grades
            return summa / len(grades)
        else: return 0


class Grade(models.Model):
    POSSIBLE_GRADES = [
        (1, 1),
        (2, 2),
        (3, 3),
        (4, 4),
        (5, 5),
    ]

    joke = models.ForeignKey(Joke)
    grades = models.IntegerField(choices=POSSIBLE_GRADES)

    def __str__(self):
        return self.grades

