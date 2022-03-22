from django.db import models

# Create your models here.
class Flashcard(models.Model):
    subject = models.TextField(max_length=255)
    question = models.TextField(max_length=255)
    answer = models.TextField(max_length=255)
