from rest_framework.serializers import ModelSerializer
from .models import QuizQuestion


class QuizQuestionsSerializer(ModelSerializer):
    """
    Сериализатор для модели QuizQuestion.

    Args:
    - question_id (int): Уникальный идентификатор вопроса.
    - question_text (str): Текст вопроса для викторины.
    - answer_text (str): Текст ответа на вопрос.
    - created_at (str): Дата и время создания записи в базе данных.
    """

    class Meta:
        model = QuizQuestion
        fields = (
            "question_id",
            "question_text",
            "answer_text",
            "created_at",
        )
