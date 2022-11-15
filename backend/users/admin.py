from django.contrib import admin

from .models import Subscribe


class SubscribeAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'author')
    search_fields = ('user', 'author')
    list_filter = ('user', 'author')
    empty_value_display = '-пусто-'


admin.site.register(Subscribe, SubscribeAdmin)
