from django.db import models


class Shopping_cart(models.Model):
    client = models.ForeignKey(
        to='users.User',
        verbose_name='Автор',
        related_name='shopping_cart_client',
        on_delete=models.CASCADE
    )
    product = models.ForeignKey(
        to='Product',
        verbose_name='Продукт',
        related_name='shopping_cart_product',
        on_delete=models.CASCADE
    )
    amount = models.IntegerField(verbose_name='Количество')


    def __str__(self):
        return f'{self.product}  {self.client}'

    class Meta:
        verbose_name = 'Корзина покупки'
        verbose_name_plural = 'Корина покупок'
        app_label = 'products'
