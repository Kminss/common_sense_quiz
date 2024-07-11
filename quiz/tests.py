from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Quiz, Answer


# Create your tests here.
class QuizTestCase(APITestCase):

    def test_create_quiz(self):

        data = {
            "title": "What is the capital of France?",
            "category": "ETC",
            "answers": [
                {
                    "content": "Paris",
                    "is_correct": True
                },
                {
                    "content": "London",
                    "is_correct": False
                },
                {
                    "content": "Berlin",
                    "is_correct": False
                },
                {
                    "content": "Madrid",
                    "is_correct": False
                }
            ]
        }

        response = self.client.post('/api/v1/quiz/', data, format='json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Quiz.objects.count(), 1)
        self.assertEqual(Answer.objects.count(), 4)

        quiz = Quiz.objects.get()
        self.assertEqual(quiz.title, "What is the capital of France?")

        correct_answer = Answer.objects.get(quiz=quiz, is_correct=True)
        self.assertEqual(correct_answer.content, "Paris")

        incorrect_answers = Answer.objects.filter(quiz=quiz, is_correct=False)
        self.assertEqual(incorrect_answers.count(), 3)
        self.assertIn("London", [answer.content for answer in incorrect_answers])
        self.assertIn("Berlin", [answer.content for answer in incorrect_answers])
        self.assertIn("Madrid", [answer.content for answer in incorrect_answers])