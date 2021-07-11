from rest_framework import generics
from .models import Contact
from .serializers import ContactSerializer

from django.core import mail
from django.core.mail import EmailMessage
from django.test import TestCase

class EmailTest(TestCase):
    def test_send_email(self):
        # メール送信処理
        EmailMessage(
            subject="件名です",
            body="本文です",
            from_email="user1@example.com",
            to=["user2@example.com"],
            cc=["user3@example.com", "user4@example.com"],
            bcc=["user5@example.com", "user6@example.com"],
        ).send()

class ContactRegister(generics.ListCreateAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer