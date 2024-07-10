from .models import Quiz, Answer
from rest_framework import serializers


class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = ['id', 'content', 'is_correct']


class QuizSerializer(serializers.ModelSerializer):
    answers = AnswerSerializer(many=True)
    category_display_value = serializers.CharField(
        source='get_category_display', read_only=True
    )

    class Meta:
        model = Quiz
        fields = [
            "id",
            "category",
            "category_display_value",
            "title",
            "answers",
            "created_at",
            "modified_at",
        ]

    def create(self, validated_data):
        answers_data = validated_data.pop('answers')
        quiz = Quiz.objects.create(**validated_data)

        for answer_data in answers_data:
            Answer.objects.create(quiz=quiz, **answer_data)

        return quiz
