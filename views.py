from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from django.template import loader
# Create your views here.

from .models import UserType, Activity, Question, Answer, Recommendation

def start(request):
    return HttpResponse("Hello, world. You're at the dss index.")

def level_1(request):
    usertype_list = UserType.objects.order_by('id')
    #output = '<br> '.join([p.user_type for p in usertype_list])
    template = loader.get_template('level_1.html')
    context = {
        'usertype_list': usertype_list,
    }
    return HttpResponse(template.render(context, request))

def level_2(request, usertype_id):
    activity_list = Activity.objects.order_by('id')
    usertype = get_object_or_404(UserType, pk=usertype_id)
    template = loader.get_template('level_2.html')
    context = {
        'usertype': usertype,
        'activity_list': activity_list,
    }
    return HttpResponse(template.render(context, request))



def activity_form(request, usertype_id, activity_id):
    activity = get_object_or_404(Activity, pk=activity_id)
    user = UserType.objects.get(pk=usertype_id)
    template = loader.get_template('form.html')
    context = {
        'user': user,
        'activity': activity,
        #'activity_description': activity.description,
        #'activity_id': activity.pk,
    }
    return HttpResponse(template.render(context, request))

def activity_result(request, usertype_id, activity_id):
    answer_list = set()
    for key, value in request.POST.items():
        if key[0:9]=='question_':
            answer_list.add(value)
    recommendation_list = Recommendation.objects.filter(answer__in=answer_list).distinct()
    activity = get_object_or_404(Activity, pk=activity_id)
    user = UserType.objects.get(pk=usertype_id)
    template = loader.get_template('result.html')
    context = {
        'user': user,
        'activity': activity,
        'recommendation_list': recommendation_list,
    }
    return HttpResponse(template.render(context, request))
