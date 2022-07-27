from django.conf.urls import url
from django.urls import path, include
from .views import (
    BookListApiView,
    BookDetailApiView,
)

urlpatterns = [
    path('', BookListApiView.as_view()),
    path('<int:book_id>', BookDetailApiView.as_view()),
]
