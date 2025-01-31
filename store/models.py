from django.db import models
from django.contrib.auth.models import User

class Cart(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    def __str__(self):
        return self.name

class Item(models.Model):
    # cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    cost = models.DecimalField(max_digits=10, decimal_places=2)
    
    def __str__(self):
        return self.name
    def num_review(self): #TODO: return number of reviews linked with this object
        return self.review_set.all().count()
    
class Review(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    item = models.ForeignKey(Item,on_delete=models.CASCADE)
    title = models.CharField(max_length=30)
    content = models.CharField(max_length=100)