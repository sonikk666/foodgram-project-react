from django.contrib import admin

from .models import Ingredient, IngredientAmount, Recipe, Tag  # Subscribe


class IngredientAmountInline(admin.TabularInline):
    model = IngredientAmount
    extra = 1


class RecipeAdmin(admin.ModelAdmin):
    inlines = (IngredientAmountInline,)

    def show_tags(self, recipe):
        # Вывод тегов в админке
        tags = []
        for tag in recipe.tags.all():
            tags.append('#' + tag.name)
        return ' '.join(tags)

    show_tags.short_description = 'Теги'

    list_display = ('pk', 'name', 'text', 'pub_date', 'author', 'show_tags')
    search_fields = ('text',)
    list_filter = ('pub_date',)
    empty_value_display = '-пусто-'


admin.site.register(Recipe, RecipeAdmin)
admin.site.register(Tag)
admin.site.register(Ingredient)
# admin.site.register(Subscribe)
