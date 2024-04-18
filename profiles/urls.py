#____________________________________________________________________ PROFILES/URLS.PY
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.profile, name='profile'),
    path('login/', views.user_login, name='login'),
    path('register/', views.register, name='register'),
]