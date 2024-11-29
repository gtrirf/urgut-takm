from django.db import models
from apps.core.models import TimeBase
from django.core.exceptions import ValidationError


class Messages(TimeBase):
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255, null=True, blank=True)
    phone_number = models.CharField(max_length=30, null=True, blank=True)
    body =  models.TextField()

    class Meta:
        db_table = 'messages'

    def save(self, *args, **kwargs):
        if not self.email and not self.phone_number:
            raise ValidationError("Elektron pochta yoki telefon raqamdan kamida bittasi kiritilishi kerak.")
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name