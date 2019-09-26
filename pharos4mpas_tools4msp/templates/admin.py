from django.contrib import admin
from django import forms
from ckeditor.widgets import CKEditorWidget

# Register your models here.
from .models import UserType, Activity, Question, Answer, Recommendation, Collection

class ActivityAdmin(admin.ModelAdmin):
    pass


class AnswerAdmin(admin.ModelAdmin):
    fields = ['question', 'answer_text']
    list_display = ('question','desc',)


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
    

#class RecommendationAdminForm(forms.ModelForm):
#    recommendation_text = forms.CharField(widget=CKEditorWidget())
#    fields = ['activity', 'recommendation_text', 'condition']
#    class Meta:
#        model = Recommendation

class RecommendationAdmin(admin.ModelAdmin):
#form = RecommendationAdminForm
    fields = ['activity','title', 'recommendation_text', 'condition']
    inlines = [CollectionInline]
    list_filter = ['activity']
    list_display = ('pk','activity', 'title',)
    filter_horizontal = ('answer',)

admin.site.register(UserType)
admin.site.register(Activity)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Answer, AnswerAdmin)
admin.site.register(Recommendation,RecommendationAdmin)
