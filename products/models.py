from django.conf import settings
from django.db import models


class Store(models.Model):
    title = models.CharField(max_length=1000)
    address = models.CharField(max_length=5000, blank=True)

    class Meta:
        verbose_name = 'Магазин'
        verbose_name_plural = 'Магазины'

    def __str__(self):
        return self.title


class Product(models.Model):
    title = models.CharField(max_length=1000)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    photo = models.ImageField(upload_to=settings.PRODUCTS, blank=True)

    store = models.ForeignKey(Store, on_delete=models.SET_NULL,
                              blank=True, null=True)

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'

    def __str__(self):
        return self.title



