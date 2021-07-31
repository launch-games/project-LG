from rest_framework import generics
from .models import inquiries
from .serializers import InquiriesSerializer

class inquiriesRegister(generics.ListCreateAPIView):
    queryset = inquiries.objects.all()
    serializer_class = InquiriesSerializer
