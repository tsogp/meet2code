from django.urls import path
from django.conf.urls import url
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('register/', views.register_request, name='register'),
    path('logout/', views.logout_request, name='logout'),
    path('login', views.login_request, name='login'),
    path('password_reset/', 
        auth_views.PasswordResetView.as_view(template_name="password_reset/password_reset.html"), 
        name='reset_password'
    ),

    path('password_reset_sent/', 
        auth_views.PasswordResetDoneView.as_view(template_name="password_reset/password_reset_sent.html"), 
        name='password_reset_done'
    ),

    path('password_reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path(
        'password_reset_complete/', 
        auth_views.PasswordResetCompleteView.as_view(template_name="password_reset/password_reset_done.html"), 
        name='password_reset_complete'
    ),
    path('activate_user/<uidb64>/<token>', views.activate_user, name='activate'),
]
