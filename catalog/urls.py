from django.conf.urls import url
from django.urls import path, include
from .views import (
    CatalogListApiView,
    CatalogDetailApiView,
)

urlpatterns = [
    path('', CatalogListApiView.as_view()),
    path('<int:catalog_id>', CatalogDetailApiView.as_view()),
]
