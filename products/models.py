from django.db import models

# Create your models here.
class Product(models.Model):
    image = models.ImageField(blank=True, null=True)
    title = models.CharField(max_length=255)
    composition = models.TextField()
    rate = models.FloatField()
    created_data = models.DateField(auto_now=True)
    modified_data = models.DateField(auto_now_add=True)

