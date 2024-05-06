#____________________________________________________________________ PROFILES/SIGNALS.PY
from django.db.models.signals import post_save
from django.dispatch import receiver
from allauth.account.signals import user_signed_up
from .models import UserProfile

@receiver(user_signed_up)
def create_user_profile(sender, user, request, **kwargs):
    UserProfile.objects.create(user=user)