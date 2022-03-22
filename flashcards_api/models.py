from django.db import models

# Create your models here.
class Flashcard(models.Model):
    subject = models.CharField(max_length=255)
    question = models.CharField(max_length=255)
    answer = models.CharField(max_length=255)
