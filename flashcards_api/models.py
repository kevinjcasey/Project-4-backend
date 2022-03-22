from django.db import models

# Create your models here.
class Flashcard(models.Model):
    subject = models.TextField(max_length=1000)
    question = models.TextField(max_length=1000)
    answer = models.TextField(max_length=1000)
