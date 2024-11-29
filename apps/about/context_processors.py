from .models import Social

def socials_context(request):
    socials = Social.objects.all()
    return {'socials': socials}
