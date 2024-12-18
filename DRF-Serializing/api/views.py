from django.shortcuts import render
from rest_framework import generics
from .serializers import *
from .models import *

class PostList(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializers
    
    def perform_create(self, serializer):
        serializer.save(author = self.request.user)
        

class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializers