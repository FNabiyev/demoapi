from django.contrib import admin
from django.contrib.auth.models import User, Group
from .models import Users

admin.site.unregister(User)
admin.site.unregister(Group)


@admin.register(Users)
class UsersAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'username', 'password', 'birthday', 'address', 'date')
    list_display_links = ('id', 'first_name',)
    date_hierarchy = 'date'
