import datetime

from django.db import models
from django.utils import timezone

class WishList(models.Model):
    name = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published")

    def __str__(self): ## defines what is returned when listed out
        return self.name
    def was_created_recently(self): ## custom defined function
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)


class Item(models.Model):
    wishlist = models.ForeignKey(WishList, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    
    def __str__(self):
        return self.name
    
class User(models.Model):
    name = models.CharField(max_length=30)
    
    def __str__(self):
        return self.name

class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    item = models.ForeignKey(Item,on_delete=models.CASCADE)
    title = models.CharField(max_length=30)
    content = models.CharField(max_length=100)