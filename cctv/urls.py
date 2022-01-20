from django.urls import path

from . import views

# app_name = cctv
urlpatterns = [
    path('', views.mycctv, name='mycctv'),
    path('mycam/', views.mycam, name='mycam')
]