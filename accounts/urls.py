from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('add/', views.add),
    path('search/', views.search),
    path('all/', views.all),
    path('delete/<int:pk>', views.delete , name='delete'),
    path('edit/<int:pk>', views.edit, name='edit' ),
    
    #login and register
    path('register/', views.register),
    path('login/', views.login),

]