from django.db import models

class City(models.Model):
    name = models.CharField(max_length=50)
    city = models.Manager()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Город'
        verbose_name_plural = 'Города'
        app_label = 'products'