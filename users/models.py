from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    role = models.CharField(
        max_length=51,
        choices=(
            ("operator","operator"),
            ("driver","driver"),
            ("owner","owner")
        )
    )
