from django.db import models


class Manufacturer(models.Model):
    name = models.CharField(verbose_name='Название компании', max_length=35)
    description = models.TextField(verbose_name='Описание')

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Компания'
        verbose_name_plural = 'Компании'
        app_label = 'products'
