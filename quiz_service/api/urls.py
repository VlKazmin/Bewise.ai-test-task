from django.urls import path

from .views import QuestionViewSet

app_name = "api"

urlpatterns = [
    path(
        "quiz_service/",
        QuestionViewSet.as_view(),
        name="quiz_service",
    ),
]
