from django.urls import path
from ads.views import (
    index_route,
    AdsListView,
    AdsCreateView,
    CategoriesListView,
    CategoriesCreateView,
    AdsDetailView,
    CategoriesDetailView
)

urlpatterns = [
    path('', index_route),
    path('ad/', AdsListView.as_view()),
    path('ad/', AdsCreateView.as_view()),
    path('ad/<int:pk>/', AdsDetailView.as_view()),
    path('cat/', CategoriesListView.as_view()),
    path('cat/', CategoriesCreateView.as_view()),
    path('cat/<int:pk>/', CategoriesDetailView.as_view())
]
