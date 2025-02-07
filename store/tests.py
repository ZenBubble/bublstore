from django.test import TestCase

from .models import *

## FOR UNIT TESTING, RUN PYTHON MANAGE.PY TEST

class ModelTests(TestCase):
    def setUp(self):
        global test_user, new_item
        test_user = User.objects.create()
        new_item = Item.objects.create(name='test1', cost='10', description='null')

    def test_num_reviews_zero_and_edge(self):
        self.assertEqual(new_item.num_review(), 0)
        new_review = Review.objects.create(item=new_item,user=test_user)
        self.assertEqual(new_item.num_review(), 1)

    def test_cart_user_link_and_adding_items(self):
        self.assertTrue(test_user.cart)
        cart = test_user.cart
        self.assertEqual(cart.total_cost(), 0)
        cart.items.add(new_item)
        self.assertEqual(cart.total_cost(), 10)

## VIEW TESTING (UI TESTING) IS A BIT MORE COMPLICATED, LOOK AT DJANGO DOCUMENTATION