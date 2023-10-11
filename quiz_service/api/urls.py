from django.urls import path

from .views import QuestionViewSet

app_name = "api"

urlpatterns = [
    path(
        "get_quiz_question/",
        QuestionViewSet.as_view(),
        name="get_quiz_question",
    ),
]
