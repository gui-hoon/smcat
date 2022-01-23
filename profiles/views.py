from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.urls import reverse
from django.views import generic
from django.utils import timezone

from .models import Cat


class IndexView(generic.ListView):
    template_name = 'profiles/index.html'
    context_object_name = 'cat_list'

    def get_queryset(self):
        return Cat.objects.filter(
            date__lte=timezone.now()
        ).order_by('-name')

# def cat_index(request):
#     cat_list = Cat.objects.order_by('-name')
#     context = {'cat_list': cat_list}
    
#     return render(request, 'profiles/index.html', context)

def cat_detail(request, pid):
    cat = get_object_or_404(Cat, pk=pid)

    # try:
    #     cat = Cat.objects.get(pk=pid)
    # except Cat.DoesNotExist:
    #     raise Http404("cat does not exist")    
    context = {'cat':cat}

    return render(request, 'profiles/detail.html', context)

