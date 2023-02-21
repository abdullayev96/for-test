from django.db import models
from django.contrib.auth.models import AbstractUser
import uuid


class User(AbstractUser):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, unique=True, editable=False)
    phone_number = models.CharField(max_length=40)
    confirm = models.PositiveBigIntegerField(null=True, blank=True)

