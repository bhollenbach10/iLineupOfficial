from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=16)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Categories'

class Product(models.Model):
    name = models.CharField(max_length=32)
    description = models.TextField()
    price = models.IntegerField()
    category = models.ForeignKey(Category)


    def __str__(self):
        return self.name




