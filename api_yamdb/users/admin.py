from django.contrib import admin

from .models import User


class UserAdmin(admin.ModelAdmin):
    list_display = ("pk", "email", "bio", "confirmation_code", "role")


admin.site.register(User, UserAdmin)
