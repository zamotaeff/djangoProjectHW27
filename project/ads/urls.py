from django.urls import path
from ads.views import (
    index_route,
    AdsList,
    CategoriesList,
    AdsDetailView,
    CategoriesDetailView
)

urlpatterns = [
    path('', index_route),
    path('ad/', AdsList.as_view()),
    path('ad/<int:pk>/', AdsDetailView.as_view()),
    path('cat/', CategoriesList.as_view()),
    path('cat/<int:pk>/', CategoriesDetailView.as_view())
]
