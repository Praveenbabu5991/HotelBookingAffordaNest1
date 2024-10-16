from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    HOST = 'host'
    GUEST = 'guest'
    ROLE_CHOICES = [
        (HOST, 'Host'),
        (GUEST, 'Guest'),
    ]
    
    role = models.CharField(max_length=10, choices=ROLE_CHOICES)
    phone_number = models.CharField(max_length=15, blank=True, null=True)

    def __str__(self):
        return self.username
