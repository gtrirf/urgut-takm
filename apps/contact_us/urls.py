from django.urls import path
from .views import MessagesCreateView

urlpatterns = [
    path('messages/create/', MessagesCreateView.as_view(), name='message_create'),
]
