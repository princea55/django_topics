from django.db import models


# Create your models here.

class Contact(models.Model):
    name = models.CharField(max_length=20)

    class Meta:
        db_table = 'contact'

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=250)
    price = models.IntegerField(default=0, null=False, blank=False)

    class Meta:
        db_table = 'product'

    def __str__(self):
        return self.name


class SaleOrder(models.Model):
    name = models.CharField(max_length=10, unique=True, null=True, blank=False)
    contact = models.ForeignKey(Contact, related_name='sale_order_contact', on_delete=models.SET_NULL, default=None,
                                null=True)
    order_date = models.DateField(null=True, blank=False)

    class Meta:
        db_table = 'sale_order'

    def __str__(self):
        return self.name


class SaleOrderLine(models.Model):
    order_id = models.ForeignKey(SaleOrder, related_name='order_line_sale_order', on_delete=models.SET_NULL,
                                 default=None, null=True)
    product = models.ForeignKey(Product, related_name='order_line_product', on_delete=models.SET_NULL,
                                default=None, null=True)
    quantity = models.IntegerField(null=False, default=1, blank=False)
    unit_price = models.IntegerField(null=True, blank=False)
    unit_total = models.IntegerField(null=False, blank=False, default=0)

    class Meta:
        db_table = 'sale_order_line'

    def __str__(self):
        return self.order_id