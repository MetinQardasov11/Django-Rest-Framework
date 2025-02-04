from rest_framework import serializers
from article.models import Article, Author
from datetime import datetime, date
from django.utils.timesince import timesince


class ArticleSerializers(serializers.ModelSerializer):
    time_since_pub = serializers.SerializerMethodField()
    # author = AuthorSerializers()
    
    class Meta:
        model = Article
        fields = '__all__'
        read_only_fields = ['id', 'created_at', 'updated_at']
        
    def get_time_since_pub(self, object):
        now = datetime.now()
        pub_date = object.publication_date
        if object.is_active:
            time_delta = timesince(pub_date, now)
            return time_delta
        else:
            return 'Article is not active'
    
    def validate_publication_date(self, timevalue):
        today = date.today()
        if timevalue > today:
            raise serializers.ValidationError('Publication date cannot be in the future')
        return timevalue



class AuthorSerializers(serializers.ModelSerializer):
    
    # articles = ArticleSerializers(many=True, read_only=True)
    articles = serializers.HyperlinkedRelatedField(
        many=True, 
        read_only=True, 
        view_name='article-detail'
    )
    
    class Meta:
        model = Author
        fields = '__all__'
        read_only_fields = ['id', 'created_at', 'updated_at']


class ArticleDefaultSerializers(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField()
    description = serializers.CharField()
    content = serializers.CharField()
    author = serializers.CharField()
    publication_date = serializers.DateField()
    is_active = serializers.BooleanField()
    created_at = serializers.DateField(read_only=True)
    updated_at = serializers.DateField(read_only=True)
    
    def create(self, validated_data):
        return Article.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.description = validated_data.get('description', instance.description)
        instance.content = validated_data.get('content', instance.content)
        instance.author = validated_data.get('author', instance.author)
        instance.publication_date = validated_data.get('publication_date', instance.publication_date)
        instance.is_active = validated_data.get('is_active', instance.is_active)
        instance.save()
        return instance
    
    def validate(self, data):
        if data['title'] == data['description']:
            raise serializers.ValidationError('Title and description cannot be the same')
        return data
    
    def validate_title(self, value):
        if len(value) < 20:
            raise serializers.ValidationError('Title must be at least 20 characters long')
        return value