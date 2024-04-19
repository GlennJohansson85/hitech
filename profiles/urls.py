#____________________________________________________________________ PROFILES/URLS.PY
from django.urls import path, include
from . import views

urlpatterns = [
    path('profile/', views.profile, name='profile'),
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
]