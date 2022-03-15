from django.urls import path
from . import views

urlpatterns = [
    path('api/flashcards', views.FlashcardList.as_view() name="flashcard_list"),
    path('api/flashcards/<int:pk>', views.FlashcardDetail.as_view(), name="flashcard_detail")
]

