#____________________________________________________________________ PROFILES/URLS.PY
from django.urls import path, include
from . import views

urlpatterns = [
    path('profile/', views.user_profile, name='profile'),
    path('login/', views.user_login, name='login'),
    path('register/', views.user_register, name='register'),
]