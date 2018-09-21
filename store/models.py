import django.contrib.auth
from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=10000)

    def __str__(self):
        return self.name


class Tree(models.Model):
    HIGH_MAINT = 'HG'
    MEDIUM_MAINT = 'MD'
    LOW_MAINT = 'LW'
    MAINTENANCE_CHOICES = (
        (HIGH_MAINT, 'High Maintenance'),
        (LOW_MAINT, 'Low Maintenance'),
        (MEDIUM_MAINT, 'Medium Maintenance'),
    )
    FAST_RATE = 'FR'
    MEDIUM_RATE = 'LR'
    SLOW_RATE = 'SR'
    GROWTH_RATE_CHOICES = (
        (FAST_RATE, 'Fast Growth'),
        (MEDIUM_RATE, 'Medium Growth'),
        (SLOW_RATE, 'Slow Growth'),
    )
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=10000)
    fun_facts = models.CharField(max_length=500)
    price = models.FloatField()
    category = models.ForeignKey('Category', on_delete=models.PROTECT,
                                 related_name='trees')
    maintenance = models.CharField(choices=MAINTENANCE_CHOICES, max_length=2)
    height = models.FloatField()
    growth_rate = models.CharField(choices=GROWTH_RATE_CHOICES, max_length=2)
    year_one = models.CharField(max_length=100000)
    year_two = models.CharField(max_length=100000)
    year_three = models.CharField(max_length=100000)
    year_five = models.CharField(max_length=100000)
    year_ten = models.CharField(max_length=100000)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=10000)
    price = models.FloatField()
    category = models.ForeignKey('Category', on_delete=models.PROTECT,
                                 related_name='products')
    image = models.CharField(max_length=100000)


class Wishlist(models.Model):
    user = models.ForeignKey(django.contrib.auth.get_user_model(),
                             related_name='wishlist', on_delete=models.CASCADE)
    trees = models.ForeignKey('Tree', on_delete=models.PROTECT)
    products = models.ForeignKey('Product', on_delete=models.PROTECT)


class Cart(models.Model):
    user = models.ForeignKey(django.contrib.auth.get_user_model(),
                             related_name='cart', on_delete=models.CASCADE)
    trees = models.ForeignKey('Tree', on_delete=models.PROTECT)
    products = models.ForeignKey('Product', on_delete=models.PROTECT)
