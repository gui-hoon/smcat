from django.urls import path
from . import views

app_name ='profiles'
urlpatterns = [
    # /profiles
    path('', views.IndexView.as_view(), name='cat-index'),
    # ex: /profiles/4/
    path('<int:pid>/', views.cat_detail, name='cat-detail')
]