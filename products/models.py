from django.db import models

class vendor(models.Model):
    Vendor_name=models.CharField(max_length=200)
    product = models.ForeignKey('Products',on_delete=models.CASCADE)

class Products(models.Model):
    Name=models.CharField(max_length=100)
    price=models.IntegerField()
    quantity=models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = 'Products'


