from django.urls import path
from . import views

from django.contrib.auth import views as auth_views

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


    #reset
    path('reset_password/' , auth_views.PasswordResetView.as_view(template_name='accounts/password_reset.html'), name="reset_password"),
    path('reset_password_sent/' , auth_views.PasswordResetDoneView.as_view(template_name='accounts/password_reset_sent.html'), name="password_reset_done"),
    path('reset/<uidb64>/<token>/' , auth_views.PasswordResetConfirmView.as_view() , name="password_reset_confirm"),
    path('reset_password_complete/' , auth_views.PasswordResetCompleteView.as_view(template_name='accounts/password_reset_done.html'), name="password_reset_complete"),



    path('navbar/', views.navbar, name='navbar'),
]