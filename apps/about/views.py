from django.shortcuts import render, get_object_or_404
from .models import About, MainPageImages, ImageText, Social

def about_view(request):
    about_items = About.objects.all().order_by('order')
    return render(request, 'about/about.html', {'about_items': about_items})


def footer_socials(request):
    socials = Social.objects.all()
    return {'socials': socials}
