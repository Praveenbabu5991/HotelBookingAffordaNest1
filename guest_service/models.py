from django.db import models

# Create your models here.
from django.db import models
from user_service.models import CustomUser
from host_service.models import Bed

class Booking(models.Model):
    guest = models.ForeignKey(CustomUser, on_delete=models.CASCADE, limit_choices_to={'role': 'guest'})
    bed = models.ForeignKey(Bed, on_delete=models.CASCADE)
    check_in = models.DateField()
    check_out = models.DateField()
    includes_food = models.BooleanField(default=False)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Booking by {self.guest.username} for Bed {self.bed.bed_number}"
