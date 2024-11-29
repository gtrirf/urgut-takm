from django.shortcuts import render
from django.views.generic import TemplateView
from apps.books.models import Book
from apps.blogs.models import Blog
from apps.about.models import MainPageImages, ImageText  # To'g'ri model nomlari bilan yangilang

class HomeView(TemplateView):
    template_name = 'main/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        # Kitoblar va bloglar
        context['latest_books'] = Book.objects.order_by('-created_at')[:8]
        context['latest_blogs'] = Blog.objects.order_by('-created_at')[:4]
        
        # Asosiy rasm va matnlar
        context['main_images'] = MainPageImages.objects.all()
        context['image_text'] = ImageText.objects.first()
        
        return context
