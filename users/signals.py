from django.apps import apps
from django.contrib.auth import get_user_model
from django.core.signals import setting_changed
from django.dispatch import receiver
from .models import PhoneUser

@receiver(setting_changed)
def user_model_swapped(* setting, **kwargs):
    if setting == "AUTH_USER_MODEL":
        apps.clear_cache()
        get_user_model()
        PhoneUser._meta.apps.clear_cache()
        PhoneUser._meta.apps.get_models()