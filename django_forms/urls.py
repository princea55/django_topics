from django.urls import path, include
from django_forms.views import email_sender

urlpatterns = [
    path('', email_sender, name='email_sender')
]
