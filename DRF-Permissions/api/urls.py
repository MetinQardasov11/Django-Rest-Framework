from django.urls import path
from .views import BookViewSet, BookListViewSet

urlpatterns = [
    path('books/', BookViewSet.as_view({'get': 'list', 'post': 'create'}), name='books'),
    path('books/<int:pk>/', BookListViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='book'),
]
