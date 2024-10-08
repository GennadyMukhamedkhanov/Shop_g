from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    phone = models.CharField(max_length=14, verbose_name='Телефон')

    def __str__(self):
        return f'{self.username} {self.phone}'

    class Meta:
        verbose_name = 'Покупатель'
        verbose_name_plural = 'Покупатели'
        app_label = 'users'
