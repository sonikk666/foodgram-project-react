# Generated by Django 2.2.19 on 2022-11-13 18:35

import json
import os

from django.conf import settings
from django.db import migrations

from recipes.models import Ingredient

PATH = os.path.join(settings.BASE_DIR, 'data/ingredients.json')


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0001_initial'),
    ]

    def load_ingredients(self, schema_editor):

        with open(file=PATH, encoding='utf-8') as json_file:
            data = json.load(json_file)
            for ingredient in data:

                Ingredient.objects.get_or_create(
                    name=ingredient.get('name'),
                    measurement_unit=ingredient.get('measurement_unit'),
                )

    operations = [
        migrations.RunPython(load_ingredients)
    ]
