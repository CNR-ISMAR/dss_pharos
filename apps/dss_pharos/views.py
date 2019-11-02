from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.template import loader
from .models import UserType, EconomicSector, Recommendation,  Impact, Description

# Create your views here.

#@login_required
def home(request):
    home_description = Description.objects.filter(textView__exact='home').first()
    template = loader.get_template('dss_index.html')
    context = {
        'home_description': home_description,
    }
    return HttpResponse(template.render(context, request))

#@login_required
def sector_sel(request):
    economic_sector_list = EconomicSector.objects.order_by('id')
    sector_sel_description = Description.objects.filter(textView__exact='sector_sel').first()
    template = loader.get_template('sector_sel.html')
    context = {
        'economic_sector_list': economic_sector_list,
        'sector_sel_description': sector_sel_description,
    }
    return HttpResponse(template.render(context, request))

#@login_required
def economic_sector_bg_info(request,  economic_sector_id):
    economic_sector = get_object_or_404(EconomicSector, pk=economic_sector_id)
    template = loader.get_template('bg_information.html')
    context = {
        'economic_sector': economic_sector,
        'economic_sector_description': economic_sector.description,
        'economic_sector_id': economic_sector.pk,
    }
    return HttpResponse(template.render(context, request))
    
#@login_required
def economic_sector_interactions(request,  economic_sector_id):
    economic_sector = get_object_or_404(EconomicSector, pk=economic_sector_id)
    template = loader.get_template('interactions.html')
    context = {
        'economic_sector': economic_sector,
        #'economic_sector_description': economic_sector.description,
        #'economic_sector_id': economic_sector.pk,
    }
    return HttpResponse(template.render(context, request))


#@login_required
def economic_sector_form(request, economic_sector_id):
    usertype_list = UserType.objects.filter(economic_sector__id__exact=economic_sector_id).order_by('id')
    impact_list = Impact.objects.filter(economic_sector__id__exact=economic_sector_id).order_by('id')
    economic_sector = get_object_or_404(EconomicSector, pk=economic_sector_id)
    template = loader.get_template('form.html')
    context = {
        'economic_sector': economic_sector,
        'usertype_list': usertype_list,
        'impact_list':impact_list,
        #'economic_sector_description': economic_sector.description,
        #'economic_sector_id': economic_sector.pk,
    }
    return HttpResponse(template.render(context, request))




#@login_required
def economic_sector_result(request, usertype_id, economic_sector_id):
    impact_list = ()
    for key, value in request.POST.items():
        if key[0:6]=='impact':
            impact_list= impact_list + (value,)
    recommendation_list = Recommendation.objects.filter(impact__id__in=impact_list, user_type__id=usertype_id).distinct() |  Recommendation.objects.filter(impact__id__in=impact_list, all_users=True).distinct()
    economic_sector = get_object_or_404(EconomicSector, pk=economic_sector_id)
    usertype = UserType.objects.get(pk=usertype_id)
    template = loader.get_template('result.html')
    context = {
        'usertype': usertype,
        'economic_sector': economic_sector,
        'recommendation_list': recommendation_list,
    }
    return HttpResponse(template.render(context, request))

def help(request):
    template = loader.get_template('help.html')
    context = {
        #'help': True,
    }
    return HttpResponse(template.render())
