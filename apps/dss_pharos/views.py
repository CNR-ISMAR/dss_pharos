from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.template import loader

# Create your views here.

@login_required
def level_1(request):
    usertype_list = UserType.objects.order_by('id')
    #output = '<br> '.join([p.user_type for p in usertype_list])
    template = loader.get_template('level_1.html')
    context = {
        'usertype_list': usertype_list,
    }
    return HttpResponse(template.render(context, request))

@login_required
def level_2(request, usertype_id):
    activity_list = Activity.objects.order_by('id')
    usertype = get_object_or_404(UserType, pk=usertype_id)
    template = loader.get_template('level_2.html')
    context = {
        'usertype': usertype,
        'activity_list': activity_list,
    }
    return HttpResponse(template.render(context, request))

@login_required
def activity_bg_info(request, usertype_id, activity_id):
    activity = get_object_or_404(Activity, pk=activity_id)
    usertype = UserType.objects.get(pk=usertype_id)
    template = loader.get_template('bg_information.html')
    context = {
        'usertype': usertype,
        'activity': activity,
        #'activity_description': activity.description,
        #'activity_id': activity.pk,
    }
    return HttpResponse(template.render(context, request))
    
@login_required
def activity_form(request, usertype_id, activity_id):
    activity = get_object_or_404(Activity, pk=activity_id)
    usertype = UserType.objects.get(pk=usertype_id)
    template = loader.get_template('form.html')
    context = {
        'usertype': usertype,
        'activity': activity,
        #'activity_description': activity.description,
        #'activity_id': activity.pk,
    }


@login_required
def activity_result(request, usertype_id, activity_id):
    answer_list = ()
    for key, value in request.POST.items():
        if key[0:9]=='question_':
            answer_list= answer_list + (value,)
    recommendation_list = Recommendation.objects.filter(answer__in=answer_list).distinct()
    activity = get_object_or_404(Activity, pk=activity_id)
    usertype = UserType.objects.get(pk=usertype_id)
    template = loader.get_template('result.html')
    context = {
        'usertype': usertype,
        'activity': activity,
        'recommendation_list': recommendation_list,
    }
    return HttpResponse(template.render(context, request))

def help(request):
    template = loader.get_template('help.html')
    context = {
        #'help': True,
    }
    return HttpResponse(template.render())
