from django.urls import path
# from .views import artice_list_create_api_view, article_detail_view
from .views import ArticleListCreateAPIView, ArticleDetailAPIView, AuthorListCreateAPIView


urlpatterns = [
    path('authors/', AuthorListCreateAPIView.as_view(), name='author-list-create'),
    path('articles/', ArticleListCreateAPIView.as_view(), name='article-list-create'),
    path('articles/<int:pk>', ArticleDetailAPIView.as_view(), name='article-detail'),
]


# urlpatterns = [
#     path('articles/', artice_list_create_api_view, name='article-list-create'),
#     path('articles/<int:pk>', article_detail_view, name='article-detail'),
# ]