from rest_framework.serializers import ModelSerializer, StringRelatedField
from books.models import Book, Comment

class CommentSerializer(ModelSerializer):
    commenter = StringRelatedField(read_only=True)
    class Meta:
        model = Comment
        exclude = ['book']


class BookSerializer(ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'
        
    comments = CommentSerializer(many=True, read_only=True)