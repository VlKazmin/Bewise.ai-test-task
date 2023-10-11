from django.db import models


class QuizQuestion(models.Model):
    """Модель для хранения информации о вопросе для викторины.
    Args:
        question_id: Уникальный идентификатор вопроса.
        question_text : Текст вопроса для викторины.
        answer_text: Текст ответа на вопрос.
        created_at: Дата и время создания записи в базе данных
    """

    question_id = models.PositiveIntegerField(unique=True)
    question_text = models.TextField()
    answer_text = models.TextField()
    created_at = models.TimeField(auto_now_add=True)
