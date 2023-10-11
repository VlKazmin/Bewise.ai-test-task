from rest_framework.serializers import ModelSerializer

from .models import QuizQuestion


class QuizQuestionsSerializer(ModelSerializer):
    """Сериализатор для модели QuizQuestion."""

    class Meta:
        model = QuizQuestion
        fields = (
            "question_id",
            "question_text",
            "answer_text",
            "created_at",
        )
