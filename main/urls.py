from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='homepage'),
    path('first/', views.first, name='first'),
]
