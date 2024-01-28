from django.db import models
from drivers.models import Driver
from users.models import CustomUser

class Operator(CustomUser):
    is_superuser = None
    first_name = None
    last_name = None
    is_staff = None
    email = None
    name = models.CharField(max_length=30)
    work_time = models.CharField(max_length=30)
    phone = models.CharField(max_length=13)

    def str(self):
        return self.name

class Clients(models.Model):
    phone = models.CharField(max_length=13)
    total_bonus = models.PositiveIntegerField()

    def str(self):
        return self.phone


class Order(models.Model):
    client = models.ForeignKey(Clients, on_delete=models.SET_NULL, null=True)
    driver = models.ForeignKey(Driver, on_delete=models.SET_NULL, null=True, blank=True)
    status = models.CharField(
        max_length=20,
        choices=(
            ('active', 'active'),
            ('olindi', 'olindi'),
            ('boshlandi', 'boshlandi'),
            ('yakunlandi', 'yakunlandi'),
            ('bekor qilindi', 'bekor qilindi'),
        )
    )
    total_sum = models.PositiveIntegerField()
    waiting_seconds = models.PositiveSmallIntegerField(default=0)
    baggage = models.BooleanField(default=False)
    for_women = models.BooleanField(default=False)
    starting_point = models.CharField(max_length=50)
    destination = models.CharField(max_length=50, null=True, blank=True)
    description = models.CharField(max_length=100, null=True, blank=True)
    grading = models.PositiveSmallIntegerField(null=True, blank=True)
    date_time = models.DateTimeField()


    def str(self):
        return self.client