from django.contrib import admin
from .models import Tweek
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

# Register your models here.
admin.site.register(Tweek)
admin.site.register(CustomUser, UserAdmin)