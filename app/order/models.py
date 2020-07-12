from django.db import models
from django.utils.translation import gettext_lazy as _


# Create your models here.
from product.models import Product


class TimeStampedModel(models.Model):
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
       abstract = True


class Order(TimeStampedModel):
    user = models.ForeignKey('members.User', verbose_name=_('구매자'), on_delete=models.DO_NOTHING)
    total_price = models.PositiveIntegerField(_('총 가격'), default=0)

    def set_total_price(self):
        self.total_price = sum([items.price for items in self.items.all()])
        self.save()


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey(Product, on_delete=models.PROTECT, related_name='order_products')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return '{}'.format(self.id)

    def get_item_price(self):
        return self.price * self.quantity


class Payment(TimeStampedModel):
    STATUS_CHOICE = [
        ('S', '결제 완료'),
        ('C', '결제 취소')
    ]
    order = models.ForeignKey(Order, verbose_name='주문', on_delete=models.CASCADE)
    status = models.CharField(choices=STATUS_CHOICE, verbose_name='결제 상태', max_length=1)