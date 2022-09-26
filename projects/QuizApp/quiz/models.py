from turtle import title
from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=50, verbose_name='Category name')

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = 'Categories'


class Quiz(models.Model):
    title = models.CharField(max_length=50, verbose_name='Quiz Title')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name_plural = 'Quizzes'


class Question(models.Model):
    SCALE =(
        ('B', 'Beginner'),
        ('I', 'Intermediate'),
        ('A', 'Advanced')
    )
    title= models.TextField()
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    difficulty = models.CharField(max_length=1, choices=SCALE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
