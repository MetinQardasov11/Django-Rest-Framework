from books.api.serializers import BookSerializer, CommentSerializer
from books.models import Book, Comment

from rest_framework.generics import GenericAPIView
from rest_framework import generics
from rest_framework.generics import get_object_or_404
from rest_framework import permissions
from rest_framework.exceptions import ValidationError

from .permissions import IsAdminOrReadOnly, IsOwnerOrReadOnly
from .pagination import SmallPagination, LargePagination


class BookListCreateAPIView(generics.ListCreateAPIView):
    queryset = Book.objects.all().order_by('-id')
    serializer_class = BookSerializer
    permission_classes = [IsAdminOrReadOnly]


class BookDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAdminOrReadOnly]


class CommentListAPIView(generics.ListAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAdminOrReadOnly]
    

class CommentCreateAPIView(generics.CreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAdminOrReadOnly]
    
    
    def perform_create(self, serializer):
        book_pk = self.kwargs.get('book_pk')
        book = get_object_or_404(Book, pk=book_pk)
        user_comment = self.request.user
        comments = Comment.objects.filter(book=book, commenter=user_comment)
        
        if comments.exists():
            raise ValidationError('You have already commented on this book')
        
        serializer.save(book = book, commenter = user_comment)
    

class CommentDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsOwnerOrReadOnly]