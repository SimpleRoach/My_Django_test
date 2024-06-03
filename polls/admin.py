from django.contrib import admin

from .models import Question, Choice


class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3
class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        ("Вопрос", {'fields':['question_text']}),
        ("Настройка времени", {'fields':["pub_date"]})
    ]
    inlines = [ChoiceInline]

admin.site.register(Question, QuestionAdmin)

