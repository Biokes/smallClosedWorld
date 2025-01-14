from django.contrib import admin

from users_module.models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    pass
