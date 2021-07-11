from django.urls import path, include
from .models import Contact
from .views import ContactRegister
from .serializers import ContactSerializer
from rest_framework import generics

urlpatterns = [
    path('', generics.ListCreateAPIView.as_view(queryset=Contact.objects.all(), serializer_class=ContactSerializer)),
]
