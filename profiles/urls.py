#____________________________________________________________________ PROFILES/URLS.PY
from django.urls import path, include
from . import views

urlpatterns = [
    path('profile/', views.user_profile, name='profile'),
]