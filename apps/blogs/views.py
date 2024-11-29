from django.views.generic import ListView, DetailView
from .models import Blog, BlogImages
from .forms import SearchForm
from django.shortcuts import render
from django.db.models import Q

def search(request):
    query = request.GET.get('q', '').strip()  # 'q' bu input name bilan mos bo'lishi kerak
    results = Blog.objects.none()  # Default bo'sh natija

    if query:  # Faqat qidiruv so'zi kiritilganda qidiruv amalga oshadi
        results = Blog.objects.filter(
            Q(title__icontains=query) | Q(body__icontains=query)
        )

    context = {
        'query': query,
        'results': results,
    }
    return render(request, 'main/search_results.html', context)


class BlogListView(ListView):
    model = Blog
    template_name = 'blog/blog_list.html'
    context_object_name = 'blogs'
    ordering = ['-created_at']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Blogga tegishli rasmlarni oling
        blog_images = BlogImages.objects.select_related('blog')
        context['blog_images'] = blog_images
        return context

class BlogDetailView(DetailView):
    model = Blog
    template_name = 'blog/blog_detail.html'
    context_object_name = 'blog'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['images'] = self.object.blogimages_set.all() 
        return context