import json

from django.http import JsonResponse
from django.utils.decorators import method_decorator

from django.views.decorators.csrf import csrf_exempt
from django.views.generic import DetailView, CreateView, ListView

from ads.models import Ads, Category


def index_route(request):

    response = JsonResponse({"status": "ok"})

    return response


class AdsListView(ListView):
    model = Ads

    def get(self, request, *args, **kwargs):
        response = []

        for item in self.get_queryset():
            response.append(
                {
                    "id": item.pk,
                    "name": item.name,
                    "author": item.author,
                    "price": item.price
                }
            )

        return JsonResponse(response, safe=False, json_dumps_params={"ensure_ascii": False})


@method_decorator(csrf_exempt, name="dispatch")
class AdsCreateView(CreateView):
    model = Ads

    def post(self, request, *args, **kwargs):
        ad_data = json.loads(request.body)

        ad = Ads(
            name=ad_data.get('name'),
            author=ad_data.get('author'),
            price=ad_data.get('price'),
            description=ad_data.get('description'),
            address=ad_data.get('address'),
            is_published=bool(ad_data.get('is_bublished'))
        )
        ad.save()

        return JsonResponse({
            "id": ad.pk,
            "name": ad.name,
            "author": ad.author,
            "price": ad.price,
            "description": ad.description,
            "address": ad.address,
            "is_published": ad.is_published
        })


class CategoriesListView(ListView):
    model = Category

    def get(self, request, *args, **kwargs):
        response = []

        for item in self.get_queryset():
            response.append(
                {
                    "id": item.pk,
                    "name": item.name
                }
            )

        return JsonResponse(response, safe=False, json_dumps_params={"ensure_ascii": False})


@method_decorator(csrf_exempt, name="dispatch")
class CategoriesCreateView(CreateView):
    model = Category

    def post(self, request, *args, **kwargs):
        category_data = json.loads(request.body)

        category = Category(name=category_data.get('name'))
        category.save()

        return JsonResponse({
            "id": category.pk,
            "name": category.name
        })


class AdsDetailView(DetailView):
    model = Ads

    def get(self, request, *args, **kwargs):
        qs = self.get_object()

        response = {
            "id": qs.pk,
            "name": qs.name,
            "author": qs.author,
            "price": qs.price,
            "description": qs.description,
            "address": qs.address,
            "is_published": qs.is_published
        }

        return JsonResponse(response, safe=False, json_dumps_params={"ensure_ascii": False})


class CategoriesDetailView(DetailView):
    model = Category

    def get(self, request, *args, **kwargs):
        qs = self.get_object()

        response = {
            "id": qs.pk,
            "name": qs.name
        }

        return JsonResponse(response, safe=False, json_dumps_params={"ensure_ascii": False})
