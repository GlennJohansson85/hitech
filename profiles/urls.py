#____________________________________________________________________ PROFILES/URLS.PY
from django.urls import path
from . import views

urlpatterns = [
    path('', views.profile, name='profile'),
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
]
