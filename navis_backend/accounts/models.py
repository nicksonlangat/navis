import uuid
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _

from .managers import UserManager

class User(AbstractUser):
    class Role(models.TextChoices):
        STAFF = "STAFF", "Staff"
        MANAGER = "MANAGER", "Manager"
        ADMIN = "ADMIN", "Admin"
    username = None
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    email = models.EmailField(_("email address"), unique=True)
    id_number = models.CharField(max_length=10, blank=True, null=True)
    phone_number = models.CharField(max_length=10, blank=True, null=True)
    kra_pin = models.CharField(max_length=20, blank=True, null=True)
    role = models.CharField(max_length=255, choices=Role.choices, default=Role.STAFF)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = UserManager()

    def __str__(self):
        return self.email
