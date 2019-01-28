from django.db import models

# Create your models here.
class Product(models.Model):
    SIZES = (
        ('S', 'Small'),
        ('M', 'Medium'),
        ('L', 'Large')
    )
    sku = models.CharField(max_length = 5)
    name = models.CharField(max_length = 20)
    price = models.PositiveIntegerField()
    size = models.CharField(max_length = 1, choices = SIZES)
    qty = models.PositiveIntegerField()

    def __repr__(self):
        return '<Product %r>' % self.name
