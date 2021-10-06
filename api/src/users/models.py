from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _


class User(AbstractUser):
    phone = models.CharField(_('phone number'), max_length=20, blank=True)

    @property
    def name(self):
        if self.first_name and self.last_name:
            return f'{self.first_name} {self.last_name}'
        elif self.last_name:
            return self.last_name
        else:
            return self.first_name
