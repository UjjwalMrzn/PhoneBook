from django.urls import path
from . import views

urlpatterns = [
    path('', views.front),
    path('home/', views.home , name='home'),
    path('add/', views.add),
    path('search/', views.search),
    path('all/', views.all),
    path('delete/<int:pk>', views.delete , name='delete'),
    path('edit/<int:pk>', views.edit, name='edit' ),
    path('user', views.user, name='user' ),

    
    #login and register
    path('register/', views.register , name='register'),
    path('login/', views.loginpage , name='login'),
    path('logout/', views.logoutuser, name='logout'),

]