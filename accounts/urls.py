from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('add/', views.add),
    path('search/', views.search),
    path('delete/', views.delete),
    path('edit/', views.edit),


]