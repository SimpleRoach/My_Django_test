from django.contrib import admin

from .models import Question, Choice


class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        ("Вопрос", {'fields':['question_text']}),
        ("Настройка времени", {'fields':["pub_date"]})
    ]
    # fields = ["pub_date", "question_text"]

admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)
