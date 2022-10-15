import csv
import json

FILE_CSV_ADS = '../uploads/ads.csv'
FILE_CSV_CATEGORIES = '../uploads/categories.csv'

FILE_JSON_ADS = '../uploads/ads.json'
FILE_JSON_CATEGORIES = '../uploads/categories.json'


def convert_ads_csv_to_json():
    with open(FILE_CSV_ADS, 'r', encoding='utf-8') as csvfile:
        csv_reader = csv.DictReader(csvfile)
        rows = list(csv_reader)

    with open(FILE_JSON_ADS, 'w', encoding='utf-8') as f:
        json.dump(rows, f, ensure_ascii=False)


def convert_categories_csv_to_json():
    with open(FILE_CSV_CATEGORIES, 'r', encoding='utf-8') as csvfile:
        csv_reader = csv.DictReader(csvfile)
        rows = list(csv_reader)

    with open(FILE_JSON_CATEGORIES, 'w', encoding='utf-8') as f:
        json.dump(rows, f, ensure_ascii=False)
