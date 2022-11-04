from django.shortcuts import get_object_or_404
from drf_extra_fields.fields import Base64ImageField
from recipes.models import (Ingredient, IngredientAmount, Recipe,  # Subscribe,
                            Tag, User)
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'email', 'id', 'username',
            'first_name', 'last_name',
            'is_subscribed',
        )


class TagSerializer(serializers.ModelSerializer):

    class Meta:
        model = Tag
        fields = ('id', 'name', 'color', 'slug')


class IngredientSerializer(serializers.ModelSerializer):

    class Meta:
        model = Ingredient
        fields = ('id', 'name', 'measurement_unit',)


class IngredientAmountSerializer(serializers.ModelSerializer):
    id = serializers.PrimaryKeyRelatedField(
        source='ingredient', read_only=True
    )
    name = serializers.SlugRelatedField(
        slug_field='name', source='ingredient', read_only=True
    )
    measurement_unit = serializers.SlugRelatedField(
        slug_field='measurement_unit',
        source='ingredient', read_only=True
    )

    class Meta:
        model = IngredientAmount
        fields = ('id', 'name', 'measurement_unit', 'amount',)


class RecipeSerializer(serializers.ModelSerializer):
    # author = serializers.StringRelatedField(
    #     read_only=True, default=serializers.CurrentUserDefault()
    # )
    author = UserSerializer(read_only=True, many=False)
    tags = TagSerializer(read_only=True, many=True)

    ingredients = IngredientAmountSerializer(
        many=True,
        # source='ingredient',
        source='ingredientamount_set',
        read_only=True,
    )
    image = Base64ImageField(
    )

    # is_favorited = serializers.SerializerMethodField()
    # Recipe.objects.filter(favorites__in=["True"])

    class Meta:
        model = Recipe
        fields = (
            'id', 'tags', 'author', 'ingredients', 'is_favorited',
            'is_in_shopping_cart', 'name', 'image', 'text', 'cooking_time',
        )
        read_only_fields = ('author',)

    def validate(self, data):
        ingredients = self.initial_data.get('ingredients')
        if not ingredients:
            raise serializers.ValidationError(
                {'ingredients': 'Без ингредиентов не приготовить'}
            )
        ingredient_list = []
        for ingredient_item in ingredients:
            ingredient = get_object_or_404(
                Ingredient, id=ingredient_item['id']
            )
            if ingredient in ingredient_list:
                raise serializers.ValidationError(
                    'Ингридиенты должны быть уникальными'
                )
            ingredient_list.append(ingredient)
            if int(ingredient_item['amount']) < 0:
                raise serializers.ValidationError(
                    {
                        'ingredients': ('Убедитесь, что значение количества '
                                        'ингредиента больше 0')
                    }
                )
        data['ingredients'] = ingredients
        return data

    def create_ingredients(self, ingredients, recipe):
        for ingredient in ingredients:
            IngredientAmount.objects.create(
                recipe=recipe,
                ingredient_id=ingredient.get('id'),
                amount=ingredient.get('amount'),
            )

    def create(self, validated_data):

        image = validated_data.pop('image')
        tags_data = self.initial_data.get('tags')
        ingredients_data = validated_data.pop('ingredients')

        recipe = Recipe.objects.create(image=image, **validated_data)

        recipe.tags.set(tags_data)
        self.create_ingredients(ingredients_data, recipe)

        return recipe
