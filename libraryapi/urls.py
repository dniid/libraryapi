from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api_auth/', include('rest_framework.urls')),
    path('catalog/', include('catalog.urls')),
    path('book/', include('book.urls')),
    path('author/', include('author.urls')),
]
