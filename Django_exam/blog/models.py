from django.db import models
from django.utils import timezone


# Create your models here.

class Product(models.Model):
    class RatingChoice(models.IntegerChoices):
        Zero = 0
        One = 1
        Two = 2
        Three = 3
        Four = 4
        Five = 5

    name = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    price = models.FloatField()
    rating = models.IntegerField(choices=RatingChoice.choices, default=RatingChoice.Zero.value)
    amount = models.IntegerField(default=1)
    discount = models.IntegerField()
    attribute = models.ManyToManyField('Attribute', related_name='attributes')
    # attribute_value = models.ManyToManyField('AttributeValue', blank=True, null=True)

    @property
    def discounted_price(self):
        if self.discount > 0:
            return self.price * (1 - self.discount / 100)
        return self.price

    def __str__(self):
        return self.name


class Image(models.Model):
    image = models.ImageField(upload_to='products/')
    product = models.ForeignKey('blog.Product', on_delete=models.CASCADE, related_name='images')


class Attribute(models.Model):
    attribute_name = models.CharField(max_length=100)

    def __str__(self):
        return self.attribute_name
    

class Customers(models.Model):
    image = models.ImageField(null=True, blank=True, upload_to='customers/')
    first_name = models.CharField(max_length= 20)
    last_name = models.CharField(max_length= 20)
    email = models.EmailField()
    phone = models.CharField(max_length= 15)
    address = models.TextField()
    joined_at = models.DateTimeField(default = timezone.now)

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"
    
    def initials(self):
        return f"{self.first_name[0]}{self.last_name[0]}"
    
