from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from .forms import MessagesForm
from .models import Messages
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from django.http import HttpResponse
from django.core.cache import cache  # Use Django's cache system for custom rate limiting

class MessagesCreateView(SuccessMessageMixin, CreateView):
    model = Messages
    form_class = MessagesForm
    template_name = 'messages/message_form.html'
    success_url = reverse_lazy('home')  # Xabar yuborilgandan so'ng qaytish sahifasi
    success_message = "Sizning xabaringiz muvaffaqiyatli yuborildi!"
    
    def dispatch(self, *args, **kwargs):
        # Get the user's IP address or other unique identifier
        user_ip = self.request.META.get('REMOTE_ADDR')
        cache_key = f"rate_limit:{user_ip}"  # Use the IP address as a unique key
        
        # Check if the rate limit has been exceeded
        if cache.get(cache_key):
            # Creating a link to the homepage
            homepage_url = reverse_lazy('home')  # Assuming your homepage URL is mapped to the name 'home'
            messages.error(self.request, f"Siz juda ko'p so'rov yubordingiz. Iltimos,<br> 5 daqiqa kuting yoki asosiy sahifaga qayting <a href='{homepage_url}'>bu yerga</a> bosing.")
            
            # Return a response with an error message and the link
            return HttpResponse(f"Siz juda ko'p so'rov yubordingiz. Iltimos,<br> 5 daqiqa kuting yoki asosiy sahifaga qayting. <a href='{homepage_url}' style='font-size:70px;'>Asosiy sahifa qaytish</a>.", status=429)
        
        # Proceed to dispatch the request if rate limit is not exceeded
        response = super().dispatch(*args, **kwargs)
        
        # Set the cache to block future requests from the same IP for 5 minutes
        cache.set(cache_key, 'blocked', timeout=300)  # 5 minutes timeout (300 seconds)
        
        return response

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, "Xabaringiz muvaffaqiyatli yuborildi!")
        return response
