from django.urls import path, include
from .models import inquiries
from .views import inquiriesRegister
from .serializers import InquiriesSerializer
from rest_framework import generics

urlpatterns = [
    path('', generics.ListCreateAPIView.as_view(queryset=inquiries.objects.all(), serializer_class=InquiriesSerializer)),
]
