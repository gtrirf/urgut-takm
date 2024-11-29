from django.db import models
from ckeditor.fields import RichTextField
from apps.core.models import TimeBase
from django.utils.text import slugify
from django.urls import reverse


class Blog(TimeBase):
    title = models.CharField(max_length=300, unique=True)
    body = RichTextField()
    slug = models.SlugField(max_length=300, unique=True, blank=True)

    class Meta:
        db_table = 'blog'
    
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog:blog_detail', kwargs={'slug': self.slug})

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)


class BlogImages(TimeBase):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='blog_images/')

    class Meta:
        db_table = 'blog_images'
    
    def __str__(self):
        return f'image of {self.blog.title}'


