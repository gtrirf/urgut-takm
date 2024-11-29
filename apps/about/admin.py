from django.contrib import admin
from .models import About, Social, MainPageImages, ImageText


@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    list_display = ('title', 'order', 'created_at', 'updated_at')
    fieldsets = (
        ('Main Title and Order', {
            'fields': ('title', 'order'),
            'classes': ('collapse',),
        }),
        ('Body Content', {
            'fields': ('body',),
            'classes': ('collapse',),
        }),
        ('Images', {
            'fields': ('image', 'about_image'),
            'classes': ('collapse',),
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',),
        }),
    )
    readonly_fields = ('created_at', 'updated_at')


@admin.register(Social)
class SocialsAdmin(admin.ModelAdmin):
    list_display = ['social_name', 'social_url', 'created_at', 'updated_at']
    fieldsets = (
        ('Social Information', {
            'fields': ('social_name', 'social_url'),
            'classes': ('collapse',),
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',),
        }),
    )
    readonly_fields = ('created_at', 'updated_at')


@admin.register(ImageText)
class ImageTextAdmin(admin.ModelAdmin):
    list_display = ['image_text']


@admin.register(MainPageImages)
class MainPageImagesTextAdmin(admin.ModelAdmin):
    list_display = ['photo_tag', '__str__']
    readonly_fields = ['created_at', 'updated_at']

