from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.http import Http404
from django.shortcuts import get_object_or_404
from django.urls import reverse
from django.views import generic
from django.utils import timezone

from .models import Profile, Detail

# Create your views here.
def index(request):
    latest_cat_list = Profile.objects.order_by('-pub_date')[:5]
    template = loader.get_template('catProfile/index.html')
    context = {
        'latest_cat_list': latest_cat_list,
    }  
    return HttpResponse(template.render(context, request))

def detail(request, cat_name):
    # try-except구문 or name=get_... 중 하나만 사용하면 됨
    
    # name = get_object_or_404(Profile, pk=cat_name)
    
    try:
        name = Profile.objects.get(pk=cat_name)
    except Profile.DoesNotExist:
        raise Http404("cat does not exist")

    return render(request, 'catProfile/detail.html', {'name':name})