from rest_framework import viewsets

from quiz.serializer import QuizSerializer
from .models import Quiz


# Create your views here.
class QuizViewSet(viewsets.ModelViewSet):
    queryset = Quiz.objects.all()
    serializer_class = QuizSerializer
