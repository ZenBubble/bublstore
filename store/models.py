from django.db import models
from django.contrib.auth.models import User

class WishList(models.Model):
    name = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published")

    def __str__(self):
        return self.name

class Item(models.Model):
    wishlist = models.ForeignKey(WishList, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    
    def __str__(self):
        return self.name
    # def num_review(self): #TODO: return number of reviews linked with this object
    #     return len(Review)
    
class Review(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    item = models.ForeignKey(Item,on_delete=models.CASCADE)
    title = models.CharField(max_length=30)
    content = models.CharField(max_length=100)