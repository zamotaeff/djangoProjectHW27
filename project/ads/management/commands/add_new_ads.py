import json

from django.core.management import BaseCommand

from ads.models import Ads
from ads.helpers import FILE_JSON_ADS


class Command(BaseCommand):
    help = 'Add new object from json files'

    def handle(self, *args, **kwargs):

        with open(FILE_JSON_ADS, 'r', encoding='utf-8') as f:
            data = json.load(f)

            for item in data:
                new_ads = Ads(
                    name=item.get('name'),
                    author=item.get('author'),
                    price=item.get('price'),
                    description=item.get('description'),
                    address=item.get('address'),
                    is_published=bool(item.get('is_published'))
                )
                new_ads.save()
