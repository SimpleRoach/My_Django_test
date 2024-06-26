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
    list_display = ["question_text", "pub_date"]
    list_display = ["question_text", "pub_date", "was_published_recently"]
    list_filter = ["pub_date"]
    search_fields = ["question_text"]

admin.site.register(Question, QuestionAdmin)

