from django.urls import path
from .views import BlogListView, BlogDetailView

app_name = 'blogs'

urlpatterns = [
    path('', BlogListView.as_view(), name='blog_list'),  # Bloglar ro'yxati
    path('<slug:slug>/', BlogDetailView.as_view(), name='blog_detail'),  # Batafsil blog
]
