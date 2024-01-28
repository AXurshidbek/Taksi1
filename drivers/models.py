from django.db import models
from users.models import CustomUser


class CarCategory(models.Model):
    type=models.CharField(max_length=30)
    minimum=models.PositiveIntegerField()
    sum_per_km=models.PositiveIntegerField()
    waiting_cost=models.PositiveIntegerField()
    baggage_cost=models.PositiveIntegerField()
    bonus_percent=models.PositiveSmallIntegerField()
    firm_percent=models.PositiveIntegerField()

    def __str__(self):
        return self.type

class Driver(CustomUser):
    first_name=None
    is_staff=None
    is_superuser=None
    fullname = models.CharField(max_length=55)
    phone=models.CharField(max_length=31)
    photo=models.FileField()
    car_type=models.CharField(max_length=31)
    car_number=models.CharField(max_length=10)
    birth_date=models.DateField()
    sms_code=models.CharField(max_length=15)
    balance = models.PositiveIntegerField(default=0)
    confirmed = models.BooleanField(default=False)
    gender = models.CharField(max_length=10, default='Erkak')
    has_baggage = models.BooleanField()
    category = models.ForeignKey(CarCategory, on_delete=models.SET_NULL, null=True)
    created_at = models.DateField(auto_now_add=True)

    def str(self):
        return self.fullname



