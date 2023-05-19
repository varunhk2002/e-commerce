from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class Product(models.Model):
    title = models.CharField(max_length=25, null=True)
    category = models.CharField(max_length=25, null=True)
    img_url = models.TextField(null=True)
    description = models.TextField(null=True)
    price = models.FloatField(null=True)
    stock_amt = models.IntegerField(null=True)
    brand = models.CharField(max_length=25, null=True)

class Cart(models.Model):
    prod_id = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='product_cart')
    username = models.CharField(max_length=25)

class Wishlist(models.Model):
    prod_id = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='product_wish')
    username = models.CharField(max_length=25)