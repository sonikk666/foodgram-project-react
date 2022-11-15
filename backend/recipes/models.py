from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()

COLOR_CHOICES = [
    ('#FFA500', 'Оранжевый'),
    ('#008000', 'Зелёный'),
    ('#0000FF', 'Синий'),
    ('#FF0000', 'Красный'),
]


class Tag(models.Model):
    name = models.CharField(max_length=200, unique=True)
    color = models.CharField(max_length=7, unique=True)
    slug = models.SlugField(max_length=200, unique=True)

    class Meta:
        ordering = ['name']
        verbose_name = 'Тег'
        verbose_name_plural = 'Теги'

    def __str__(self):
        return self.name


class Ingredient(models.Model):
    name = models.CharField(
        'Название ингредиента',
        max_length=200,
        help_text='Название ингредиента',
    )
    measurement_unit = models.CharField(
        'Единица измерения',
        max_length=200,
        help_text='Единица измерения',
    )

    class Meta:
        ordering = ['name']
        verbose_name = 'Ингредиент'
        verbose_name_plural = 'Ингредиенты'

    def __str__(self):
        return self.name


class Recipe(models.Model):
    """Модель рецептов."""
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='recipes',
        verbose_name='Автор рецепта',
    )
    name = models.CharField(
        'Название рецепта', max_length=100
    )
    image = models.ImageField(
        'Изображение блюда',
        upload_to='recipes/images/',
    )
    text = models.TextField(
        'Текстовое описание рецепта',
        help_text='Введите текст рецепта',
    )

    ingredients = models.ManyToManyField(
        Ingredient,
        through='IngredientAmount',
        related_name='recipes',
        verbose_name='Ингредиенты',
        help_text='Ингредиенты для рецепта',
    )

    tags = models.ManyToManyField(
        Tag,
        related_name='recipes',
        verbose_name='Тег',
        help_text='Метка, к которой будет относиться рецепт',
    )
    cooking_time = models.PositiveSmallIntegerField(
        'Время приготовления',
        help_text='Время приготовления в минутах',
    )
    pub_date = models.DateTimeField(
        'Дата публикации',
        auto_now_add=True,
    )

    class Meta:
        ordering = ['-pub_date']
        verbose_name = 'Рецепт'
        verbose_name_plural = 'Рецепты'

    def __str__(self):
        return self.name


class IngredientAmount(models.Model):
    ingredient = models.ForeignKey(
        Ingredient, on_delete=models.CASCADE,
        related_name='recipe',
    )
    recipe = models.ForeignKey(
        Recipe,
        on_delete=models.CASCADE,
    )
    amount = models.PositiveSmallIntegerField(
        'Количество',
        help_text='Количество',
    )

    def __str__(self):
        return f'{self.ingredient} {self.recipe}'


class Favorite(models.Model):
    user = models.ForeignKey(
        User,
        verbose_name='Пользователь',
        on_delete=models.CASCADE,
        related_name='favorites'
    )
    recipe = models.ForeignKey(
        Recipe,
        verbose_name='Рецепт',
        on_delete=models.CASCADE,
        related_name='favorites',
    )

    class Meta:
        ordering = ['-id']
        verbose_name = 'Избранное'
        verbose_name_plural = 'Избранные'


class ShoppingCart(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='shopping_cart',
        verbose_name='Пользователь',
    )
    recipe = models.ForeignKey(
        Recipe,
        on_delete=models.CASCADE,
        related_name='shopping_cart',
        verbose_name='Рецепт',
    )

    class Meta:
        ordering = ['-id']
        verbose_name = 'Корзина'
        verbose_name_plural = 'В корзине'
