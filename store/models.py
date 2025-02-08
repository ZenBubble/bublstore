from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save

class Item(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    cost = models.DecimalField(max_digits=10, decimal_places=2)
    
    def __str__(self):
        return self.name
    def num_review(self):
        return self.review_set.all().count()
    
class Cart(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    items = models.ManyToManyField(Item, blank=True)
    def __str__(self):
        return (self.user.username + "'s cart")
    def total_cost(self):
        return sum(item.cost for item in self.items.all())

# automatically creates the cart object and assigns to the new user
@receiver(post_save, sender=User)
def cart_create(sender, instance=None, created=False, **kwargs):
    if created:
        Cart.objects.create(user=instance)

class Review(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    item = models.ForeignKey(Item,on_delete=models.CASCADE)
    title = models.CharField(max_length=30)
    content = models.CharField(max_length=100)

class Order(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    item = models.ForeignKey(Item,on_delete=models.CASCADE)
    details = models.CharField(max_length=2000)