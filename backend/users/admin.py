from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

from .models import Subscribe


class SubscribeAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'author')
    search_fields = ('user', 'author')
    list_filter = ('user', 'author')
    empty_value_display = '-пусто-'


class UserAdmin(UserAdmin):
    list_filter = ('username',)


admin.site.unregister(User)
admin.site.register(User, UserAdmin)
admin.site.register(Subscribe, SubscribeAdmin)
