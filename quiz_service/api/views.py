import logging

import requests

from django.db import transaction

from rest_framework.response import Response
from rest_framework.views import APIView, status

from .models import QuizQuestion
from .serializers import QuizQuestionsSerializer


class QuestionViewSet(APIView):
    """
    Веб-представление для создания вопросов в викторине.

    Этот представление обрабатывает POST-запрос с количеством вопросов
    (questions_num) для создания вопросов в базе данных.

    Args:
    - questions_num (int): Количество вопросов, которое нужно создать.

    HTTP-ответы:
    - 200: Успешно создано указанное количество вопросов.
    - 400: Недопустимый ввод (например, questions_num не является
           положительным целым числом).
    - 500: Внутренняя ошибка сервера при выполнении запроса.

    Для создания вопросов используется сторонний API (jservice.io),
    и ошибки при запросах к нему могут вызвать HTTP 500 ошибку.
    """

    def post(self, request):
        questions_num = request.data.get("questions_num")

        if not isinstance(questions_num, int) or questions_num <= 0:
            return Response(
                {"message": "Invalid input."},
                status=status.HTTP_400_BAD_REQUEST,
            )

        unique_questions = []

        try:
            with transaction.atomic():
                while len(unique_questions) < questions_num:
                    response = requests.get(
                        "https://jservice.io/api/random?count=1"
                    ).json()[0]

                    existing_question = QuizQuestion.objects.filter(
                        question_id=response["id"]
                    ).first()

                    if not existing_question:
                        new_question = QuizQuestion(
                            question_id=response["id"],
                            question_text=response["question"],
                            answer_text=response["answer"],
                        )
                        new_question.save()
                        unique_questions.append(new_question)

        except Exception as e:
            logging.error(f"error: {str(e)}")
            return Response(
                {"error": repr(e)},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )

        serializer = QuizQuestionsSerializer(unique_questions, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
