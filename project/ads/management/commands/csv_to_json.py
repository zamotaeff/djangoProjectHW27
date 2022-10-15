from django.core.management.base import BaseCommand

from project.ads.helpers import convert_ads_csv_to_json, convert_categories_csv_to_json


class Command(BaseCommand):
    help = 'Create json from csv files'

    def handle(self, *args, **kwargs):

        convert_ads_csv_to_json()

        convert_categories_csv_to_json()
