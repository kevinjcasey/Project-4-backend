from django.db import models

# Create your models here.
class Flashcard(models.Model):
    subject = models.CharField(max_length=32)
    question = models.CharField(max_length=32)
    answer = models.CharField(max_length=32)
