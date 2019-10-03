from django.contrib import admin

# Register your models here.

from django import forms
from ckeditor.widgets import CKEditorWidget

# Register your models here.
from .models import UserType, EconomicSector, Impact,  Recommendation, Collection

class EconomicSectorAdmin(admin.ModelAdmin):
    fields = ['title', 'description']
    list_display = ['title','description',]

    pass


# class UserTypeInline(admin.TabularInline):
#     model = UserType
#     extra = 10



class ImpactAdmin(admin.ModelAdmin):
    fields = ['economic_sector', 'question_level','impact_name', 'multichoice']
    # inlines = [UserTypeInline]
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
    filter_horizontal = ('impact',)

admin.site.register(UserType)
admin.site.register(EconomicSector)
admin.site.register(Impact, ImpactAdmin)
admin.site.register(Recommendation,RecommendationAdmin)

