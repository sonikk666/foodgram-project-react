from django.contrib import admin

from .models import Ingredient, IngredientAmount, Recipe, Tag


class IngredientAmountInline(admin.TabularInline):
    model = IngredientAmount
    extra = 1


class RecipeAdmin(admin.ModelAdmin):
    inlines = (IngredientAmountInline,)
    list_display = ('name', 'author', 'count_favorites', 'show_tags')
    search_fields = ('name',)
    list_filter = ('author', 'name', 'tags', 'pub_date',)
    empty_value_display = '-пусто-'

    def show_tags(self, recipe):
        # Вывод тегов в админке
        tags = []
        for tag in Recipe.objects.values_list('tags__name', flat=True):
            tags.append(f'#{tag}')
        return ' '.join(tags)

    show_tags.short_description = 'Теги'

    def count_favorites(self, obj):
        return obj.favorites.count()


class IngredientAdmin(admin.ModelAdmin):
    list_display = ('name', 'measurement_unit')
    search_fields = ('name',)
    list_filter = ('name',)


class TagAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'color')


admin.site.register(Recipe, RecipeAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(Ingredient, IngredientAdmin)
