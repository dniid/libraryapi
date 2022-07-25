from django.conf.urls import url
from django.urls import path, include
from .views import (
    BookListApiView,
    BookDetailApiView,
)

urlpatterns = [
    path('api', BookListApiView.as_view()),
    path('api/<int:book_id>', BookDetailApiView.as_view()),
]
