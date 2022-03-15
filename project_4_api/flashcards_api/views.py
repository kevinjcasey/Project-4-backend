from django.shortcuts import render
from rest_framework import generics
from .serializers import FlashcardSerializer
# Create your views here.

class FlashcardList(generics.ListCreateAPIView):
    queryset = Flashcard.objects.all().order_by('id')
    serializer_class = FlashcardSerializer

class FlashcardDetail(generics.ListCreateAPIView):
    queryset = Flashcard.objects.all().order_by('id')
    serializer_class = FlashcardSerializer