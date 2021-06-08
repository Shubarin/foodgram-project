import csv

from django.core.management.base import BaseCommand

from foodgram.settings import BASE_DIR
from recipes.models import Ingredient, Measurement

file_name = f'{BASE_DIR}/fixtures/ingredients.csv'


class Command(BaseCommand):
    help = 'Closes the specified poll for voting'

    def handle(self, *args, **options):
        with open(file_name) as csv_file:
            reader = csv.reader(csv_file)
            for line in reader:
                name, unit = line
                unit, create = Measurement.objects.get_or_create(name=unit)
                Ingredient.objects.get_or_create(name=name,
                                                 unit_of_measurement=unit)
