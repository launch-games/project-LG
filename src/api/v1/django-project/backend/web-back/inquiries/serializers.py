from rest_framework.serializers import ModelSerializer
from .models import inquiries

class InquiriesSerializer(ModelSerializer):
    class Meta:
        model = inquiries
        fields = ('name','email','inquiries',)
