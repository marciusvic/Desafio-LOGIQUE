from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('logout/', views.logout_view, name='logout'),
    path('ponto/', views.ponto, name='ponto'),
]