from django.contrib import admin
from .models import Book, Author


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'nickname']
    search_fields = ['first_name', 'last_name', 'nickname']
    fields = ['first_name', 'last_name', 'nickname']


@admin.register(Book)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'times_read', 'created_at', 'updated_at')
    search_fields = ['title', 'author']
    fields = ['title', 'author', 'cover_image', 'times_read', 'created_at', 'updated_at']
    readonly_fields = ['created_at', 'updated_at']