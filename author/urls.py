from django.conf.urls import url
from django.urls import path, include
from .views import (
    AuthorListApiView,
    AuthorDetailApiView,
)

urlpatterns = [
    path('api', AuthorListApiView.as_view()),
    path('api/<int:author_id>', AuthorDetailApiView.as_view()),
]
