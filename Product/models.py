from django.db import models
from vendor.models import vendor
# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.FloatField()
    stock = models.IntegerField()
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    vendor = models.ForeignKey('vendor.vendor', on_delete=models.CASCADE)

    def __str__(self):
        return self.name
