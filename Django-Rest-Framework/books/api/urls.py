from django.urls import path
from .views import BookListCreateAPIView, BookDetailAPIView, CommentCreateAPIView, CommentDetailAPIView, CommentListAPIView

urlpatterns = [
    path('books/', BookListCreateAPIView.as_view(), name='book-list-create'),
    path('books/<int:pk>/', BookDetailAPIView.as_view(), name='book-detail'),
    path('books/<int:book_pk>/comment/', CommentCreateAPIView.as_view(), name='write-comment'),
    path('comments/', CommentListAPIView.as_view(), name='comment-list'),
    path('comments/<int:pk>/', CommentDetailAPIView.as_view(), name='comment-detail'),
]