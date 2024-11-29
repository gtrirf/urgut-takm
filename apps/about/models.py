from django.core.exceptions import ValidationError
from django.db import models
from apps.core.models import TimeBase
from django.utils.safestring import mark_safe


class About(TimeBase):
    title = models.CharField(max_length=255, null=True, blank=True)
    body = models.TextField()
    image = models.ImageField(upload_to='about_images/', null=True, blank=True)
    about_image = models.TextField(null=True, blank=True)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        db_table = 'about'
        ordering = ['order']

    def __str__(self):
        return self.title


class Social(TimeBase):
    social_name = models.CharField(max_length=255)
    social_url = models.CharField(max_length=300)

    class Meta:
        db_table = 'social'

    def __str__(self):
        return self.social_name


class MainPageImages(TimeBase):
    image = models.ImageField(upload_to='mainimages/')

    def photo_tag(self):
        if self.image:
            return mark_safe(
                f'<img src="{self.image.url}" width="200px" />'
            )
        return "No Image"

    class Meta:
        db_table = 'images'

    def __str__(self):
        return f'Maipage Images'


class ImageText(models.Model):
    image_text = models.CharField(max_length=255)

    def clean(self):
        if not self.pk and ImageText.objects.exists():
            raise ValidationError("Faqat bitta Text yozish mumkin.")

    def __str__(self):
        return self.image_text


