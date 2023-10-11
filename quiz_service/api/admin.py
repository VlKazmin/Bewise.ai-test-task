from django.contrib import admin

from .models import QuizQuestion


@admin.register(QuizQuestion)
class QuizQuestionAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "question_id",
        "question_text",
        "answer_text",
        "created_at",
    )
    search_fields = ("id",)
    ordering = ("-created_at",)
