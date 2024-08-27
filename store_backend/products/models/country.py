from django.db import models

from products.models.city import City


class Country(models.Model):
    name = models.CharField(max_length=50, verbose_name='Название страны')
    city = models.ManyToManyField(to=City, verbose_name='Город', related_name='countries')
    country = models.Manager()
    vasia = models.Manager()
    objects = models.Manager()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Страна'
        verbose_name_plural = 'Страны'
        app_label = 'products'