from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

from article.models import Article, Author
from article.api.serializers import ArticleSerializers, AuthorSerializers

from rest_framework.views import APIView
from rest_framework.generics import get_object_or_404



class AuthorListCreateAPIView(APIView):
    
    def get(self, request):
        authors = Author.objects.all()
        serializer = AuthorSerializers(authors, many=True, context={'request': request})
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request):
        serializer = AuthorSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class ArticleListCreateAPIView(APIView):
    
    def get(self, request):
        article_instance = Article.objects.filter(is_active=True)
        serializer = ArticleSerializers(article_instance, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request):
        serializer = ArticleSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class ArticleDetailAPIView(APIView):

    def get_object(self, pk):
        article_instance = get_object_or_404(Article, pk=pk)
        return article_instance

    def get(self, request, pk):
        article_instance = self.get_object(pk=pk)
        serializer = ArticleSerializers(article_instance)
        return Response(serializer.data)
    
    def put(self, request, pk):
        article_instance = self.get_object(pk=pk)
        serializer = ArticleSerializers(article_instance, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response( serializer.errors ,status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        article_instance = self.get_object(pk=pk)
        article_instance.delete()
        return Response(
            {
                'success': True,
                'message': f'Article with id: {pk} deleted successfully'
            },
            status=status.HTTP_204_NO_CONTENT
        )



# --------------     Function Based Views     --------------
# @api_view(['GET', 'POST'])
# def artice_list_create_api_view(request):
    
#     if request.method == 'GET':
#         articles = Article.objects.filter(is_active=True)
#         serializer = ArticleSerializers(articles, many=True)
#         return Response(serializer.data, status=status.HTTP_200_OK)
    
#     elif request.method == 'POST':
#         serializer = ArticleSerializers(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(status=status.HTTP_400_BAD_REQUEST)
    

# @api_view(['GET', 'PUT', 'DELETE'])
# def article_detail_view(request, pk):
#     try:
#         article_instance = Article.objects.get(pk=pk)
#     except Article.DoesNotExist:
#         return Response(
#             {
#                 'errors': {
#                     'code': 404,
#                     'message': f'Article with id: {pk} not found'
#                 }
#             },
#             status=status.HTTP_404_NOT_FOUND
#         )
#     if request.method == 'GET':
#         serializer = ArticleSerializers(article_instance)
#         return Response(serializer.data)
    
#     elif request.method == 'PUT':
#         serializer = ArticleSerializers(article_instance, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(status=status.HTTP_400_BAD_REQUEST)
    
#     elif request.method == 'DELETE':
#         article_instance.delete()
#         return Response(
#             {
#                 'success': True,
#                 'message': f'Article with id: {pk} deleted successfully'
#             },
#             status=status.HTTP_204_NO_CONTENT
#         ) 