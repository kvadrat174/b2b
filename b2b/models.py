from django.db import models

class Company(models.Model):

    company_name = models.CharField(verbose_name='Company name', max_length=20)

class Product(models.Model):
    product_name = models.CharField(verbose_name='Product name',  max_length=20)


class Order(models.Model):
    buyer = models.ForeignKey(Company, related_name='Buyer', on_delete=models.CASCADE)
    seller = models.ForeignKey(Company, related_name='Seller', on_delete=models.CASCADE)

class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, related_name='order_items', on_delete=models.CASCADE)
    price = models.DecimalField(verbose_name='Price', max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField(verbose_name='Quantity', default=1)


