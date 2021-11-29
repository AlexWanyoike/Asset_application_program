from django.conf.urls import url
from . import views
from django.urls import path, re_path

urlpatterns = [
    path('', views.welcome, name='welcome'),
    path('login/', views.login, name='login'),
    path('request/', views.request, name='request'),
    path('manager/', views.approval, name='manager'),
    path('teamleader/', views.allocate, name='teamleader'),
]
