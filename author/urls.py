from django.conf.urls import url
from django.urls import path, include
from .views import (
    AuthorListApiView,
    AuthorDetailApiView,
)

urlpatterns = [
    path('', AuthorListApiView.as_view()),
    path('<int:author_id>', AuthorDetailApiView.as_view()),
]
