from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from apps.blogs.views import search

urlpatterns = [
    path('admin/', admin.site.urls),
    path('blogs/', include('apps.blogs.urls')),
    path('about/', include('apps.about.urls')),
    path('books/', include('apps.books.urls')),
    path('contact/', include('apps.contact_us.urls')),
    path('', include('apps.core.urls')), 
    path('search/', search, name='search'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
