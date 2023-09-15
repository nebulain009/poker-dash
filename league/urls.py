from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home, name='home'),
    path('hands/', views.Hands, name='hands'),
    path('', views.Home, name='stats'),
]