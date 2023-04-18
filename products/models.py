from django.db import models
# Create your models here.


class Product(models.Model):
    image = models.ImageField(blank=True, null=True)
    title = models.CharField(max_length=255)
    composition = models.TextField()
    rate = models.FloatField()
    created_data = models.DateField(auto_now=True)
    modified_data = models.DateField(auto_now_add=True)


class Review(models.Model):
    text = models.CharField(max_length=256)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    def __str__(self):
        return self.text
