from django.contrib import admin

# Register your models here.

from django import forms
from ckeditor.widgets import CKEditorWidget

# Register your models here.
from .models import UserType, EconomicSector, Impact,  Recommendation, Collection

class EconomicSectorAdmin(admin.ModelAdmin):
    fields = ['title', 'description', 'bg_information', 'bg_image','interactions', 'interactions_image']
    list_display = ('id', 'title','description')
    list_display_links = ('id', 'title')
    ordering = ['id']




# class UserTypeInline(admin.TabularInline):
#     model = UserType
#     extra = 10



class ImpactAdmin(admin.ModelAdmin):
    fields = ['economic_sector',  'impact_name', 'impact_description', ]
    # inlines = [UserTypeInline]
    ordering = ["id"]
    list_display= ('id',  'impact_name')
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
    ordering = ['id']
    fields = ['economic_sector',  'title', 'user_type', 'all_users', 'recommendation_text', ]
    inlines = [CollectionInline]
    list_filter = ['economic_sector', 'user_type']
    list_display = ('pk','economic_sector', 'title',)
    filter_horizontal = ('impact',)

class DescriptionAdmin(admin.ModelAdmin):
    fields = ['textView', 'textContent']



admin.site.register(UserType)
admin.site.register(EconomicSector, EconomicSectorAdmin)
admin.site.register(Impact, ImpactAdmin)
admin.site.register(Recommendation,RecommendationAdmin)

