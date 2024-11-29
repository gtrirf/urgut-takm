from django.contrib import admin
from .models import Blog, BlogImages


class BlogImagesInline(admin.TabularInline):
    model = BlogImages
    extra = 1
    fields = ['image']
    max_num = 5


@admin.register(Blog)
class blogAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'created_at', 'updated_at')
    search_fields = ['title', 'body']
    fields = ['slug','title', 'body', 'created_at', 'updated_at']
    readonly_fields = ['slug','created_at', 'updated_at']
    inlines = [BlogImagesInline]