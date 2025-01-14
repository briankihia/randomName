from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('random/', views.random_name, name='random_name'),
]
