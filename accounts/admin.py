from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .views import User

class UserAdmin(UserAdmin):
    model = User
    list_display = ['id', 'username']

admin.site.register(User, UserAdmin)
