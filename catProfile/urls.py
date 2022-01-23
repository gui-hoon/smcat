from django.urls import path

from . import views

urlpatterns =[
    # ex: /profiles/
    path('', views.index, name='index'),
    # ex: /profiles/()
    path('<int:name>/detail/', views.detail, name='detail'),
    
]