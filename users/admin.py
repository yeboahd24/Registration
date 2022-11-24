from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

# Register your models here.

class CustomUserAdmin(UserAdmin):
    model = User
    list_display = [
        "first_name",
        "last_name",
        "date_joined",
        "email",
        "phone",
    ]
    list_display_links = (
        "first_name",
        "last_name",
        "date_joined",
        "email",
        "phone",
    )
    ordering = ("-date_joined",)


admin.site.register(User, CustomUserAdmin)
