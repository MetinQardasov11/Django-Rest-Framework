from django.contrib import admin
from .models import Book, Comment

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('name', 'author', 'publication_date')
    list_per_page = 25


admin.site.register(Comment)