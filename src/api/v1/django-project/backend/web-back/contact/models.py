from django.db import models

class Contact(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=100)
    contact = models.TextField(max_length=1000)

    def __str__(self):
        return self.contact