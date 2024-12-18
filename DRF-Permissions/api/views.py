from django.shortcuts import render
from rest_framework import viewsets
from .models import Book
from .serializers import BookSerializer, BookListSerializer
from .permissions import *

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsSuperUser]
    
    def get_serializer_class(self):
        if self.action == 'list':
            return BookListSerializer
        return BookSerializer
    
class BookListViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookListSerializer
    permission_classes = [IsSuperUser]