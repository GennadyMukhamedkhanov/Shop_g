from django.db import models


class Warehouse(models.Model):
    name = models.CharField(verbose_name='Название продукта', max_length=35)
    amount = models.IntegerField(verbose_name='Количество')
    measurement_unit = models.CharField(verbose_name='Единица измерения', max_length=20)
    manufacturer = models.ForeignKey(
        to='Manufacturer',
        verbose_name='Производитель',
        related_name='warehouses_manufacturer',
        on_delete=models.CASCADE
    )

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Склад'
        verbose_name_plural = 'Склады'
        app_label = 'products'
