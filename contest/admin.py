from django.contrib import admin
from .models import Choice, Question, Contest, Result

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3


class QuestionAdmin(admin.ModelAdmin):
    list_display = ['text', 'date']
    fieldsets = [
        (None,               {'fields': ['text']}),
        ('Contest', {'fields': ['contest']}),
        ('Users', {'fields':['author']}),
    ]
    inlines = [ChoiceInline]


admin.site.register(Question, QuestionAdmin)


class ResultInline(admin.StackedInline):
    model = Result

class ContestAdmin(admin.ModelAdmin):
    inlines = [ResultInline]

admin.site.register(Contest)
admin.site.register(Result)
