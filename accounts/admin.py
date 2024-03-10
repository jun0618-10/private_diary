from django.contrib import admin
from .models import CustomUser
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth import get_user_model
from django.contrib.admin.models import LogEntry

# Register your models here.



admin.site.register(CustomUser)