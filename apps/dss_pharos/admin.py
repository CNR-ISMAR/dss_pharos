from django.contrib import admin

# Register your models here.

from django import forms
from ckeditor.widgets import CKEditorWidget

# Register your models here.
from .models import UserType, EconomicSector, Question, Answer, Recommendation, Collection

class EconomicSectorAdmin(admin.ModelAdmin):
    fields = ['title', 'description']
    list_display = ['title','description',]

    pass


class AnswerAdmin(admin.ModelAdmin):
    fields = ['question', 'answer_text']
    list_display = ('question','desc',)


class AnswerInline(admin.TabularInline):
    model = Answer
    extra = 3

class QuestionAdmin(admin.ModelAdmin):
    fields = ['economic_sector', 'question_level','question_text', 'multichoice']
    inlines = [AnswerInline]
    list_filter = ['economic_sector']


class CollectionInline(admin.TabularInline):
    model = Collection
    extra = 10
    list_filter = ['economic_sector']
    

#class RecommendationAdminForm(forms.ModelForm):
#    recommendation_text = forms.CharField(widget=CKEditorWidget())
#    fields = ['economic_sector', 'recommendation_text', 'condition']
#    class Meta:
#        model = Recommendation

class RecommendationAdmin(admin.ModelAdmin):
#form = RecommendationAdminForm
    fields = ['economic_sector','title', 'recommendation_text', 'condition']
    inlines = [CollectionInline]
    list_filter = ['economic_sector']
    list_display = ('pk','economic_sector', 'title',)
    filter_horizontal = ('answer',)

admin.site.register(UserType)
admin.site.register(EconomicSector)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Answer, AnswerAdmin)
admin.site.register(Recommendation,RecommendationAdmin)

