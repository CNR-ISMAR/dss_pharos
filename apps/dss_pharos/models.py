from django.db import models
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
# Create your models here.
from django.db import models

class UserType(models.Model):
    user_type = models.CharField(max_length=80)
    def __str__(self):
        return self.user_type

class EconomicSector(models.Model):
    title = models.CharField(max_length=80, blank=True, null=True, )
    description = models.CharField(max_length=400)
    bg_information = RichTextUploadingField()
    bg_image=models.ImageField(upload_to='images',blank=True,null=True)
    interactions = RichTextUploadingField(blank=True, null=True)
    interactions_image=models.ImageField(upload_to='images',blank=True,null=True)

    def __str__(self):
        return self.description


class Impact(models.Model):
    economic_sector = models.ManyToManyField(EconomicSector) 
    user_type = models.ManyToManyField(UserType)
    impact_name = models.TextField(max_length=100)


    #set ordering parameters for the class
    class Meta:
        ordering = ['impact_name']
    def __str__(self):
        return self.impact_name
    def ecnonomic_sector_list(self):
        return ','.join(self.economic_sector)



class Recommendation(models.Model):
    economic_sector = models.ForeignKey(EconomicSector, blank=True, null=True, on_delete=models.SET_NULL)
    user_type = models.ForeignKey(UserType, blank=True, null=True, on_delete=models.SET_NULL)
    impact = models.ManyToManyField(Impact, through='Collection')
    title = models.CharField(max_length=100)
    recommendation_text = RichTextUploadingField()


    def __unicode__(self):
        return self.title
    def desc(self):
        return 'R' + str(self.id) + ' ' + self.recommendation_text



class Collection(models.Model):
        recommendation = models.ForeignKey(Recommendation, on_delete=models.CASCADE)
        impact = models.ForeignKey(Impact, on_delete=models.CASCADE)



