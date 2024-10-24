from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission

class CustomUser(AbstractUser):
    HOST = 'host'
    GUEST = 'guest'
    ROLE_CHOICES = [
        (HOST, 'Host'),
        (GUEST, 'Guest'),
    ]
    
    role = models.CharField(max_length=10, choices=ROLE_CHOICES)
    phone_number = models.CharField(max_length=15, blank=True, null=True)

    # Override the groups field
    groups = models.ManyToManyField(
        Group,
        related_name='customuser_set',  # Change this to something unique
        blank=True,
    )

    # Override the user_permissions field
    user_permissions = models.ManyToManyField(
        Permission,
        related_name='customuser_set',  # Change this to something unique
        blank=True,
    )

    def __str__(self):
        return self.username
