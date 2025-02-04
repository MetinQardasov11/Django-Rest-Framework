from django.contrib import admin
from .models import Article, Author

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publication_date', 'is_active')
    
    
admin.site.register(Author)