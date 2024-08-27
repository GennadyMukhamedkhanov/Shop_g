from django.db import models


class Product(models.Model):
    name = models.ForeignKey(
        to='Warehouse',
        verbose_name='Название продукта',
        related_name='products_warehouse',
        on_delete=models.CASCADE
    )
    cost_product = models.IntegerField(verbose_name='Стоимость продукта')
    measurement_unit = models.CharField(verbose_name='Единица измерения', max_length=15)
    description = models.CharField(verbose_name='Описание', max_length=300)
    image = models.ImageField(upload_to='image/', verbose_name='Изображение', null=True, blank=True)


    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'
        app_label = 'products'
