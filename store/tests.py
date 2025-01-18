import datetime

from django.test import TestCase
from django.utils import timezone

from .models import WishList

## FOR UNIT TESTING

class QuestionModelTests(TestCase): ## example test case, run by typing python manage.py test store
    def test_was_published_recently_with_future_question(self):
        """
        was_published_recently() returns False for questions whose pub_date
        is in the future.
        """
        time = timezone.now() + datetime.timedelta(days=30)
        future_question = WishList(pub_date=time)
        self.assertIs(future_question.was_created_recently(), False)

## VIEW TESTING (UI TESTING) IS A BIT MORE COMPLICATED, LOOK AT DJANGO DOCUMENTATION