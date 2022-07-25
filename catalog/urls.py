from django.conf.urls import url
from django.urls import path, include
from .views import (
    CatalogListApiView,
    CatalogDetailApiView,
)

urlpatterns = [
    path('api', CatalogListApiView.as_view()),
    path('api/<int:catalog_id>', CatalogDetailApiView.as_view()),
]
