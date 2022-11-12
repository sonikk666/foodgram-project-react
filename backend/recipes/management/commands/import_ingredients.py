import csv

from django.core.management.base import BaseCommand

from recipes.models import Ingredient

MODELS = (
    Ingredient,
)

ALREDY_LOADED_ERROR_MESSAGE = """
If you need to reload the data from the CSV file,
first delete the db.sqlite3 file to destroy the database.
Then, run `python manage.py migrate` for a new empty
database with tables"""


class Command(BaseCommand):
    help = 'Loads data from .csv'

    def handle(self, *args, **kwargs):

        for model in MODELS:
            if model.objects.exists():
                print('data already loaded...exiting.')
                print(ALREDY_LOADED_ERROR_MESSAGE)
                return

        print("Data successfuly loading")

        reader = csv.reader(open(
            '../data/ingredients.csv', newline='', encoding='utf-8'
        ))
        for row in reader:
            _, created = Ingredient.objects.get_or_create(
                name=row[0],
                measurement_unit=row[1],
            )
