from django.db import models


class Feedback(models.Model):
    description = models.CharField(verbose_name='Описание', max_length=300)
    like = models.BooleanField()
    client = models.ForeignKey(
        to='users.User',
        verbose_name='Автор',
        related_name='feedbacks_client',
        on_delete=models.CASCADE
    )
    product = models.ForeignKey(
        to='Product',
        verbose_name='Продукт',
        related_name='feedback_product',
        on_delete=models.CASCADE
    )

    def __str__(self):
        return f'{self.product}  {self.description}'

    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'
        app_label = 'products'
