from django.db import models

# Create your models here.
from django.db import models

class UserType(models.Model):
    user_type = models.CharField(max_length=80)
    def __unicode__(self):
        return self.user_type

class Activity(models.Model):
    description = models.CharField(max_length=200)
    def __unicode__(self):
        return self.description


class Question(models.Model):
    activity = models.ManyToManyField(Activity) 
    question_text = models.TextField(max_length=500)
    question_level = models.PositiveSmallIntegerField(default=1)
    multichoice = models.BooleanField("multi", default=0)

    def __unicode__(self):
        return self.question_text
    def activity_list(self):
        return ','.join(self.activity)

class Answer(models.Model):
    question = models.ForeignKey(Question)
    answer_text = models.CharField(max_length=200)
    def __unicode__(self):
        return self.answer_text
    def desc(self):
        return str(self.question) + ': -' + self.answer_text
    def activity_list(self):
        return ','.join(self.question.activity_set)

class Recommendation(models.Model):
    activity = models.ForeignKey(Activity, blank=True, null=True, on_delete=models.SET_NULL)
    answer = models.ManyToManyField(Answer, through='Collection')
    recommendation_text = models.TextField()
    def __unicode__(self):
        return self.recommendation_text
    def desc(self):
        return 'R' + str(self.id) + ' ' + self.recommendation_text



class Collection(models.Model):
	recommendation = models.ForeignKey(Recommendation, on_delete=models.CASCADE)
	answer = models.ForeignKey(Answer, on_delete=models.CASCADE)
	condition = models.CharField(max_length=3, choices=(('AND', 'AND'),('OR', 'OR'),('NOT', 'NOT'),), default='OR')

