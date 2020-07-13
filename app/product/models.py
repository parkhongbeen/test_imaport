from django.db import models
from django.utils.translation import gettext_lazy as _


# Create your models here.
class Product(models.Model):
    name = models.CharField(_('상품이름'), max_length=128)
    price = models.PositiveIntegerField(_('가격'))
    image = models.ImageField(_('상품 이미지'), upload_to='images/products', default='images/products/testimage.jpg')
    stock = models.PositiveIntegerField(_('재고'))

    class Meta:
        db_table = 'product'
        verbose_name = 'product'
        verbose_name_plural = 'product'

        def __str__(self):
            return self.name