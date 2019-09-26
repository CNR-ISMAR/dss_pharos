from django.db import models
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
# Create your models here.
from django.db import models

class UserType(models.Model):
    user_type = models.CharField(max_length=80)
    def __unicode__(self):
        return self.user_type

class Activity(models.Model):
    description = models.CharField(max_length=200)
    bg_information = RichTextUploadingField()
    bg_image=models.ImageField(upload_to='images',blank=True,null=True)
    def __unicode__(self):
        return self.description


class Question(models.Model):
    activity = models.ManyToManyField(Activity) 
    question_text = models.TextField(max_length=500)
    question_level = models.PositiveSmallIntegerField(default=1)
    multichoice = models.BooleanField("multi", default=0)
    #set ordering parameters for the class
    class Meta:
        ordering = ["question_level"]
    def __unicode__(self):
        return self.question_text
    def activity_list(self):
        return ','.join(self.activity)


class Answer(models.Model):
#    order = models.AutoField()
    question = models.ForeignKey(Question, null=True, on_delete=models.SET_NULL)
    answer_text = models.CharField(max_length=200)
    class Meta:
        ordering = ["pk"]
    def __unicode__(self):
        return str(self.question) + ' -' + self.answer_text
    def desc(self):
        return self.answer_text
    def activity_list(self):
        return ','.join(self.question.activity_set)

class Recommendation(models.Model):
    activity = models.ForeignKey(Activity, blank=True, null=True, on_delete=models.SET_NULL)
    answer = models.ManyToManyField(Answer, through='Collection')
    title = models.CharField(max_length=100)
    recommendation_text = RichTextUploadingField()
    condition = models.CharField(max_length=3, choices=(('AND', 'AND'),('OR', 'OR'),('NOT', 'NOT'),), default='OR')
 
    def __unicode__(self):
        return self.title
    def desc(self):
        return 'R' + str(self.id) + ' ' + self.recommendation_text



class Collection(models.Model):
        recommendation = models.ForeignKey(Recommendation, on_delete=models.CASCADE)
        answer = models.ForeignKey(Answer, on_delete=models.CASCADE)



