from django.db import models
from django.contrib.auth.models import User

class UserAddress(models.Model):
    items = models.TextField()
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    address = models.TextField()
    contact = models.CharField(max_length=12)
    city = models.CharField(max_length=200)
    state = models.CharField(max_length=200)
    zip = models.IntegerField()
    price = models.IntegerField()
    cash_on_delivery = models.CharField(max_length=10, default=True)

    def __str__(self):
        return '%s %s %s' % (self.name, self.items, self.email)


