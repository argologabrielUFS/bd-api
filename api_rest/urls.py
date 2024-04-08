from django.contrib import admin
from django.urls import path, include

from . import views

urlpatterns = [
    path('end', views.get_end, name='get_all_users'),
    path('plat', views.get_plat, name='get_all_users'),
    path('loja', views.get_loja, name='get_all_users'),
    path('vend', views.get_vend, name='get_all_users'),
    path('data/', views.end_manager),
    path('data/1', views.loja_manager),
    path('data/2', views.plat_manager),
    path('data/3', views.vend_manager)
]
  #  path('user/<str:nick>', views.get_by_nick),
  #  path('', views.get_users, name='get_all_users'),
  #  path('1', views.get_users, name='get_all_users'),
  #  path('2', views.get_users, name='get_all_users'),
  #  path('3', views.get_users, name='get_all_users'),