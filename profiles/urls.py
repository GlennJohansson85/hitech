#____________________________________________________________________ PROFILES/URLS.PY
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.profile, name='profile'),
    path('accounts/', include('allauth.urls')),
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
]
