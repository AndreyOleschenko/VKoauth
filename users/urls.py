from django.urls import path
from django.contrib.auth.views import LogoutView
from . import views

urlpatterns = [
    path('', views.home_view, name='home'),
    path('login/', views.login_view, name='login'),
    path('signin/', views.signin_view, name='signin'),

    # logout по POST (и GET тоже работает в стандартном LogoutView)
    path('logout/', views.logout_view, name='logout'),

    
]
