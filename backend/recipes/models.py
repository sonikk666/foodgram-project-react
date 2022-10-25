from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Tag(models.Model):
    title = models.CharField(max_length=100, unique=True)
    color = models.CharField(max_length=16, unique=True) # изменить на hex-код
    slug = models.SlugField(unique=True)
    # может быть сделать автодобавление слага

    def __str__(self):
        return self.title

class Recipe(models.Model):
    """Модель рецептов."""
    class Meta:
        ordering = ['-pub_date']
        verbose_name = 'Рецепт'
        verbose_name_plural = 'Рецепты'

    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='recipes',
        verbose_name='Автор рецепта',
    )
    title  = models.CharField(max_length=100)
    # image = models.ImageField(
    #     'Картинка',
    #     upload_to='recipes/',
    #     blank=True,  # убрать
    # )
    text = models.TextField(
        'Текстовое описание рецепта',
        help_text='Введите текст рецепта',
    )

    # ingredients = models.ForeignKey(
        
    tag = models.ForeignKey(
        Tag,
        blank=True,  # убрать
        null=True,  # убрать
        on_delete=models.SET_NULL,
        related_name='recipes',
        verbose_name='Тег',
        help_text='Метка, к которой будет относиться рецепт',
    )
    time_cooking = models.TimeField(
        'Время приготовления',
        help_text='Время приготовления в минутах',       
        auto_now=False,
        auto_now_add=False,
    )
    pub_date = models.DateTimeField(
        'Дата публикации',
        auto_now_add=True,
    )

    def __str__(self):
        return self.title


