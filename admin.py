from django.contrib import admin

# Register your models here.
from .models import UserType, Activity, Question, Answer, Recommendation, Collection

class AnswerAdmin(admin.ModelAdmin):
    fields = ['question', 'answer_text']
    list_display = ('desc',)


class AnswerInline(admin.TabularInline):
    model = Answer
    extra = 3

class QuestionAdmin(admin.ModelAdmin):
    fields = ['activity', 'question_level','question_text', 'multichoice']
    inlines = [AnswerInline]
    list_filter = ['activity']


class CollectionInline(admin.TabularInline):
    model = Collection
    extra = 10
    list_filter = ['activity']
    

class RecommendationAdmin(admin.ModelAdmin):
    fields = ['recommendation_text']
    inlines = [CollectionInline]
    list_filter = ['activity']
    list_display = ('desc',)
    filter_horizontal = ('answer',)

admin.site.register(UserType)
admin.site.register(Activity)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Answer, AnswerAdmin)
admin.site.register(Recommendation,RecommendationAdmin)
